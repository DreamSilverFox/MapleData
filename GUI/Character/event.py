# -*- coding: utf-8 -*-
from GUI.gui import event, w
from GUI.key import *

from GUI.change import change

from GUI.button import save, new, clear

import MyLib.sql as sql


def character_event():
    # list
    if event['c'] == character['list']:
        get(sql.row_read('character', event['d'][character['list']][0]))

    # button
    if event['c'] == character['button']['save']:
        data = {}
        for key, value in character['data'].items():
            if value in (character['data']['male'], character['data']['female']):
                if event['d'][character['data']['male']]:

                    data['sex'] = 0
                else:
                    data['sex'] = 1
            else:
                data[key] = event['d'][character['data'][key]]
        save('character', data)
    if event['c'] == character['button']['new']:
        new('character')
    if event['c'] == character['button']['clear']:
        clear('character')

    # change
    if event['c'] in list(character['data'].values()):
        change(character['text'][character['relate'][event['c']]])


def get(dt):
    w[character['data']['id']].update(value=dt['id'])
    w[character['data']['name']].update(value=dt['name'])
    w[character['data']['nickname']].update(value=dt['nickname'])
    w[character['data']['cv']].update(value=dt['cv'])

    if dt['sex']:
        w[character['data']['female']].update(value=True)
    else:
        w[character['data']['male']].update(value=True)

    w[character['data']['intro']].update(value=dt['intro'])

    # button
    w[character['button']['save']].update(disabled=False)