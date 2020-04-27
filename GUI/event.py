# -*- coding: utf-8 -*-
from GUI.gui import event
from GUI.key import table

import GUI.refresh as rf
from GUI.refresh import refresh

from GUI.Character.event import character_event
from GUI.Skill.event import skill_event
from GUI.Eqpt.event import eqpt_event
from GUI.Attr.event import attr_event
from GUI.Json.event import json_event


def e():
    # 切换 tab
    if event['c'] == table['group']:
        tp = list(table.keys())[list(table.values()).index(event['d'][table['group']])]
        refresh(tp)
    character_event()
    skill_event()
    eqpt_event()
    attr_event()
    json_event()



