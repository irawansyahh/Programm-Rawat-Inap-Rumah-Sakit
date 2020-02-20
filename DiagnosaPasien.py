def Diagnosa(L) :
	print('============================================================')
	print('                     PEMESANAN RUANG INAP                   ')
	print('============================================================')
	print('Dokter Yang Tersedia:\n'+'=======================\n'+
  		'1. Dokter Umum\n'+'2. Dokter Spesialis Penyakit Dalam\n'+ '3. Dokter Spesial Mata\n' +'4. Dokter spesialis Anak\n'+
  		'=======================\n')
	pilihan_user=int(input("Dokter Yang Dipilih : "))
	if pilihan_user==1 :
		x = "dr. Supradi"
	if pilihan_user==2 :
		x = "dr. Amira Zalikha, Sp.PD"
	if pilihan_user==3 :
		x ='dr. Andi Arsyil, Sp.M'
	if pilihan_user==4 :
		x='dr. Mia Ariani, Sp.A'
	
	print('Dokter yang Menangani Anda : ',x)
	keluhan=input('Keluhan yang Dirasakan : ')
	record=x,keluhan
	L.append(record)
	return L


	
