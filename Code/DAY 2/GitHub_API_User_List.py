import requests
from pprint import pprint
url = f"https://api.github.com/users?"
data = requests.get(url).json()
for i in data:
	f = open("User_List.txt", "a")
	f.write(i['login'])
	f.write("\n")
	f.close()
