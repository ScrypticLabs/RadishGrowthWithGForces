#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-10-31 01:19:28
# @Last Modified by:   Abhi
# @Last Modified time: 2015-11-07 01:49:18

# MAX - Largest Radius Samples 	 = 25.5 cm (3)
# MEDIAN - Middle Radius Samples = 15.5 cm (3)
# MIN - Smallest Radius Samples  = 5.5cm   (3)

import plotly.plotly as py 		# To communicate with Plotly's server, sign in with credentials file
import plotly.tools as tls 		# Useful Python/Plotly tools
from plotly.graph_objs import *	# Graph objects to piece together plots
import datetime					# Import module keep track and format current time
import time
import numpy as np  			# (*) numpy for math functions and arrays

class TripleLine():
	def __init__(self, title, token, traces, markers = False, maxpoints = 500, clear = False):
		self.currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		self.clear = clear
		self.title = title
		self.graph1 = Scatter(
    		x=[],
    		y=[],
    		name=traces[0],
    		type="scatter",
    		mode='lines+markers' if markers else 'lines',
    		stream=Stream(
    			token=token[0],    		# (!) link stream id to 'token' key
    			maxpoints=maxpoints     # (!) keep a max of 80 pts on screen
				)	   
		)
		self.graph2 = Scatter(
    		x=[],
    		y=[],
    		name=traces[1],
    		type="scatter",
    		mode='lines+markers' if markers else 'lines',
    		stream=Stream(
    			token=token[1], 		 # (!) link stream id to 'token' key
    			maxpoints=maxpoints      # (!) keep a max of 80 pts on screen
				)	   
		)
		self.graph3 = Scatter(
    		x=[],
    		y=[],
    		name=traces[2],
    		type="scatter",
    		mode='lines+markers' if markers else 'lines',
    		stream=Stream(
    			token=token[2],    		 # (!) link stream id to 'token' key
    			maxpoints=maxpoints      # (!) keep a max of 80 pts on screen
				)	   
		)

		self.layout = Layout(title=title, xaxis=dict(title="Time (UTC)"), yaxis=dict(title="Magnitude"))

		self.stream1 = py.Stream(token[0])
		self.stream2 = py.Stream(token[1])
		self.stream3 = py.Stream(token[2])
		
		self.streamData = Data([self.graph1, self.graph2, self.graph3])
		# Make a figure object
		self.fig = Figure(data=self.streamData, layout=self.layout)
		# (@) Send fig to Plotly, initialize streaming plot, open new tab
		# unique_url = py.plot(self.fig, filename=self.title)

		self.stream1.open()
		self.stream2.open()
		self.stream3.open()
		
		self.data = {
			"Trial1" : [],
			"Trial2" : [],
			"Trial3" : []
		}
		
		self.values = {
			"Trial1" : (0,0),
			"Trial2" : (0,0),
			"Trial3" : (0,0)
		}

		# time.sleep(2)	# delay of 5 seconds before plotting

	def save(self, trial1, trial2, trial3):
		self.refreshTime()
		self.values["Trial1"] = (self.currentTime, trial1)
		self.values["Trial2"] = (self.currentTime, trial2)
		self.values["Trial3"] = (self.currentTime, trial3)
		for trial in self.data:
			self.data[trial].append(self.values[trial])
		self.update()
		time.sleep(0.08)

	def getGraph(self):
		return self.graph

	def update(self):
		"""Plots recent values to the web"""
		print("Plotting " + str(str(self.values["Trial1"][1]) + " at " + str(self.values["Trial1"][0]) + "\n"))
		if self.clear:
			self.stream1.write(dict(x=[], y=[]))
			self.stream2.write(dict(x=[], y=[]))
			self.stream3.write(dict(x=[], y=[]))
		else:
			self.stream1.write(dict(x=self.values["Trial1"][0], y=self.values["Trial1"][1]))#, trace=Bar)
			self.stream2.write(dict(x=self.values["Trial2"][0], y=self.values["Trial2"][1]))
			self.stream3.write(dict(x=self.values["Trial3"][0], y=self.values["Trial3"][1]))
			
	def refreshTime(self):
		self.currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

	def close(self):
		self.stream1.close()
		self.stream2.close()
		self.stream3.close()

class Line():
	def __init__(self, title, token, yaxis, markers = True, maxpoints = 500, clear = False):
		self.currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		self.clear = clear
		self.title = title
		self.graph = Scatter(
    		x=[],
    		y=[],
    		type="scatter",
    		mode='lines+markers' if markers else 'lines',
    		stream=Stream(
    			token=token[0],    		# (!) link stream id to 'token' key
    			maxpoints=maxpoints     # (!) keep a max of 80 pts on screen
				)	   
		)

		self.layout = Layout(title=title, xaxis=dict(title="Time (UTC)"), yaxis=dict(title=yaxis))

		self.stream = py.Stream(token[0])
		
		self.streamData = Data([self.graph])	
		# Make a figure object
		self.fig = Figure(data=self.streamData, layout=self.layout)
		# (@) Send fig to Plotly, initialize streaming plot, open new tab
		# unique_url = py.plot(self.fig, filename=self.title)

		self.stream.open()

		self.data = {
			"Trials" : [],
		}
		
		self.values = {
			"Trial" : (0,0),
		}

		# time.sleep(2)	# delay of 5 seconds before plotting

	def save(self, value):
		self.refreshTime()
		self.values["Trial"] = (self.currentTime, value)
		self.data["Trials"].append(self.values["Trial"])
		self.update()
		time.sleep(0.08)

	def getGraph(self):
		return self.graph

	def update(self):
		"""Plots recent values to the web"""
		print("Plotting " + str(str(self.values["Trial"][1]) + " at " + str(self.values["Trial"][0]) + "\n"))
		if self.clear:
			self.stream.write(dict(x=[], y=[]))
		else:
			self.stream.write(dict(x=self.values["Trial"][0], y=self.values["Trial"][1]))

	def refreshTime(self):
		self.currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

	def close(self):
		self.stream.close()

def randomDataInput():
	values = []
	output = ""
	for i in range(1,16):
		val = (np.cos(5*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]
		# values.append(i)
		values.append(val)
		output += str(val)+"\t"
	return output