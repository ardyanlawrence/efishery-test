from lib.utility.json_ import safe_deep_get
from lib.utility.object import is_either_none
from lib.utility.file_ import load_json_file


class Mqtt:
    MQTT_HOST = '82893f05d8f441a0a872cab8a9d884e1.s1.eu.hivemq.cloud'
    MQTT_PORT = 8883

    def __init__(self):
        self.mqtt_json = load_json_file('conf/mqtt.json')
        self.mqtt_username = safe_deep_get(self.mqtt_json, ['username'])
        self.mqtt_password = safe_deep_get(self.mqtt_json, ['password'])

        if is_either_none(self.mqtt_application_id, self.mqtt_device_id):
            raise ValueError('application_id or device_id undefined')

    def data(self):
        return 'mqtt/pub/data'

    def online(self):
        return 'mqtt/pub/online'

    def offline(self):
        return 'mqtt/pub/offline'

    def subscribe_wildcard(self):
        return '/+'
