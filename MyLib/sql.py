# -*- coding: utf-8 -*-
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# 返回List
def list_read(table):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT name from {table}")
    print("读取数据成功")
    result = []
    for row in cursor:
        result.append(row[0])
    conn.close()

    return result


# 返回Name列表
def name_read(table, ls):
    if ls:
        wh = '(' + ', '.join(ls) + ')'
        conn = sqlite3.connect('.\\SQL\\maple.db')
        print("打开数据库成功")
        c = conn.cursor()
        cursor = c.execute(f"SELECT id from {table} where id in { wh }")
        print("读取数据成功")
        result = []
        for row in cursor:
            result.append(row[0])
        conn.close()

        return result
    else:
        return []


# 返回一行数据
def row_read(table, name):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    conn.row_factory = dict_factory
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT * from {table} where name=\"{name}\"")
    print("读取数据成功")
    result = cursor.fetchone()
    conn.close()
    return result


def row_save(table, data):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    conn.row_factory = dict_factory
    print("打开数据库成功")
    c = conn.cursor()
    print(data)

    name = ''
    value = ''
    for k, v in data.items():
        name += k + ', '
        if v is int:
            value += (str(v) + ', ')
        elif v is None:
            value += ('' + 'NULL' + ', ')
        else:
            value += ('\"' + str(v) + '\", ')
    print(f"replace into { table } ({ name[:-2] }) values ({ value[:-2] })")
    c.execute(f"replace into { table } ({ name[:-2] }) values ({ value[:-2] })")
    conn.commit()
    print("保存数据成功")
    conn.close()


# attr
# 返回List
def list_read_attr(table):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT time from {table}")
    print("读取数据成功")
    result = []
    for row in cursor:
        result.append(row[0])
    conn.close()

    return result


def row_read_attr(table, name):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    conn.row_factory = dict_factory
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT * from {table} where time=\"{name}\"")
    print("读取数据成功")
    result = cursor.fetchone()
    conn.close()
    return result


# attr
# code
def character_read_attr():
    conn = sqlite3.connect('.\\SQL\\maple.db')
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT nickname from character")
    print("读取数据成功")
    result = []
    for row in cursor:
        result.append(row[0])
    conn.close()

    return result


# 读取数据库
def all_read(table):
    conn = sqlite3.connect('.\\SQL\\maple.db')
    conn.row_factory = dict_factory
    print("打开数据库成功")
    c = conn.cursor()
    cursor = c.execute(f"SELECT * from {table}")
    print("读取数据成功")
    result = []
    for row in cursor:
        result.append(row)
    conn.close()

    return result


if __name__ == '__main__':
    print(list_read('character'))

