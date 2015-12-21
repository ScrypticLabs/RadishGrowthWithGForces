#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-10-31 01:46:45
# @Last Modified by:   Abhi
# @Last Modified time: 2015-10-31 02:22:10

# Plots a Scatter Plot
# import plotly.plotly as py
# from plotly.graph_objs import Scatter

# trace0 = Scatter(
# 	x=[1, 2, 3, 4],
#     y=[10, 15, 13, 17]
# )
# trace1 = Scatter(
#     x=[11, 12, 13, 14],
#     y=[16, 5, 11, 9]
# )
# data = [trace0, trace1]

# unique_url = py.plot(data, filename = 'basic-line')

# Real Time Data Plotting
import plotly.plotly as py
from plotly.graph_objs import *
from random import *
# auto sign-in with credentials or use py.sign_in()
trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(token='iwpjagmjiz')
    )
data = Data([trace1])
py.plot(data)
s = py.Stream('iwpjagmjiz')
s.open()
counter = 0
total = 0
while(counter < 100):
	print("Plotting...")
	total += 5
	s.write(dict(x=total, y=randint(0,100)))
	counter += 0.25
s.close()