#!/usr/bin/env python

import urllib2
import re

srcFile = urllib2.urlopen('http://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/extensions/api/?sortby=rev&sortdir=down#dirlist').read()

myFile = open("apiPage.html", "w")

for lines in srcFile:
    myFile.write(lines)
