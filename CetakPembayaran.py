from read import *
L=[["Regular",850000],["VIP",1200000],["VVIP",2000000]]
def pembayaran(c):
	d=(readfile("GolonganKamar.txt"))
	e=(readfile("asuransi.txt"))
	if d == "VIP" :
		biaya=L[1][1]
	elif d == "VVIP" :
		biaya=L[2][1]
	elif d == "Regular" :
		biaya=L[0][1]
	Lama=int(input("Lama Di Rawat Di Rumah Sakit (Hari) : "))
	tanggal=input("Tanggal Cetak Bukti Pembayaran (ex:21 Oktober 2017) : ")
	print()
	print("======================================================")
	print("                  BUKTI PEMBAYARAN                    ")
	print("======================================================")
	print('Nama Pasien   : ',end="")
	print(c[0][0])
	print('Jenis Kelamin : ',end="")
	print(c[0][2])
	print('Nama Dokter   : ',end="")
	print(c[1][0])
	print("")
	Biaya1=Lama*biaya
	konsultasi=300000
	total = Biaya1+konsultasi
	if e == "Prudential" :
		Biaya1 = biaya-500000
		ket=" Pengurangan Biaya Sebesar Rp 500000,00\n"+"\tBagi Pengguna Asuransi Prudential"
	elif e == "BPJS" :
		Biaya1 = Biaya1
		total=total-total
		ket='Bebas Biaya Bagi Pengguna BPJS'
	elif e == "" :
		Biaya1=Biaya1
		ket="-"
	print("Rincian pembayaran")
	print()
	print("	Biaya Kamar              ","Rp   ",Biaya1,",00")
	print("	Konsultasi Dokter        ","Rp   ",konsultasi,",00")
	print("	                           ___________________+")
	print("	                          Rp   ",total,",00  ")
	print()
	print("Ket : ", ket)

	print()
	carabayar=input('Cara pembayaran(Cash/Debit) : ')
	while carabayar != "Debit" and carabayar != "debit" and carabayar != "Cash" and carabayar != "cash" :
		carabayar=input("Cara pembayaran(Cash/Debit) : ")
	if (carabayar == "Debit") or (carabayar== "debit") :
		print()
		print("------------LUNAS---------------")
	elif (carabayar=="Cash") or (carabayar == "cash") :
		a=int(input("Masukkan Besar Biaya yang Dibayarkan : "))
		while (a < total) :
			print("Biaya Yang Anda Masukkan Kurang!")
			a=int(input("Masukkan Besar Biaya yang Dibayarkan : "))
		else :
			kembalian=a-total
			print("Kembalian Anda : ",end="")
			print("Rp.",kembalian,",00")
			print()
			print("------------LUNAS---------------")
	print()
	print()
	print("                           Lampung,",tanggal,"         ")





	
	














