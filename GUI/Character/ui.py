# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from GUI.key import character


def character_ui():
    frame_layout = [
        [sg.Text('ID', size=(10, 0), font='Any 16', key=character['text']['id']), sg.Input(size=(30, 0), key=character['data']['id'], disabled=True, font='Any 16', enable_events=True)],
        [sg.Text('Name', size=(10, 0), key=character['text']['name'], font='Any 16'), sg.Input(key=character['data']['name'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('NickName', size=(10, 0), key=character['text']['nickname'], font='Any 16'), sg.Input(key=character['data']['nickname'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Cv', size=(10, 0), key=character['text']['cv'], font='Any 16'), sg.Input(key=character['data']['cv'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Sex', size=(10, 0), key=character['text']['sex'], font='Any 16'),
         sg.Radio('男', "SEX", key=character['data']['male'], default=True, font='Any 16', enable_events=True),
         sg.Radio('女', "SEX", key=character['data']['female'], font='Any 16', enable_events=True)],
        [sg.Text('Intro', size=(10, 0), key=character['text']['intro'], font='Any 16'), sg.Multiline(key=character['data']['intro'], size=(50, 10), font='Any 12', enable_events=True)],
        [sg.Button('保存', key=character['button']['save'], pad=(20, 10), size=(15, 2), disabled=True),
         sg.Button('新增', key=character['button']['new'], pad=(20, 10), size=(15, 2)),
         sg.Button('清空', key=character['button']['clear'], pad=(20, 10), size=(15, 2))]
    ]
    return [[
        sg.Listbox(values=[], size=(40, 20), key=character['list'], enable_events=True),
        sg.Frame('Character', frame_layout, size=(80, 20), pad=(40, 0), font='Any 20', title_color='blue')
    ]]

