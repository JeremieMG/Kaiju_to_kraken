#!/usr/bin/python2.7
import sys
import os
import uuid
import re
from optparse import OptionParser

#Options
parser = OptionParser()
parser.add_option("-i", dest="kaiju", help='Input kaiju.out file')
parser.add_option("-t", dest="nodes", help='nodes.dmp file')
parser.add_option("-n", dest="names", help='names.dmp file')
parser.add_option("-f", dest="id", help='id_nodes file')
(options, args) = parser.parse_args()
kaiju_input = options.kaiju
nodes_file = options.nodes
names_file = options.names
id_nodes = options.id

#First step, creatin of the id's dictionary for the taxonomic IDs
id_name = open(names_file, "r")
id_dico = {}
name_dico = {}

for line in id_name:
    taxid, u_1, taxname, u_2, space, u_3, description, u_4 = line.strip().split("\t")
    if description == "scientific name":
        id_dico[taxname] = taxid
        name_dico[taxid] = taxname

#Creating summary File
os.popen("kaijuReport -t %s -n %s -i %s -r species -l superkingdom,phylum,order,class,family,genus,species -o kaiju.out.summary"% (nodes_file,names_file, kaiju_input))

#
my_id = uuid.uuid1()
os.popen("./taxa_parser.awk kaiju.out.summary > /tmp/names_%s.txt"% (my_id))

main = {}
secondary = {}
tertiary = {}
quaternary = {}
main["main"] = []
input_file = open(("/tmp/names_%s.txt" %my_id),"r")
L = []
tax_names = ["U","D","P","C","O","F","G","S","-"]
#Functions needed

def loop(x, y):
    if main[x]:
        for element in main[x]:
            space = y
            rank_display = ''.join((quaternary[element]))
            test = rank_display
            print str(sum(tertiary[element])) + "\t" + str(sum(secondary[element])) + "\t" + str(sum(secondary[element])) + "\t" + rank_display.rstrip() + "\t" + id_dico[element] + "\t" + space * "  " + element
            if main[element]:
                space += 1
                loop_2(element, space)

def loop_2(x, y):
    for element in main[x]:
        space = y
        rank_display = ''.join(quaternary[element])
        print str(sum(tertiary[element])) + "\t" + str(sum(secondary[element])) + "\t" + str(sum(secondary[element])) + "\t" + rank_display.rstrip() + "\t" + id_dico[element] + "\t" + space * "  " + element
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
        percent, reads, rank, name = line.strip().split("\t")
        L.append(name.strip())
        if not name in secondary:
            secondary[name] = []
            tertiary[name] = []
            quaternary[name] = []
        secondary[name].append(int(reads))
        tertiary[name].append(float(percent))
        if quaternary[name] == []:
            quaternary[name].append(tax_names[int(rank)])
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
        reverse = 100 - float(percent)
	print str(percent) + "\t" + str(reads) + "\t" + str(reads) + "\tU\t0\t" + name
#        print str(reverse) + "\t" + str(reads) + "\t" + str(reads) + "\t-\t1\troot"

#The result is a dictionary with a key for each group, classes, .. (the parent branch of the tree) that contains the names of the daughters branches.

#print root
a = []
for i in secondary:
	a.append(sum(secondary[i]))

print str(reverse) + "\t" + str(sum(a)) + "\t" + str(sum(a)) + "\t-\t1\troot"

#Print the tree. The parent branch (key) is printed. Afterwards, its daughters branches are printed. The daughter branch become a parent branch if it contains daughters branches.
#When there is no more daughters branches, it returns to the previous parent and check for the daughters branches.

#(key root; number of starting space)
loop('main',1)

#Print the viruses classification

def virus_loop(x, y):
    if virus[x]:
        for element in virus[x]:
            space = y
            id = str(id_dico[element])
	    rank_display = ''.join(d_4[id])
            print str((float(sum(virus_count[element]))/ float(sum(secondary["Viruses"])))*float(sum(tertiary["Viruses"]))) + "\t" + str(sum(virus_count[element])) + "\t" + str(sum(virus_count[element])) + "\t" + rank_display.rstrip() + "\t" + id_dico[element] + "\t" + space * "  " + element
            if virus[element]:
                space += 1
		virus_loop_2(element, space)

def virus_loop_2(x, y):
    if virus[x]:
        for element in virus[x]:
            space = y
	    id = str(id_dico[element])
            rank_display = ''.join(d_4[id])
            print str((float(sum(virus_count[element]))/ float(sum(secondary["Viruses"])))*float(sum(tertiary["Viruses"]))) + "\t" + str(sum(virus_count[element])) + "\t" + str(sum(virus_count[element])) + "\t" + rank_display.rstrip() + "\t" + id_dico[element] + "\t" + space * "  " + element
            if virus[element]:
                space += 1
		virus_loop(element, space)

def virus_key(where, name):
    if not name in virus:
        virus[where].append(name)
        virus[name] = []

virus = {}
virus["virus"] = []
virus_count = {}
virus_list = []
kaiju_report = open(kaiju_input, "r")
nodes = open(id_nodes, "r")

d_2 = {}
d_3 = {}
d_4 = {}

for line in nodes:
	current, ref, rank = line.strip().split("\t")
	d_3[current] = ref
	d_2[current] = rank

for rank in d_2:
	if d_2[rank] == "species":
		number = 7
	elif d_2[rank] == "genus":
		number = 6
	elif d_2[rank] == "family":
		number = 5
	elif d_2[rank] == "order":
		number = 4
	elif d_2[rank] == "class":
		number = 3
	elif d_2[rank] == "phylum":
		number = 2
	else:
		number = 8
	if not rank in d_4:
		d_4[rank] = []
		d_4[rank].append(tax_names[number])

L = []
for line in kaiju_report:
	rstate, rname, ncbi = line.strip().split("\t")
	if ncbi != "0" and re.search('virus', name_dico[ncbi]):
		space = 1
		while ncbi != "10239":
			L.append(name_dico[ncbi])
			ncbi = d_3[ncbi]
		L.reverse()
		element = 1
		for i in L:
			if element == 1:
				truc = i
				virus_key("virus",i)
				element = 0
			else:
				virus_key(truc,i)
				truc = i
			L = []
			if not i in virus_count:
				virus_count[i] = []
			virus_count[i].append(int("1"))

virus_loop('virus',2)

