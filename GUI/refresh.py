# -*- coding: utf-8 -*-
import MyLib.sql as sql

from GUI.gui import w
from GUI.key import *


def refresh(tp):
    if tp == 'json':
        return 0
    if tp == 'attr':
        ls = sql.list_read_attr(tp)
        w[globals()[tp]['list']].update(values=ls)
        _attr()
        return 0
    ls = sql.list_read(tp)
    w[globals()[tp]['list']].update(values=ls)
    if tp == 'skill':
        _skill()
    if tp == 'eqpt':
        _eqpt()
    print(ls)


def _skill():
    ls = sql.list_read('skill')
    w[globals()['skill']['children']['choose']].update(values=ls, value='')


def _eqpt():
    ls = sql.list_read('skill')
    w[globals()['eqpt']['skill']['choose']].update(values=ls, value='')
    w[globals()['eqpt']['slot']['choose']].update(values=ls, value='')


def _attr():
    ls = sql.character_read_attr()
    w[globals()['attr']['data']['code']].update(values=ls, value='')
    ls2 = sql.list_read('skill')
    w[globals()['attr']['skill']['choose']].update(values=ls2, value='')
    ls3 = sql.list_read('eqpt')
    w[globals()['attr']['data']['head']].update(values=ls3, value='')
    w[globals()['attr']['data']['body']].update(values=ls3, value='')
    w[globals()['attr']['data']['r_hand']].update(values=ls3, value='')
    w[globals()['attr']['data']['l_hand']].update(values=ls3, value='')
    w[globals()['attr']['data']['log']].update(values=ls3, value='')
    w[globals()['attr']['data']['foot']].update(values=ls3, value='')
    w[globals()['attr']['data']['jew1']].update(values=ls3, value='')
    w[globals()['attr']['data']['jew2']].update(values=ls3, value='')
    w[globals()['attr']['data']['jew3']].update(values=ls3, value='')


