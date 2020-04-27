# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from GUI.Character.ui import character_ui
from GUI.Skill.ui import skill_ui
from GUI.Eqpt.ui import eqpt_ui
from GUI.Attr.ui import attr_ui
from GUI.Json.ui import json_ui

from GUI.key import table


def ui():
    return [[
        sg.TabGroup(
            [[
                sg.Tab('角色', character_ui(), key=table['character']),
                sg.Tab('属性', attr_ui(), key=table['attr']),
                sg.Tab('技能', skill_ui(), key=table['skill']),
                sg.Tab('装备', eqpt_ui(), key=table['eqpt']),
                sg.Tab('保存', json_ui(), key=table['json'], element_justification='center')
            ]],
            key=table['group'],
            enable_events=True,
            pad=(12, 9)
        )
    ]]







