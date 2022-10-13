import logging
from os import system
from threading import Thread
from time import time, sleep
from zlib import compress
# import bluetooth
import paho.mqtt.client as mqtt
from flask import Flask, Response, request, render_template
from lib.utility.json_ import parse, stringify, safe_deep_get_with_type
from lib.webservice.wsrequest import JPOST
from lib.utility.file_ import save_json_file, load_json_file
from db.db_helper import push_backup_data
from mqtt import *


# Logger level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

global ENABLE_REUPLOAD
global reupload_backup_timer
global sock
FIRST_CONNECT = False
ENABLE_REUPLOAD = False
reupload_backup_timer = None

IOT_PATH = '/apps/sd1/conf/iot.json'
IOT_CONFIG = load_json_file(IOT_PATH)

COMMAND_TIMEOUT = 300
CONFIG_TIMEOUT = 300
SENSORS_TIMEOUT = 300
IOT_PORT = 5000

# Mqtt Connection
mqtt = Mqtt()


def subscribe_topic(_client):
    _client.subscribe(mqtt.subscribe_wildcard())


def __on_connect_task(_client, userdata, flags, rc):
    # Send online
    _client.publish(topic=mqtt.online(), payload='{}')

    global ENABLE_REUPLOAD
    global reupload_backup_timer
    ENABLE_REUPLOAD = True
    if rc == 0:
        try:
            logger.debug('[MQTT] Starting...')
        except:
            logger.debug('[MQTT] Error Connecting MQTT...')
        logger.debug('[MQTT] Connected OK')
        subscribe_topic(_client)
        logger.debug('[MQTT] Subscribed')

    else:
        logger.debug('[MQTT] Bad connection')
        subscribe_topic(_client)


def on_connect(_client, userdata, flags, rc):
    Thread(target=__on_connect_task, args=(_client, userdata, flags, rc)).start()


def __on_disconnect_task(_client, userdata, rc):
    global ENABLE_REUPLOAD
    global reupload_backup_timer
    ENABLE_REUPLOAD = False
    if reupload_backup_timer is not None:
        reupload_backup_timer.cancel()
        reupload_backup_timer = None
    try:
        logger.debug('[MQTT] Stopping Thread')
    except:
        logger.debug('[MQTT] Error Stopping Thread')
    logging.debug('[MQTT] Disconnecting reason  ' + str(rc))


def on_disconnect(_client, userdata, rc):
    Thread(target=__on_disconnect_task, args=(_client, userdata, rc)).start()


def get_specific_topic(long_topic):
    list_ = long_topic.split('/')
    return list_[-1]


def __on_message_task(_client, userdata, msg):
    payload = parse(msg.payload.decode('utf-8'))
    logger.debug('Payload : ' + str(payload))
    topic_ = get_specific_topic(msg.topic)
    logger.debug('Topic : ' + topic_)


def on_message(_client, userdata, msg):
    Thread(target=__on_message_task, args=(_client, userdata, msg)).start()


def publish_mqtt(_client, topic, payload):
    spayload = stringify(payload)
    ssc = compress(spayload.encode('utf8'))
    cpayload = bytearray(ssc)
    try:
        res = _client.publish(topic, cpayload, 1)
        if res:
            last_upload = int(time())
        else:
            push_backup_data(spayload)
    except:
        push_backup_data(spayload)


def publish_mqtt_text_uncompressed(_client, topic, payload):
    try:
        _client.publish(topic, stringify(payload), 2)
        logger.debug('[MQTT] Published')
    except:
        pass


_client = None

while not FIRST_CONNECT:
    try:
        _client = mqtt.Client()
        _client.username_pw_set(username=mqtt.mqtt_username, password=mqtt.mqtt_password)
        _client.will_set(mqtt.offline(), '{}', 0, False)
        _client.tls_set()
        _client.connect(mqtt.MQTT_HOST, port=mqtt.MQTT_PORT, keepalive=10, bind_address='')
        _client.on_connect = on_connect
        _client.on_disconnect = on_disconnect
        _client.on_message = on_message
        _client.loop_start()
        FIRST_CONNECT = True
    except Exception as e:
        logger.debug(e)
        logger.debug('[MQTT] Connect to MQTT broker Failed')
        sleep(5)

# Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    body = request.get_json()
    if body is None:
        return Response(status=400)
    publish_mqtt_text_uncompressed(_client, mqtt.data(), body)
    return Response('OK', status=200, mimetype='text/plain')

@app.route('/bl_scan', methods=['POST'])
def bl_scan():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    bl_array = []
    for addr in nearby_devices:
        bl_array.append(addr)
    bl_dict = {}
    bl_dict['bl_list'] = bl_array
    return Response(response=stringify(bl_dict), status=200, mimetype="application/json")

@app.route('/connect_bl', methods=['POST'])
def connect_bl():
    global sock
    try:
        body = request.get_json()
        if body is None:
            return Response(status=400)
        addr = safe_deep_get(body, ['addr'])
        service_matches = bluetooth.find_service(address=addr)
        if len(service_matches) == 0:
            print("couldn't find the SampleServer service =(")
            return Response(status=400)

        for s in range(len(service_matches)):
            print("\nservice_matches: [" + str(s) + "]:")
            print(service_matches[s])

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]
        port=1
        print("connecting to \"%s\" on %s, port %s" % (name, host, port))
        # Create the client socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))
        return Response(status=200)
    except:
        return Response(status=400)

@app.route('/connect_bl', methods=['POST'])
def disconnect_bl():
    global sock
    sock.close()
    return Response(200)

@app.route('/data_stream')
def data_stream():
    def stream():
        try:
            while True:
                data = sock.recv(1024)
                if not data:
                    break
        except OSError:
            pass
        yield data  # return also will work
    return Response(stream(), mimetype='text')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=IOT_PORT)
