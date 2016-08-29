# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:29:38 2016

@author: zackakil
"""
import pandas as pa
import numpy as np
from PrimeText import PrimeText
import matplotlib.pyplot as plt

pt = PrimeText()
ytData = pa.read_csv("utube.csv",encoding ='ISO-8859-1')
comments = ytData['comment']


pt.cleanData(comments)
pt.assembleDictionary()
#
pt.indexDictionary()
pt.indexComments()

keyText = []
keyCount = []
for key, value in pt.indexedDictionary.iteritems():
    c = pt.countInRecords([key])
    keyText.append(key)
    keyCount.append(c)
    
s1 = pa.Series(keyCount,index=keyText)

sortedS1  = s1.sort_values(ascending= False)[:100]

sortedS1.plot.bar()
    