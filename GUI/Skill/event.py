# -*- coding: utf-8 -*-
from GUI.gui import event, w
from GUI.key import *

from GUI.change import change

from GUI.button import save, new, clear

import MyLib.sql as sql


def skill_event():
    # list
    if event['c'] == skill['list']:
        get(sql.row_read('skill', event['d'][skill['list']][0]))

    # button
    if event['c'] == skill['button']['save']:
        data = {}
        for key, value in skill['data'].items():
            if value in (skill['data']['active'], skill['data']['passive'], skill['data']['trigger']):
                if event['d'][skill['data']['active']]:
                    data['kind'] = 0
                elif event['d'][skill['data']['passive']]:
                    data['kind'] = 1
                else:
                    data['kind' \
                         ''] = 2
            else:
                data[key] = event['d'][skill['data'][key]]
        if w[skill['children']['list']].get_list_values():
            data['skill'] = ' '.join(w[skill['children']['list']].get_list_values())
        else:
            data['skill'] = None
        save('skill', data)
    if event['c'] == skill['button']['new']:
        new('skill')
    if event['c'] == skill['button']['clear']:
        clear('skill')

    # change
    if event['c'] in list(skill['data'].values()):
        change(skill['text'][skill['relate'][event['c']]])

    # children select
    if event['c'] == skill['children']['choose']:
        print("bbb")
        skill_children_list = list(w[skill['children']['list']].get_list_values())
        skill_children_list.append(event['d'][skill['children']['choose']])
        skill_children_list_new = list(set(skill_children_list))
        skill_children_list_new.sort(key=skill_children_list.index)
        w[skill['children']['list']].update(values=skill_children_list_new)
    # children delete
    if event['c'] == skill['children']['list']:
        li = list(w[skill['children']['list']].get_list_values())
        li.remove(event['d'][skill['children']['list']][0])
        w[skill['children']['list']].update(values=li)


def get(dt):
    w[skill['data']['id']].update(value=dt['id'])
    w[skill['data']['name']].update(value=dt['name'])
    w[skill['data']['buff']].update(value=dt['buff'])
    w[skill['data']['debuff']].update(value=dt['debuff'])
    w[skill['data']['use']].update(value=dt['use'])
    w[skill['data']['time']].update(value=dt['time'])

    w[skill['data']['access']].update(value=dt['access'])

    w[skill['data']['hp']].update(value=dt['hp'])
    w[skill['data']['mp']].update(value=dt['mp'])
    w[skill['data']['str']].update(value=dt['str'])
    w[skill['data']['vit']].update(value=dt['vit'])
    w[skill['data']['agi']].update(value=dt['agi'])
    w[skill['data']['dex']].update(value=dt['dex'])
    w[skill['data']['int']].update(value=dt['int'])

    if dt['kind'] == 0:
        w[skill['data']['active']].update(value=True)
    elif dt['kind'] == 1:
        w[skill['data']['passive']].update(value=True)
    else:
        w[skill['data']['trigger']].update(value=True)

    w[skill['data']['hp_p']].update(value=dt['hp_p'])
    w[skill['data']['mp_p']].update(value=dt['mp_p'])
    w[skill['data']['str_p']].update(value=dt['str_p'])
    w[skill['data']['vit_p']].update(value=dt['vit_p'])
    w[skill['data']['agi_p']].update(value=dt['agi_p'])
    w[skill['data']['dex_p']].update(value=dt['dex_p'])
    w[skill['data']['int_p']].update(value=dt['int_p'])
    if dt['skill']:
        w[skill['children']['list']].update(values=dt['skill'].split(' '))
    else:
        w[skill['children']['list']].update(values=[])
    # button
    w[skill['button']['save']].update(disabled=False)


