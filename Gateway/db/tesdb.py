import logging
from db_helper import get_user_by_rfid,get_all_user, update_user_by_rfid, update_user_new_entries, cursor_execute
import sqlite3


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


def update_balance(rfid, price):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute('SELECT balance from user WHERE rfid = {arg}'.format(arg=rfid))
    data = cur.fetchone()
    updated_balance = int(data[0]) - price
    cur.execute('UPDATE user SET balance = ? WHERE rfid = ?', (updated_balance, rfid))
    conn.commit()
    conn.close()
def get_balance(rfid):
    data = cursor_execute('SELECT balance from user WHERE rfid = {arg}'.format(arg=rfid))
    # logger.info("Checking Balance.....")
    return data[0]
def set_member_balance(balance, rfid):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute('UPDATE user SET balance = ? WHERE rfid = ?', (balance, rfid))
    conn.commit()
    conn.close()
def set_all_balance(balance):
    cursor_execute('UPDATE user SET balance = {arg}'.format(arg=balance))


def get_all_balance():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    data = {}
    for row in cur.execute("SELECT * FROM user"):
        data[row[0]] = int(row[1])
    return data

print(get_all_balance())
# members_dict = {"1001": 1000, "101112": 50000, "1003": 50000, "1004": 50000, "1005": 50000, "1020": 50000}
# print(members_dict)
# new_data = list(members_dict.keys())
# user = get_all_user()
# old_data = list()
# for row in user:
#     rfid = row[0]
#     old_data.append(rfid)
# # Check if there is deleted data from new CSV
# deleted_data = diff(old_data, new_data)
# if not deleted_data:
#     print("No Deleted Data")
# else:
#     for row in deleted_data:
#         rfid = row
#         conn = sqlite3.connect("data.db")
#         cur = conn.cursor()
#         cur.execute('DELETE FROM user WHERE rfid = ?', (rfid,))
#         conn.commit()
#         conn.close()
# # list rfid yang sudah ada stocknya
# data = get_user_by_rfid(new_data)
# # update config rfid yang sudah ada stocknya, delete dari dict
# for row in data:
#     rfid = row[0]
#     args = (members_dict[rfid], rfid)
#     update_user_by_rfid(args)
#     del members_dict[rfid]
# # create new entries in DB for new data
# members_array = []
# for key, value in members_dict.items():
#     members_array.append((key, value))
# # update_user_new_entries(members_array)
# db_cmd = 'INSERT INTO user VALUES (?,?)'
# conn = sqlite3.connect("data.db")
# cur = conn.cursor()
# cur.executemany(db_cmd, members_array)
# conn.commit()
# conn.close()