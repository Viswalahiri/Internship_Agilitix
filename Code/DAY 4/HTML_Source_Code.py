#!/usr/bin/env python
# -*- coding: utf-8 -*-
from timeit import default_timer as timer
import requests
for i in range(10):
	start = timer()
	url = f"https://github.com/search?q=Graph"
	page_html = requests.get(url).text.split("\n")
	f = open("HTML_Source_Code.txt", "w", encoding="utf-8")
	for i in page_html:
		f = open("HTML_Source_Code.txt", "a", encoding="utf-8")
		f.write(i)
		f.write("\n")
		f.close()
	import re
	pattern = re.compile("href=\"/\w+/\w+\">(\w+)/(<em>)?\w+(</em>)?(\w+)?</a>")
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

	end = timer()
	print(end-start)