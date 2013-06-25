from sys import argv
import re

script, filename = argv

text = open(filename)
filetext = text.read()
text.close()

filetext = re.sub(":","\n",filetext)
filelist = filetext.split("\n")

d = {}

counter = 1
for item in filelist[:-2:2]:
    d[item] = d.get(item,filelist[counter])
    counter += 2

sorted_key =sorted(d.iteritems(), key= lambda x : x[0])

for key,value in sorted_key:
    print "Restaurant '%s' is rated at %r." % (key,int(value))