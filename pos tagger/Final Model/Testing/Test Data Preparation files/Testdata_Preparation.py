# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:05:40 2016

@author: laksh
"""

f1 = open("Sentencefile.txt","a")
f2 = open("TagFile.txt","a")
with open("cn19.txt") as f:
    for l in f:
        if(l!='\n'):
            l = l.lstrip()
            l = l.rstrip()
            wt = l.split(" ")
            for w in wt:
                t = w.split("/")
                word = t[0]
                tag = t[1]
                f1.write(word+' ')
                #if tag!='.':
                f2.write(tag+' ')
            f1.write("\n")
            f2.write("\n")

f1.close()
f2.close()