import requests
import json
from pprint import pprint
# Gets user information
url1 = f"https://api.github.com/users?"
data = requests.get(url).json()
user_list = []
for i in data:
	user_list.append(i['login'])
for i in user_list:
	url = "https://api.github.com/users/{}/repos".format(i)
	data = requests.get(url).json()
	with open("User_Repos.json", "a") as outfile: 
		json.dump(data,outfile)

# Gets repos related to REST written in Java
url2 = f"https://api.github.com/search/repositories?q=language:Java&topic=REST"
data = requests.get(url).json()
f = open("Java_Rest.json", "w")
with open("Java_Rest.json", "a") as outfile: 
	json.dump(data,outfile)
