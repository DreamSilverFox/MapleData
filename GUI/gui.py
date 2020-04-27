# -*- coding: utf-8 -*-
import PySimpleGUI as sg

import GUI.ui as ui

# 窗口样式
sg.theme('BluePurple')  # Add a touch of color

# 页面
w = sg.Window('Maple Data', ui.ui(), size=(1024, 768))
# 事件
event = {'c': '', 'd': {}}


