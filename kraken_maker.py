#!/usr/bin/python2.7
import sys
import os
import uuid

my_id = uuid.uuid1()
kaiju_file = sys.argv[1]
os.popen("./taxa_parser.awk %s > /tmp/names_%s.txt"% (kaiju_file,my_id))

main = {}
secondary = {}
tertiary = {}
main["main"] = []
input_file = open(("/tmp/names_%s.txt" %my_id),"r")
L = []

#Functions needed

def loop(x, y):
    if main[x]:
        for element in main[x]:
            space = y
            print sum(tertiary[element]),"\t", sum(secondary[element]),"\t", sum(secondary[element]),"\t","-\t", "unknow_ID\t", space * "  " + element
            if main[element]:
                space += 1
                loop_2(element, space)

def loop_2(x, y):
    for element in main[x]:
        space = y
        print sum(tertiary[element]),"\t", sum(secondary[element]),"\t", sum(secondary[element]),"\t","-\t", "unknow_ID\t", space * "  " + element
        if main[element]:
            space += 1
            loop(element, space)

def key(where, name):
    if not name in main:
        main[where].append(name)
        main[name] = []

#Creation of the dictionary keys
#Add the classification names, the number of reads and percentage into the right branch (key)
for line in input_file:
    if not line.startswith("-") and not "unclassified\n" in line:
        percent, reads, name = line.strip().split("\t")
        L.append(name.strip())
        if not name in secondary:
            secondary[name] = []
            tertiary[name] = []
        secondary[name].append(int(reads))
        tertiary[name].append(float(percent))
    elif not "unclassified\n" in line:
        element = 1
        for line in L:
            if element == 1:
                truc = line
                key("main",line)
                element += 1
            else:
                key(truc,line)
                truc = line
        L = []
    else:
        percent, reads, name = line.strip().split("\t")
        print percent,"\t",reads,"\t",reads,"\t","U\t0\t",name
        print percent,"\t",reads,"\t",reads,"\t","-\t1\troot"

#The result is a dictionary with a key for each group, classes, .. (the parent branch of the tree) that contains the names of the daughters branches.



#Print the tree. The parent branch (key) is printed. Afterwards, its daughters branches are printed. The daughter branch become a parent branch if it contains daughters branches.
#When there is no more daughters branches, it returns to the previous parent and check for the daughters branches.

#(key root; number of starting space)
loop('main',1)
