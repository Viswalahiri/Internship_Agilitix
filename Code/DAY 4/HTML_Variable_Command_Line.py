#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Net Regex href=./(\w|\-)+/(\w|\-)+.>.+</a>

#Net Regex for star ratings
import re
import sys
import requests

def parser(a):
	a = str(a)
	t = a[-1]
	if(t == 'k'):
		val = a[0:-1]
		val = int(val)*1000
		return int(val)
	return int(a)
def main(p):
	url = f"https://github.com/search?q={p[0]}"
	print(f"First 10 Projects for {p[0]}")
	page_html = requests.get(url).text.split("\n")
	f = open("HTML_Source_Code.txt", "w", encoding="utf-8")
	for i in page_html:
		f = open("HTML_Source_Code.txt", "a", encoding="utf-8")
		f.write(i)
		f.write("\n")
		f.close()
	pattern = re.compile("href=./(\w|\-)+/(\w|\-)+.>.+</a>")
	all_projects = []
	for i, line in enumerate(open('HTML_Source_Code.txt')):
		for match in re.finditer(pattern, line):
			l = match.group()
			to_print = ''
			to_print = ("Link = ""github.com"+l.split('"')[1]).ljust(40) + ("Project Name = "+l.split('"')[1].split('/')[-1]).rjust(40)
			all_projects.append(to_print)
	fhandle = open('HTML_Source_Code.txt')
	inp = fhandle.read()
	star_gazers = []
	reglist = re.findall(r"</path></svg>(\s)+(\w+|\.+)+(\s)+</a>", inp)
	for i in reglist:
		star_gazers.append(parser(i[1]))
	final_projects_list = [x for _,x in sorted(zip(star_gazers,all_projects))] 
	for i in final_projects_list:
		print(i)


if __name__ == "__main__":
	main(sys.argv[1:])