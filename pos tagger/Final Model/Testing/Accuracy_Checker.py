# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:55:35 2016

@author: laksh
"""
from itertools import izip

#f1 = open("Output_TagFile.txt","r")
#f2 = open("TagFile.txt","r")
equal_words = 0
total_words = 0
with open("Output_TagFile.txt") as f1, open("TagFile.txt") as f2:
    for x, y in izip(f1, f2):
        x = x.strip()
        y = y.strip()
        w1 = x.split(" ")
        w2 = y.split(" ")
        for i in range(0,len(w1)):
            if(w1[i]==w2[i]):
                equal_words +=1
            total_words +=1
f1.close()
f2.close()
print  (float(equal_words)/total_words) * 100