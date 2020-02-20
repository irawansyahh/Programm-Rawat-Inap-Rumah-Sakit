import json
def Simpan(L,nama):
	with open(nama+'.txt','w') as file:
		json.dump(L,file)