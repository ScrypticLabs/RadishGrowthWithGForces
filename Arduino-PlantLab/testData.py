#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2015-10-31 01:37:42
# @Last Modified by:   Abhi
# @Last Modified time: 2015-11-07 01:49:35

# MAX - Largest Radius Samples 	 = 25.5 cm (3)
# MEDIAN - Middle Radius Samples = 15.5 cm (3)
# MIN - Smallest Radius Samples  = 5.5cm   (3)

import plotly.plotly as py 		# To communicate with Plotly's server, sign in with credentials file
import plotly.tools as tls 		# Useful Python/Plotly tools
from plotly.graph_objs import *	# Graph objects to piece together plots
from sensors import *
import numpy as np  			# (*) numpy for math functions and arrays
import time

py.sign_in("ScrypticLabs", "d76nf7o1bf")
tokens = ['iwpjagmjiz',
		  '6ejid18sle',
		  '2jkuzebbi1',
		  'zxm8hwasyg',
		  'tyrlcun2m5',
		  'b2cgqd35o9',
		  'd78trngq8y',
		  '08vjlpvk07',
		  'dlwye45s3a',
		  'm2bioq88ku',
		  'cd2lmtyx7o',
		  '2ptdbgsf5c',
		  'glw7anma5h',
		  'qcbo9hhc6s',
		  '3a60oqzw04',
		  '90vwed277p',
		  'dn06fuqnpa',
		  'oss0lr8uk5',
		  'xw8fbyz8w1',
		  'n7q6iwlg40',
		  'swzsnhsz27',
		  'akxz0awg60',
		  'epc7qql2a0',
		  'vl6xg1b8uk',
		  '7ttimi6opm',
		  'u3yy7exb72',
		  'gqnn4z81md',
		  'dvpeb98x1x']

graphs = {
	"lightMIN" 			: 	 TripleLine("Light Exposure at F-min", tokens[0:3], ("Trial 1", "Trial 2", "Trial 3")),
	"lightMinAVG" 		:	 Line("Average Light Exposure with Minimal Centripetal Force Over Two Weeks", tokens[3:4], "Amount of Light Exposure"),
	"lightMEDIAN" 		:	 TripleLine("Light Exposure at F-median", tokens[4:7], ("Trial 1", "Trial 2", "Trial 3")),
	"lightMedianAVG" 	:	 Line("Average Light Exposure with Median Centripetal Force Over Two Weeks", tokens[7:8], "Amount of Light Exposure"),
	"lightMAX" 			:	 TripleLine("Light Exposure at F-max", tokens[8:11], ("Trial 1", "Trial 2", "Trial 3")),
	"lightMaxAVG" 		:	 Line("Average Light Exposure with Maximal Centripetal Force Over Two Weeks", tokens[11:12], "Amount of Light Exposure"),
	"soilMinAVG"		:	 Line("Average Soil Moisture Levels with Minimal Centripetal Force Over Two Weeks ", tokens[12:13], "Soil Moisture"),
	"soilMedianAVG"		:	 Line("Average Soil Moisture Levels with Median Centripetal Force Over Two Weeks ", tokens[13:14], "Soil Moisture") ,
	"soilMaxAVG"		:	 Line("Average Soil Moisture Levels with Maximal Centripetal Force Over Two Weeks ", tokens[14:15], "Soil Moisture"),
	"tempMinAVG"		:	 Line("Average Temperature Levels with Minimal Centripetal Force Over Two Weeks ", tokens[15:16], "Temperature Levels"),
	"tempMedianAVG"		:	 Line("Average Temperature Levels with Median Centripetal Force Over Two Weeks ", tokens[16:17], "Temperature Levels"),
	"tempMaxAVG"		:	 Line("Average Temperature Levels with Maximal Centripetal Force Over Two Weeks ", tokens[17:18], "Temperature Levels"),
	"overallMIN"		:	 TripleLine("Changes in Environmental Conditions Imposed by Minimal Centripetal Force", tokens[18:21], ("Light Exposure", "Soil Moisture", "Temperature")),
	"overallMEDIAN"		:	 TripleLine("Changes in Environmental Conditions Imposed by Median Centripetal Force", tokens[21:24], ("Light Exposure", "Soil Moisture", "Temperature")),
	"overallMAX"		:	 TripleLine("Changes in Environmental Conditions Imposed by Maximal Centripetal Force", tokens[24:27], ("Light Exposure", "Soil Moisture", "Temperature"))
}

