# -*- coding: utf-8 -*-
from GUI.gui import *

import GUI.event as e

while True:
    event['c'], event['d'] = w.read()

    # 事件序列
    if event['c'] in (None, 'Cancel'):
        break
    e.e()
w.close()
