from sys import argv
import re

script, filename = argv

text = open(filename)
filetext = text.readlines()
text.close()

# filetext = re.sub(":","\n",filetext)
# filelist = filetext.split("\n")

d = {}

counter = 1
for line in filetext:
    name, score = line.strip().split(":")
    # line_components = line.strip()
    # line_components = line_components.split(":")
    # name = line_components[0]
    # score = int(line_components[1])
    d[name] = int(score)
    # d[item] = d.get(item,filelist[counter])
    # counter += 2

sorted_key =sorted(d.iteritems(), key= lambda x : x[0])

for key,value in sorted_key:
    print "Restaurant '%s' is rated at %r." % (key,int(value))