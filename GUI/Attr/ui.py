# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from GUI.key import attr


def attr_ui():
    frame_layout_a_p = [
        [sg.Text('HP', size=(5, 0), font='Any 12', key=attr['text']['hp']), sg.Input(key=attr['data']['hp'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('MP', size=(5, 0), font='Any 12', key=attr['text']['mp']), sg.Input(key=attr['data']['mp'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('STR', size=(5, 0), font='Any 12', key=attr['text']['str']), sg.Input(key=attr['data']['str'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('DEX', size=(5, 0), font='Any 12', key=attr['text']['dex']), sg.Input(key=attr['data']['dex'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('VIT', size=(5, 0), font='Any 12', key=attr['text']['vit']), sg.Input(key=attr['data']['vit'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('INT', size=(5, 0), font='Any 12', key=attr['text']['int']), sg.Input(key=attr['data']['int'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('AGI', size=(5, 0), font='Any 12', key=attr['text']['agi']), sg.Input(key=attr['data']['agi'], size=(8, 0), font='Any 12', enable_events=True)]
    ]
    frame_layout_a_e = [
        [sg.Text('Head', size=(5, 0), font='Any 12', key=attr['text']['head']), sg.Combo(attr['data']['head'], size=(8, 0), font='Any 12', key=attr['data']['head'], enable_events=True),
         sg.Text('Body', size=(5, 0), font='Any 12', key=attr['text']['body']), sg.Combo(attr['data']['body'], size=(8, 0), font='Any 12', key=attr['data']['body'], enable_events=True)],
        [sg.Text('RHand', size=(5, 0), font='Any 12', key=attr['text']['r_hand']), sg.Combo(attr['data']['r_hand'], size=(8, 0), font='Any 12', key=attr['data']['r_hand'], enable_events=True),
         sg.Text('LHand', size=(5, 0), font='Any 12', key=attr['text']['l_hand']), sg.Combo(attr['data']['l_hand'], size=(8, 0), font='Any 12', key=attr['data']['l_hand'], enable_events=True)],
        [sg.Text('Leg', size=(5, 0), font='Any 12', key=attr['text']['log']), sg.Combo(attr['data']['log'], size=(8, 0), font='Any 12', key=attr['data']['log'], enable_events=True),
         sg.Text('Foot', size=(5, 0), font='Any 12', key=attr['text']['foot']), sg.Combo(attr['data']['foot'], size=(8, 0), font='Any 12', key=attr['data']['foot'], enable_events=True)],
        [sg.Text('Jew1', size=(5, 0), font='Any 12', key=attr['text']['jew1']), sg.Combo(attr['data']['jew1'], size=(8, 0), font='Any 12', key=attr['data']['jew1'], enable_events=True),
         sg.Text('Jew2', size=(5, 0), font='Any 12', key=attr['text']['jew2']), sg.Combo(attr['data']['jew2'], size=(8, 0), font='Any 12', key=attr['data']['jew2'], enable_events=True)],
        [sg.Text('Jew3', size=(5, 0), font='Any 12', key=attr['text']['jew3']), sg.Combo(attr['data']['jew3'], size=(8, 0), font='Any 12', key=attr['data']['jew3'], enable_events=True)]
    ]

    frame_layout_a_s = [
        [sg.Listbox(values=[], size=(40, 6), key=attr['skill']['list'], enable_events=True),
         sg.Combo([], key=attr['skill']['choose'], enable_events=True, size=(10, 0), font='Any 16',)]
    ]

    frame_layout = [
        [sg.Text('ID', size=(10, 0), font='Any 16', key=attr['text']['id']), sg.Input(size=(30, 0), key=attr['data']['id'], disabled=True, font='Any 16', enable_events=True)],
        [sg.Text('Level', size=(10, 0), key=attr['text']['level'], font='Any 16'), sg.Input(key=attr['data']['level'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Time', size=(10, 0), key=attr['text']['time'], font='Any 16'),
         sg.Input(key=attr['data']['time'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('TimeA', size=(10, 0), key=attr['text']['time_a'], font='Any 16'),
         sg.Input(key=attr['data']['time_a'], size=(30, 0), font='Any 16', enable_events=True)],

        [sg.Text('Character', size=(10, 0), font='Any 16', key=attr['text']['code']),
         sg.Combo([], size=(8, 0), font='Any 16', key=attr['data']['code'], enable_events=True)],

        [sg.Frame('Point', frame_layout_a_p, font='Any 12', title_color='blue'),
         sg.Frame('Eqpt', frame_layout_a_e, font='Any 12', title_color='blue')],
        [sg.Frame('Skill', frame_layout_a_s, font='Any 12', title_color='blue')],

        [sg.Button('保存', key=attr['button']['save'], pad=(20, 10), size=(15, 2), disabled=True),
         sg.Button('新增', key=attr['button']['new'], pad=(20, 10), size=(15, 2)),
         sg.Button('清空', key=attr['button']['clear'], pad=(20, 10), size=(15, 2))]
    ]
    return [[
        sg.Listbox(values=[], size=(40, 20), key=attr['list'], enable_events=True),
        sg.Frame('Attr', frame_layout, size=(80, 20), pad=(40, 0), font='Any 20', title_color='blue')
    ]]

