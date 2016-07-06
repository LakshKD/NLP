# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:13:48 2016

@author: laksh
"""
import csv
import math
#-----------------------------------------#Loading the Model File#-----------------------------# 
print 
print 
print
print "------------------------------------POS TAGGER(IIT BOMBAY)---------------------------------------------"
print "-----------------------------------Author(Lakshya And Arpan)----------------------------#"
print 
print "   Please Enter a Sentence to Assign Part of Speech Tags with full stop at End  "
print
transition = dict()
emission = dict()
possible_tags = dict()
#MY i =1
with open('ModelFile.csv', 'rb') as csvfile:
    modelreader = csv.reader(csvfile, delimiter=' ')
    for row in modelreader:
        str = ', '.join(row)
        w = str.split(",")
        #print w,i
        #i +=1
        possible_tags[w[1]] = 1
        
        if w[0] == "T":
            transition[w[1]+" "+w[2]] = w[len(w)-1]
        else:
            emission[w[1]+" "+w[2]] = w[3]

#print possible_tags
#print transition 
#print emission

#--------------------------------------------#Forward Step#------------------------------------#
line = raw_input()
words = line.split(" ")
l = len(words)
#print words
best_score = dict()
best_edge = dict()
best_score[repr(0)+" "+"<s>"] = float(0)
best_edge[repr(0)+" "+"<s>"] = ""
mini = float(0.0000000475285171102662)  #Min probability of emission for words that are not present in the emission dictionary
for i in range(0,l):
    for prev,k in possible_tags.items():
        for curr,j in possible_tags.items():
            if repr(i)+" "+prev in best_score and prev+" "+curr in transition:
                #print "cvc"
                if curr+" "+words[i] in emission:                
                    score = best_score[repr(i)+" "+prev] -(math.log(float(transition[prev+" "+curr])))-(math.log(float(emission[curr+" "+words[i]])))
                else:
                    #print best_score[repr(i)+" "+prev], transition[prev+" "+curr]
                    score = float(best_score[repr(i)+" "+prev]) -(math.log(float(transition[prev+" "+curr])))-(math.log(float(mini)))
                    
                if repr(i+1)+" "+curr not in best_score or best_score[repr(i+1)+" "+curr] > score:
                    #m = i+1
                    #print "a"
                    best_score[repr(i+1)+" "+curr]  = score
                    best_edge[repr(i+1)+" "+curr] = repr(i)+" "+prev
    #print len(best_edge)


#-------------------------------------------#Backward Step#------------------------------------------#

tags = []
next_edge = best_edge[repr(l)+" "+"."]
while next_edge!= "0 <s>":
    w = next_edge.split(" ")
    position = w[0]
    tag = w[1]
    tags.append(tag)
    next_edge = best_edge[next_edge]
    
#----------------------------------------#POS Tagged Sentence#----------------------------------------#    
tags.reverse()
print tags
    




























'''
l1 = []
l2 = []
l3 = []
l4 = []


for key,value in best_score.items():
    w = key.split(" ")
    if(w[0] == "1"): 
        l1.append([w[1],value])
    elif(w[0] == "2"): 
        l2.append([w[1],value])
    elif(w[0] == "3"): 
        l3.append([w[1],value])
    elif(w[0] == "4"): 
        l4.append([w[1],value])

print maxl1
'''



   
   
