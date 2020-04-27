# -*- coding: utf-8 -*-
from GUI.gui import event, w
from GUI.key import json

import MyLib.sql as sql

import json as js


def write_list_to_json(ls, json_file_name):
    """
    将list写入到json文件
    :param ls:
    :param json_file_name: 写入的json文件名字
    :return:
    """
    with open(json_file_name, 'w') as f:
        js.dump(ls, f, ensure_ascii=True, indent=4)


def json_event():
    # list
    if event['c'] == json['button']:
        write_list_to_json(sql.all_read('character'), 'Save/character.json')
        write_list_to_json(sql.all_read('skill'), 'Save/skill.json')
        write_list_to_json(sql.all_read('eqpt'), 'Save/eqpt.json')
        write_list_to_json(sql.all_read('attr'), 'Save/attr.json')




