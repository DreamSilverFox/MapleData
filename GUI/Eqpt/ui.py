# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from GUI.key import eqpt


def eqpt_ui():
    frame_layout_e_p = [
        [sg.Text('HP', size=(5, 0), font='Any 12', key=eqpt['text']['hp']), sg.Input(key=eqpt['data']['hp'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('MP', size=(5, 0), font='Any 12', key=eqpt['text']['mp']), sg.Input(key=eqpt['data']['mp'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('STR', size=(5, 0), font='Any 12', key=eqpt['text']['str']), sg.Input(key=eqpt['data']['str'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('DEX', size=(5, 0), font='Any 12', key=eqpt['text']['dex']), sg.Input(key=eqpt['data']['dex'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('VIT', size=(5, 0), font='Any 12', key=eqpt['text']['vit']), sg.Input(key=eqpt['data']['vit'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('INT', size=(5, 0), font='Any 12', key=eqpt['text']['int']), sg.Input(key=eqpt['data']['int'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('AGI', size=(5, 0), font='Any 12', key=eqpt['text']['agi']), sg.Input(key=eqpt['data']['agi'], size=(8, 0), font='Any 12', enable_events=True)]
    ]
    frame_layout_e_pp = [
        [sg.Text('HP', size=(5, 0), font='Any 12', key=eqpt['text']['hp_p']), sg.Input(key=eqpt['data']['hp_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('MP', size=(5, 0), font='Any 12', key=eqpt['text']['mp_p']), sg.Input(key=eqpt['data']['mp_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('STR', size=(5, 0), font='Any 12', key=eqpt['text']['str_p']), sg.Input(key=eqpt['data']['str_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('DEX', size=(5, 0), font='Any 12', key=eqpt['text']['dex_p']), sg.Input(key=eqpt['data']['dex_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('VIT', size=(5, 0), font='Any 12', key=eqpt['text']['vit_p']), sg.Input(key=eqpt['data']['vit_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('INT', size=(5, 0), font='Any 12', key=eqpt['text']['int_p']), sg.Input(key=eqpt['data']['int_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('AGI', size=(5, 0), font='Any 12', key=eqpt['text']['agi_p']), sg.Input(key=eqpt['data']['agi_p'], size=(8, 0), font='Any 12', enable_events=True)]
    ]

    frame_layout_e_sk = [
        [sg.Listbox(values=[], size=(18, 6), key=eqpt['skill']['list'], enable_events=True),
         sg.Combo([], key=eqpt['skill']['choose'], enable_events=True, size=(8, 10), font='Any 16')]
    ]
    frame_layout_e_sl = [
        [sg.Listbox(values=[], size=(18, 6), key=eqpt['slot']['list'], enable_events=True),
         sg.Combo([], key=eqpt['slot']['choose'], enable_events=True, size=(8, 10), font='Any 16')]
    ]
    frame_layout = [
        [sg.Text('ID', size=(10, 0), font='Any 16', key=eqpt['text']['id']), sg.Input(size=(30, 0), key=eqpt['data']['id'], disabled=True, font='Any 16', enable_events=True)],
        [sg.Text('Name', size=(10, 0), key=eqpt['text']['name'], font='Any 16'), sg.Input(key=eqpt['data']['name'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Frame('Point', frame_layout_e_p, font='Any 12', title_color='blue'),
         sg.Frame('PointPCT', frame_layout_e_pp, font='Any 12', title_color='blue')],
        [sg.Frame('Skill', frame_layout_e_sk, font='Any 12', title_color='blue'),
         sg.Frame('Slot', frame_layout_e_sl, font='Any 12', title_color='blue')],
        [sg.Text('Access', size=(10, 0), key=eqpt['text']['access'], font='Any 16'), sg.Multiline(key=eqpt['data']['access'], size=(50, 10), font='Any 12', enable_events=True)],
        [sg.Button('保存', key=eqpt['button']['save'], pad=(20, 10), size=(15, 2), disabled=True),
         sg.Button('新增', key=eqpt['button']['new'], pad=(20, 10), size=(15, 2)),
         sg.Button('清空', key=eqpt['button']['clear'], pad=(20, 10), size=(15, 2))]
    ]
    return [[
        sg.Listbox(values=[], size=(40, 20), key=eqpt['list'], enable_events=True),
        sg.Frame('Eqpt', frame_layout, size=(80, 20), pad=(40, 0), font='Any 20', title_color='blue')
    ]]

