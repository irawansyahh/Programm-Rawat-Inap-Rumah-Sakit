import json
def Buka(nama):
	file = open(nama+'.txt','r+')
	return json.load(file)
