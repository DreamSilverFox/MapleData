# -*- coding: utf-8 -*-
from GUI.gui import event, w
from GUI.key import *

from GUI.change import change

from GUI.button import save, new, clear

import MyLib.sql as sql


def attr_event():
    # list
    if event['c'] == attr['list']:
        get(sql.row_read_attr('attr', event['d'][attr['list']][0]))

    # button
    if event['c'] == attr['button']['save']:
        data = {}
        for key, value in attr['data'].items():
            data[key] = event['d'][attr['data'][key]]
        if w[attr['skill']['list']].get_list_values():
            data['skill'] = ' '.join(w[attr['skill']['list']].get_list_values())
        else:
            data['skill'] = None
        save('attr', data)
    if event['c'] == attr['button']['new']:
        new('attr')
    if event['c'] == attr['button']['clear']:
        clear('attr')

    # change
    if event['c'] in list(attr['data'].values()):
        change(attr['text'][attr['relate'][event['c']]])

    # skill select
    if event['c'] == attr['skill']['choose']:
        attr_skill_list = list(w[attr['skill']['list']].get_list_values())
        attr_skill_list.append(event['d'][attr['skill']['choose']])
        attr_skill_list_new = list(set(attr_skill_list))
        attr_skill_list_new.sort(key=attr_skill_list.index)
        w[attr['skill']['list']].update(values=attr_skill_list_new)
    # skill delete
    if event['c'] == attr['skill']['list']:
        li = list(w[attr['skill']['list']].get_list_values())
        li.remove(event['d'][attr['skill']['list']][0])
        w[attr['skill']['list']].update(values=li)
        

def get(dt):
    print(dt)
    w[attr['data']['id']].update(value=dt['id'])
    w[attr['data']['time']].update(value=dt['time'])
    w[attr['data']['time_a']].update(value=dt['time_a'])
    w[attr['data']['level']].update(value=dt['level'])
    w[attr['data']['code']].update(value=dt['code'])

    w[attr['data']['hp']].update(value=dt['hp'])
    w[attr['data']['mp']].update(value=dt['mp'])
    w[attr['data']['str']].update(value=dt['str'])
    w[attr['data']['vit']].update(value=dt['vit'])
    w[attr['data']['agi']].update(value=dt['agi'])
    w[attr['data']['dex']].update(value=dt['dex'])
    w[attr['data']['int']].update(value=dt['int'])

    w[attr['data']['head']].update(value=dt['head'])
    w[attr['data']['body']].update(value=dt['body'])
    w[attr['data']['r_hand']].update(value=dt['r_hand'])
    w[attr['data']['l_hand']].update(value=dt['l_hand'])
    w[attr['data']['log']].update(value=dt['log'])
    w[attr['data']['foot']].update(value=dt['foot'])
    w[attr['data']['jew1']].update(value=dt['jew1'])
    w[attr['data']['jew2']].update(value=dt['jew2'])
    w[attr['data']['jew3']].update(value=dt['jew3'])

    if dt['skill']:
        w[attr['skill']['list']].update(values=dt['skill'].split(' '))
    else:
        w[attr['skill']['list']].update(values=[])

    # button
    w[attr['button']['save']].update(disabled=False)





