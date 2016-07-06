# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:26:24 2016

@author: laksh
"""

#Corpus preparation in the below code

import csv

'''
f1 = open("tagged_corpus.txt","a")
with open("cp24.txt") as f:
    for l in f:
        if(l!='\n'):
            l = l.lstrip()
            l = l.rstrip()
            #l = '<s>'+l
            #print "\n"
            f1.write(l+'\n')
        
'''

#Training Code
f1 = open("tagged_corpus.txt","r")
f2 = open("test.txt","r")
emit = dict()
transition = dict()
context = dict()
context["<s>"] = 0
for l in f1:
    l = l.rstrip()
    #print l
    previous = "<s>"
    context[previous] +=1
    wordtags = l.split(" ")   #splitting the line on space
    #print wordtags
    for wordtag in wordtags:
        wt = wordtag.split("/")   #Splitting the Words in / to get word and tag
        #print wt
        if previous+" "+wt[1] in transition:        
            transition[previous+" "+wt[1]] +=1
        else:
            transition[previous+" "+wt[1]] =1
        if wt[1] in context:
            context[wt[1]] +=1
        else:
            context[wt[1]] =1
        if wt[1]+" "+wt[0] in emit:
            emit[wt[1]+" "+wt[0]] +=1
        else:
            emit[wt[1]+" "+wt[0]] =1
        
        previous = wt[1]
    if previous+"." in transition:    
        transition[previous+" "+"."]+=1
    else:
        transition[previous+" "+"."]=1 

#Transition Probabilities
'''
f3 = open("NewModelFile.txt","w")
#l = []
for key,value in transition.items():
    l = []    
    k = key.split(" ")
    #print k,i
    #print k,value,context[k[0]]
    l.extend(("T",k[0],k[1],float(value)/context[k[0]]))
    
    f3.write(l)
    f3.write("\n")
    #print str(l),i
    
f3.close() 
 

#Emission Probabilities
f4 = open("NewModelFile.txt","a")
for key,value in emit.items():
    l = []
    k = key.split(" ")
    #print k
    #print k,value,context[k[0]]
    l.extend(("E",k[0],k[1],float(value)/context[k[0]]))
    f4.write(l)
    f4.write("\n")
f4.close()
'''

with open('ModelFile.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Type','Context','Word','Probabilities'])
    for key,value in transition.items():
        k = key.split(" ")
        writer.writerow(["T",k[0],k[1],float(value)/context[k[0]]])
    for key,value in emit.items():
        k = key.split(" ")
        writer.writerow(["E",k[0],k[1],float(value)/context[k[0]]])    


with open('ModelFile.csv', "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Type','Context','Word','Probabilities'])
    writer.writerow(["T",".",".","."])





'''
print "\n"
print transition
print "\n"
print context
print "\n"
print emit    
'''


'''
print len(train_text)


for line in train_text:
    #if(line!=" "):
    print line
        #break

print (train_text)
'''