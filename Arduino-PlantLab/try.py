#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-11-04 16:09:04
# @Last Modified by:   Abhi
# @Last Modified time: 2015-11-04 18:17:51


import plotly.plotly as py
from plotly.graph_objs import *
import time

py.sign_in("ScrypticLabs", "d76nf7o1bf")

lightExposureSmall = Scatter(x=[],y=[],stream=dict(token='iwpjagmjiz'))

dataSet = Data([lightExposureSmall])
stream = py.Stream('iwpjagmjiz')
stream.open()
time.sleep(5)

log = input("Enter data point: ")

while(log != "exit"):
	x,y = log.split()
	x,y = float(x), float(y)

	stream.write(dict(x=x,y=y))

	time.sleep(0.08)
	# py.plot(dataSet)

	log = input("Enter data point: ")

stream.close()
