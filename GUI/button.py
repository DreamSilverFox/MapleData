# -*- coding: utf-8 -*-
from GUI.gui import w
import MyLib.sql as sql
from GUI.change import back
from GUI.key import *
from GUI.refresh import refresh


def save(tp, data):
    sql.row_save(tp, data)
    clear(tp)
    w[globals()[tp]['button']['save']].update(disabled=True)
    refresh(tp)


def new(tp):
    clear(tp)
    w[globals()[tp]['data']['id']].update(value=len(w[globals()[tp]['list']].get_list_values()) + 1)
    w[globals()[tp]['button']['save']].update(disabled=False)


def clear(tp):
    print(globals()[tp]['data'])
    for v in globals()[tp]['data'].values():
        w[v].update(value='')
    back(tp)



