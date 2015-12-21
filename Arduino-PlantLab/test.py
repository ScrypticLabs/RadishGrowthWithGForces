#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-10-30 23:46:43
# @Last Modified by:   Abhi
# @Last Modified time: 2015-10-31 01:38:02

import serial  # Arduino to Computer Communications Library
import plotly  # Real time graphing of Values on the Web


ser = serial.Serial('/dev/tty.HC-06-DevB', 9600)

while True:
	a = ser.readline()
	print(a)

