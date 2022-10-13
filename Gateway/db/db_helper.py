import sqlite3
from sqlite3 import Error
from time import time
from json import dumps

# DB_NAME = "/apps/sd2/db/data.db"
DB_NAME = "BackupData.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        conn = None
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        return


def init_backup_db():
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS periodic_data (id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts INTEGER,  payload TEXT); """

    sql_create_trigger = """CREATE TRIGGER IF NOT EXISTS delete_tail AFTER INSERT ON periodic_data
                                BEGIN
                                    DELETE FROM periodic_data WHERE id%10000=NEW.id%10000 AND id!=NEW.id;
                                END;"""

    # create a database connection
    conn = create_connection(DB_NAME)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create trigger
        create_table(conn, sql_create_trigger)


def push_backup_data(payload):
    ts = int(time() * 1000)
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = "INSERT INTO sensor (ts,payload) VALUES ({},{})".format(ts, '\'' + payload + '\'')
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


def pop_backup_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = "SELECT * from sensor ORDER BY id DESC LIMIT 1;"
    cur.execute(db_cmd)
    data = cur.fetchone()
    if data:
        db_cmd = 'DELETE FROM sensor WHERE id ="' + str(data[0]) + '";'
        cur.execute(db_cmd)
        conn.commit()
        return data[1], data[2]
    conn.close()
    return None, None


#   write data to database test.db and sensor table
def write_data_db(payload):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    ex = None
    try:
        db_cmd = 'INSERT INTO sensor_status VALUES ({},{},{},{})'.format('\'' + str(payload['id']) + '\'',
                                                                         '\'' + str(payload['timestamp']) + '\'',
                                                                         '\'' + str(payload['sensor']) + '\'',
                                                                         '\'' + str(payload['payload']) + '\'')
        cur.execute(db_cmd)
        conn.commit()
    except Exception as e:
        ex = e
    finally:
        conn.close()
    if ex is not None:
        raise ex


def clear_sensor_status():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'DELETE FROM sensor_status;'
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


def delete_old_sensor_status(sensor, ts):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'DELETE FROM sensor_status WHERE sensor ="' + sensor + '" and timestamp <' + str(ts) + ';'
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


#   write data to database test.db and sensor table
def write_last_data_db(payload):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cmd = 'UPDATE last_value SET ts =' + str(payload['ts']) + ', payload = ' + '\'' + str(
        payload['payload']) + '\'' + ' WHERE id ="' + payload['id'] + '";'
    cur.execute(cmd)
    conn.commit()
    conn.close()


def write_new_last_value(payload):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    ex = None
    try:
        db_cmd = 'INSERT INTO last_value VALUES ({},{},{})'.format('\'' + str(payload['id']) + '\'',
                                                                   '\'' + str(payload['ts']) + '\'',
                                                                   '\'' + str(payload['payload']) + '\'')
        cur.execute(db_cmd)
        conn.commit()
    except Exception as e:
        ex = e
    finally:
        conn.close()
    if ex is not None:
        raise ex


def delete_last_data_by_id(id_):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'DELETE FROM last_value WHERE id ="' + str(id_) + '";'
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


def get_last_data_by_id(id_):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT * FROM last_value WHERE id ="' + str(id_) + '";'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


#   delete all data from sensor table
def delete_all_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'DELETE FROM sensor;'
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


def get_sensor_data(sensor):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT * FROM sensor_status WHERE sensor = "' + sensor + '";'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


#   get n data from table
def get_n_data(n_data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT * FROM sensor LIMIT ' + str(n_data) + ';'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


#   get latest name
def get_last_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'select * from sensor_status  ORDER BY timestamp DESC LIMIT 1;'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


#   get old data by timestamp
def get_new_data_by_timestamp(ts, sensor):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'select * from sensor_status where timestamp > ' + str(ts) + ' and sensor="' + sensor + '";'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


def get_old_data_by_two_timestamp(ts1, ts2, sensor):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'select * from sensor_status where ' + str(ts2) + ' < timestamp and timestamp < ' + str(
        ts1) + ' and sensor="' + sensor + '";'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


def delete_old_data_ts(ts, sensor):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'delete from sensor_status where ' + str(ts) + ' > timestamp  and sensor="' + sensor + '";'
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


#   get all data from table
def get_all_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT * FROM sensor_status;'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


#   delete n data
def delete_n_data(n):
    data_ = get_n_data(n)
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for data in data_:
        # print data
        id_ = data[0]
        db_cmd = 'DELETE FROM sensor_status WHERE id ="' + str(id_) + '";'
        # print db_cmd
        cur.execute(db_cmd)
    conn.commit()
    conn.close()


def delete_by_id(id_):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'DELETE FROM sensor_status WHERE id ="' + str(id_) + '";'
    # print db_cmd
    cur.execute(db_cmd)
    conn.commit()
    conn.close()


#   delete n data
def delete_array_data_timestamp(ts):
    data_ = get_new_data_by_timestamp(ts)
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for data in data_:
        # print data
        id_ = data[0]
        db_cmd = 'DELETE FROM sensor_status WHERE id ="' + str(id_) + '";'
        # print db_cmd
        cur.execute(db_cmd)
    conn.commit()
    conn.close()


def get_total_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT COUNT(*) FROM sensor_status;'
    cur.execute(db_cmd)
    total_data = cur.fetchall()
    conn.commit()
    conn.close()
    return total_data[0][0]


def get_total_old_data(ts):
    conn = sqlite3.connect(DB_NAME)
    # print ts
    cur = conn.cursor()
    db_cmd = 'SELECT COUNT(*) FROM sensor_status WHERE timestamp < ' + str(ts) + ';'
    cur.execute(db_cmd)
    total_data = cur.fetchall()
    conn.commit()
    conn.close()
    return total_data[0][0]


def write_new_data_db(id, json_data):
    # try:
    #     delete_last_data_by_id(id)
    # except:
    #     print 'asdasd'
    new_payload = {'id': id, 'ts': int(time() * 1000), 'payload': dumps(json_data)}
    write_last_data_db(new_payload)


def get_data(sensor, param):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    db_cmd = 'SELECT * FROM sensor_last_state WHERE sensor = "' + sensor + '" and param="' + param + '";'
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


def insert_data(cmd_id, ts_rcv_cmd):
    db_cmd = 'INSERT INTO transaction_data (cmd_id,ts_rcv_cmd) VALUES ({},{})'.format('"' + cmd_id + '"',
                                                                                      str(ts_rcv_cmd))
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


def update_data(cmd_id, cell, value):
    db_cmd = 'UPDATE transaction_data SET ' + cell + ' = ' + str(value) + ' ' + 'WHERE cmd_id = "' + cmd_id + '"'
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(db_cmd)
    all_data = cur.fetchall()
    conn.commit()
    conn.close()
    return all_data


def get_user_by_rfid(args):
    db_cmd = 'SELECT * FROM user WHERE rfid IN ({seq})'.format(seq=','.join(['?'] * len(args)))
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(db_cmd, args)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data


def update_user_by_rfid(args):
    db_cmd = 'UPDATE user SET balance = ? WHERE rfid = ?'
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(db_cmd, args)
    conn.commit()
    conn.close()

def update_user_new_entries(members_array):
    db_cmd = 'INSERT INTO user VALUES (?,?,?)'
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.executemany(db_cmd, members_array)
    conn.commit()
    conn.close()

def cursor_execute(cmd, arg=None):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    if arg is None:
        cur.execute(cmd)
    else:
        cur.execute(cmd, arg)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data

def get_all_user():
    db_cmd = 'SELECT * FROM user'
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(db_cmd)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data
