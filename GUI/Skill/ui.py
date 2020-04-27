# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from GUI.key import skill


def skill_ui():
    # # 分页4——技能
    frame_layout_s_p = [
        [sg.Text('HP', size=(5, 0), font='Any 12', key=skill['text']['hp']), sg.Input(key=skill['data']['hp'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('MP', size=(5, 0), font='Any 12', key=skill['text']['mp']), sg.Input(key=skill['data']['mp'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('STR', size=(5, 0), font='Any 12', key=skill['text']['str']), sg.Input(key=skill['data']['str'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('DEX', size=(5, 0), font='Any 12', key=skill['text']['dex']), sg.Input(key=skill['data']['dex'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('VIT', size=(5, 0), font='Any 12', key=skill['text']['vit']), sg.Input(key=skill['data']['vit'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('INT', size=(5, 0), font='Any 12', key=skill['text']['int']), sg.Input(key=skill['data']['int'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('AGI', size=(5, 0), font='Any 12', key=skill['text']['agi']), sg.Input(key=skill['data']['agi'], size=(8, 0), font='Any 12', enable_events=True)]
    ]
    frame_layout_s_pp = [
        [sg.Text('HP', size=(5, 0), font='Any 12', key=skill['text']['hp_p']), sg.Input(key=skill['data']['hp_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('MP', size=(5, 0), font='Any 12', key=skill['text']['mp_p']), sg.Input(key=skill['data']['mp_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('STR', size=(5, 0), font='Any 12', key=skill['text']['str_p']), sg.Input(key=skill['data']['str_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('DEX', size=(5, 0), font='Any 12', key=skill['text']['dex_p']), sg.Input(key=skill['data']['dex_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('VIT', size=(5, 0), font='Any 12', key=skill['text']['vit_p']), sg.Input(key=skill['data']['vit_p'], size=(8, 0), font='Any 12', enable_events=True),
         sg.Text('INT', size=(5, 0), font='Any 12', key=skill['text']['int_p']), sg.Input(key=skill['data']['int_p'], size=(8, 0), font='Any 12', enable_events=True)],
        [sg.Text('AGI', size=(5, 0), font='Any 12', key=skill['text']['agi_p']), sg.Input(key=skill['data']['agi_p'], size=(8, 0), font='Any 12', enable_events=True)]
    ]
    frame_layout_s_cs = [
        [sg.Listbox(values=[], size=(40, 6), key=skill['children']['list'], enable_events=True),
         sg.Combo([], key=skill['children']['choose'], enable_events=True, size=(10, 10), font='Any 16',)]
    ]
    frame_layout = [
        [sg.Text('ID', size=(10, 0), font='Any 16', key=skill['text']['id']), sg.Input(key=skill['data']['id'], size=(30, 0), disabled=True, font='Any 16', enable_events=True)],
        [sg.Text('Name', size=(10, 0), font='Any 16', key=skill['text']['name']), sg.Input(key=skill['data']['name'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Frame('Point', frame_layout_s_p, font='Any 12', title_color='blue'),
         sg.Frame('PointPCT', frame_layout_s_pp, font='Any 12', title_color='blue')],
        [sg.Text('Buff', size=(10, 0), font='Any 16', key=skill['text']['buff']), sg.Input(key=skill['data']['buff'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Debuff', size=(10, 0), font='Any 16', key=skill['text']['debuff']), sg.Input(key=skill['data']['debuff'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Kind', size=(10, 0), font='Any 16', key=skill['text']['kind']),
         sg.Radio('主动', "SKIND", key=skill['data']['active'], default=True, font='Any 16', enable_events=True),
         sg.Radio('被动', "SKIND", key=skill['data']['passive'], font='Any 16', enable_events=True),
         sg.Radio('触发', "SKIND", key=skill['data']['trigger'], font='Any 16', enable_events=True)],
        [sg.Text('Use', size=(10, 0), font='Any 16', key=skill['text']['use']), sg.Input(key=skill['data']['use'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Text('Time', size=(10, 0), font='Any 16', key=skill['text']['time']), sg.Input(key=skill['data']['time'], size=(30, 0), font='Any 16', enable_events=True)],
        [sg.Frame('ChildrenSkill', frame_layout_s_cs, font='Any 12', title_color='blue')],
        [sg.Text('Intro', size=(10, 0), font='Any 16', key=skill['text']['access']),  sg.Multiline('', font='Any 12', key=skill['data']['access'], size=(50, 6))],
        [sg.Button('保存', key=skill['button']['save'], pad=(20, 10), size=(15, 2), disabled=True, enable_events=True),
         sg.Button('新增', key=skill['button']['new'], pad=(20, 10), size=(15, 2), enable_events=True),
         sg.Button('清空', key=skill['button']['clear'], pad=(20, 10), size=(15, 2), enable_events=True)]
    ]
    return [[
        sg.Listbox(values=[], size=(40, 20), key=skill['list'], enable_events=True),
        sg.Frame('Skill', frame_layout, size=(80, 20), pad=(40, 0), font='Any 20', title_color='blue')
    ]]