names 	= [	"lightMIN",
			"lightMinAVG",
			"lightMEDIAN",
			"lightMedianAVG",
			"lightMAX",
			"lightMaxAVG",
			"soilMinAVG",
			"soilMedianAVG",
			"soilMaxAVG",
		   	"tempMinAVG",
		   	"tempMedianAVG",
		   	"tempMaxAVG",
		   	"overallMIN",
		   	"overallMEDIAN",
		   	"overallMAX"]
values 	= [
			{"Trial1" : 0,	"Trial2" : 0, "Trial3" : 0},	
			0,
			{"Trial1" : 0,	"Trial2" : 0, "Trial3" : 0},
			0,
			{"Trial1" : 0,	"Trial2" : 0, "Trial3" : 0},
			0,
			0,
			0,
			0,
			0,
			0,
			0,
			{"Light" : 0,	"Soil" : 0, "Temp" : 0},
			{"Light" : 0,	"Soil" : 0, "Temp" : 0},
			{"Light" : 0,	"Soil" : 0, "Temp" : 0}]

i = 0   
k = 5    
N = 2500  

while i<N:
    i += 1   

    if i % 5 == 0:
	    rawData = randomDataInput().split("\t")

	    for value in names:
	    	index = names.index(value)
	    	if value[-3:] != "AVG" and value[:7] != "overall":
	    		values[index]["Trial1"] = float(rawData[0])
	    		values[index]["Trial2"] = float(rawData[1])
	    		values[index]["Trial3"] = float(rawData[2])
	    		del rawData[:3]
	    	elif value == "lightMinAVG":
	    		secondIndex = names.index("lightMIN")
	    		values[index] = (values[secondIndex]["Trial1"]+values[secondIndex]["Trial2"]+values[secondIndex]["Trial3"])/3
	    	elif value == "lightMedianAVG":
	    		secondIndex = names.index("lightMEDIAN")
	    		values[index] = (values[secondIndex]["Trial1"]+values[secondIndex]["Trial2"]+values[secondIndex]["Trial3"])/3
	    	elif value == "lightMaxAVG":
	    		secondIndex = names.index("lightMAX")
	    		values[index] = (values[secondIndex]["Trial1"]+values[secondIndex]["Trial2"]+values[secondIndex]["Trial3"])/3
	    	elif value.split("M")[0] == "overall":
	    		values[index]["Light"] = values[names.index("lightM"+value.split("M")[1].lower()+"AVG")]
	    		values[index]["Soil"] = values[names.index("soilM"+value.split("M")[1].lower()+"AVG")]
	    		values[index]["Temp"] = values[names.index("tempM"+value.split("M")[1].lower()+"AVG")]
	    	else:
	    		values[index] = float(rawData[0])
	    		del rawData[0]
	    
	    for i in range(len(names)):
	    	if names[i][-3:] != "AVG" and names[i][:7] != "overall":
	    		graphs[names[i]].save(values[i]["Trial1"], values[i]["Trial2"], values[i]["Trial3"])
	    	elif names[i][:7] == "overall":
	    		graphs[names[i]].save(values[i]["Light"], values[i]["Soil"], values[i]["Temp"])
	    	else:
	    		graphs[names[i]].save(values[i])

	    time.sleep(2)
    # trial1 = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

for graph in graphs:
	graphs[graph].close()