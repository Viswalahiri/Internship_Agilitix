#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Net Regex href=./(\w|\-)+/(\w|\-)+.>.+</a>
import re
pattern = re.compile("href=\"/(\w|-)+/(\w|-)+\">.+</a>")
all_matches = []
for i, line in enumerate(open('HTML_Source_Code.txt')):
    for match in re.finditer(pattern, line):
        l = match.group()
        to_print = ''
        to_print = ("Link = ""github.com"+l.split('"')[1]).ljust(40) + ("Project Name = "+l.split('"')[1].split('/')[-1]).rjust(40)
        all_matches.append(to_print)
for i in all_matches:
	f = open("Project_Link_RegEx.txt", "a")
	f.write(i)
	f.write("\n")
	f.close()