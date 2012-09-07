#!/usr/bin/env python

import urllib2
import re

srcFile = urllib2.urlopen('http://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/extensions/api/omnibox.json?view=markup&sortby=rev')

myFile = re.compile(r'name')

for line in srcFile.readlines():
    if myFile.findall(line):
        print line,
