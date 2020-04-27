# -*- coding: utf-8 -*-
from GUI.gui import w
from GUI.key import *


def change(text):
    w[text].update(text_color='red')


def back(tp):
    for v in globals()[tp]['text'].values():
        w[v].update(text_color='black')


