# -*- coding: utf-8 -*-
from GUI.gui import event, w
from GUI.key import *

from GUI.change import change

from GUI.button import save, new, clear

import MyLib.sql as sql


def eqpt_event():
    # list
    if event['c'] == eqpt['list']:
        get(sql.row_read('eqpt', event['d'][eqpt['list']][0]))

    # button
    if event['c'] == eqpt['button']['save']:
        data = {}
        for key, value in eqpt['data'].items():
            data[key] = event['d'][eqpt['data'][key]]
        if w[eqpt['skill']['list']].get_list_values():
            data['skill'] = ' '.join(w[eqpt['skill']['list']].get_list_values())
        else:
            data['skill'] = None

        if w[eqpt['slot']['list']].get_list_values():
            data['slot'] = ' '.join(w[eqpt['slot']['list']].get_list_values())
        else:
            data['slot'] = None

        save('eqpt', data)

    if event['c'] == eqpt['button']['new']:
        new('eqpt')
    if event['c'] == eqpt['button']['clear']:
        clear('eqpt')

    # change
    if event['c'] in list(eqpt['data'].values()):
        # print(eqpt['text'][eqpt['relate'][event['c']]])
        print(event['c'])
        change(eqpt['text'][eqpt['relate'][event['c']]])

    # skill select
    if event['c'] == eqpt['skill']['choose']:
        eqpt_skill_list = list(w[eqpt['skill']['list']].get_list_values())
        eqpt_skill_list.append(event['d'][eqpt['skill']['choose']])
        eqpt_skill_list_new = list(set(eqpt_skill_list))
        eqpt_skill_list_new.sort(key=eqpt_skill_list.index)
        w[eqpt['skill']['list']].update(values=eqpt_skill_list_new)
    # skill delete
    if event['c'] == eqpt['skill']['list']:
        li = list(w[eqpt['skill']['list']].get_list_values())
        li.remove(event['d'][eqpt['skill']['list']][0])
        w[eqpt['skill']['list']].update(values=li)

    # slot select
    if event['c'] == eqpt['slot']['choose']:
        eqpt_slot_list = list(w[eqpt['slot']['list']].get_list_values())
        eqpt_slot_list.append(event['d'][eqpt['slot']['choose']])
        eqpt_slot_list_new = list(set(eqpt_slot_list))
        eqpt_slot_list_new.sort(key=eqpt_slot_list.index)
        w[eqpt['slot']['list']].update(values=eqpt_slot_list_new)
    # slot delete
    if event['c'] == eqpt['slot']['list']:
        li = list(w[eqpt['slot']['list']].get_list_values())
        li.remove(event['d'][eqpt['slot']['list']][0])
        w[eqpt['slot']['list']].update(values=li)

def get(dt):
    w[eqpt['data']['id']].update(value=dt['id'])
    w[eqpt['data']['name']].update(value=dt['name'])
    w[eqpt['data']['access']].update(value=dt['access'])

    w[eqpt['data']['hp']].update(value=dt['hp'])
    w[eqpt['data']['mp']].update(value=dt['mp'])
    w[eqpt['data']['str']].update(value=dt['str'])
    w[eqpt['data']['vit']].update(value=dt['vit'])
    w[eqpt['data']['agi']].update(value=dt['agi'])
    w[eqpt['data']['dex']].update(value=dt['dex'])
    w[eqpt['data']['int']].update(value=dt['int'])

    w[eqpt['data']['hp_p']].update(value=dt['hp_p'])
    w[eqpt['data']['mp_p']].update(value=dt['mp_p'])
    w[eqpt['data']['str_p']].update(value=dt['str_p'])
    w[eqpt['data']['vit_p']].update(value=dt['vit_p'])
    w[eqpt['data']['agi_p']].update(value=dt['agi_p'])
    w[eqpt['data']['dex_p']].update(value=dt['dex_p'])
    w[eqpt['data']['int_p']].update(value=dt['int_p'])
    if dt['skill']:
        w[eqpt['skill']['list']].update(values=dt['skill'].split(' '))
    else:
        w[eqpt['skill']['list']].update(values=[])

    if dt['slot']:
        w[eqpt['slot']['list']].update(values=dt['slot'].split(' '))
    else:
        w[eqpt['slot']['list']].update(values=[])
    # button
    w[eqpt['button']['save']].update(disabled=False)


