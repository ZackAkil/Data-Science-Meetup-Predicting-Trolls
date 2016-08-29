# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:29:38 2016

@author: zackakil
"""
import pandas as pa
from PrimeText import PrimeText

pt = PrimeText()
ytData = pa.read_csv("utube.csv",encoding ='ISO-8859-1')
comments = ytData['comment'][:30]


pt.cleanData(comments)
pt.assembleDictionary()
#
pt.indexDictionary()
pt.indexComments()

