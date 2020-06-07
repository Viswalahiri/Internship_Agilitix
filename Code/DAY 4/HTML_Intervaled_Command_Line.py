#!/usr/bin/env python
# -*- coding: utf-8 -*-
from timeit import default_timer as timer
__author__ = "Viswalahiri Swamy Hejeebu"
__credits__ = ["Viswalahiri Swamy Hejeebu"]
__email__ = 'viswalahiriswamyh@gmail.com'
__status__ = 'Dev'
#Net Regex href=./(\w|\-)+/(\w|\-)+.>.+</a>
import re
import sys
import requests
def main(p):
	int1 = int(p[1])
	int2 = int(p[2])
	print(f"Projects for {p[0]}")
	f = open("HTML_Source_Code.txt", "w", encoding="utf-8")
	for i in range(int1//10,(int2//10)):
		url = f"https://github.com/search?p={i+1}&q={p[0]}"
		
		page_html = requests.get(url).text.split("\n")
		for i in page_html:
			f = open("HTML_Source_Code.txt", "a", encoding="utf-8")
			f.write(i)
			f.write("\n")
			f.close()
		pattern = re.compile("href=./(\w|\-)+/(\w|\-)+.>.+</a>")
	for i, line in enumerate(open('HTML_Source_Code.txt')):
		for match in re.finditer(pattern, line):
			l = match.group()
			to_print = ''
			to_print = ("Link = ""github.com"+l.split('"')[1]).ljust(40) + ("Project Name = "+l.split('"')[1].split('/')[-1]).rjust(40)
			print(to_print)
if __name__ == "__main__":
	main(sys.argv[1:])