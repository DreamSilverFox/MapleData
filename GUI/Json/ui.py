# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from GUI.key import json


def json_ui():
    return [
        [sg.Text('', size=(10, 0), font='Any 48', key=json['text'], pad=((200, 200), (200, 20)))],
        [sg.Button('保存', key=json['button'], pad=(20, 10), size=(50, 10))]
    ]

