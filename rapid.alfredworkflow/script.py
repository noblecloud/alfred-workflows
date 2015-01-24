#!/bin/python

import subprocess, urllib, sys, os

inputURL='http://imgur.com/download/JRznZSu'
confRAW = open("conf","r")
conf = confRAW.readlines()
confRAW.close()
for line in conf:
	if "location" in line:
		location = line.split(':')
		location = (location[1])
	else:
		location = '/Downloads'
		

resp = urllib.urlopen(inputURL)
resp.getcode()
finalURL = resp.url

# Get user home
home = os.getenv("HOME")
print home + locationd

p = subprocess.Popen(["axel", '-a', '-v', '-o', home + location, finalURL], stdout=subprocess.PIPE)
output = p.communicate()[0]
print(output)