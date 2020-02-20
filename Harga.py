def HargaKamar(listkamar):
	print('--------------------LIST BIAYA KAMAR-----------------------\n' + 'Jenis Kamar \t Biaya Kamar ')
	for i in range (len(listkamar)) :
		print('%s \t Rp.%s,00' %(listkamar[i][0],listkamar[i][1]))
