# -*- coding: utf-8 -*-
__author__ = "Viswalahiri Swamy Hejeebu"
__credits__ = ["Viswalahiri Swamy Hejeebu"]
__email__ = 'viswalahiriswamyh@gmail.com'
__status__ = 'Dev'
#Net Regex "href=\"/(\w|\-)+/(\w|\-)+\">.+</a>"
import re
import sys
def main(p):
    pattern = re.compile(str(p[0]))
    for i, line in enumerate(open('HTML_Source_Code.txt')):
        for match in re.finditer(pattern, line):
            l = match.group()
            to_print = ''
            to_print = ("Link = ""github.com"+l.split('"')[1]).ljust(40) + ("Project Name = "+l.split('"')[1].split('/')[-1]).rjust(40)
            print(to_print)
if __name__ == "__main__":
	main(sys.argv[1:]) 