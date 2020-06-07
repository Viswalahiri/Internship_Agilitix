import requests
import json
from pprint import pprint
for i in range(10):
	url = f"https://api.github.com/search/repositories?q=language:Java&topic=REST"
	data = requests.get(url).json()
	f = open("Java_Rest.json", "w")
	with open("Java_Rest.json", "a") as outfile: 
		json.dump(data,outfile)
