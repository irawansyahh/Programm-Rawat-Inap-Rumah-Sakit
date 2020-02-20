def Pesan():
	print('============================================================')
	print('                     PEMESANAN RUANG INAP                    ')
	print('============================================================')
	f=open("GolonganKamar.txt", "w")
	fo=open("asuransi.txt","w")
	i,Asuransi=0,input("Apakah anda mempunyai asuransi (iya/tidak) : ")
	if Asuransi==("iya"):
		Asuransi1=input("Asuransi apa yang anda pakai (BPJS/Prudential): ")
		if Asuransi1==("BPJS"):
			Data1='{}'.format("BPJS")
			fo.write(Data1)
			print("Anda Mendapat Ruangan Regular")
			ruangan= "Regular"
			Data='{}'.format(ruangan)
			f.write(Data)
		if Asuransi1==("Prudential"):
			Data1 = '{}'.format("Prudential")
			fo.write(Data1)
			ruangan= input('VVIP/VIP/Regular :')
			Data='{}'.format(ruangan)
			f.write(Data)
	else:
		if Asuransi==("tidak"):
			print("Pilih Ruangan")
			ruangan=input("VVIP/VIP/Regular ? : ")
			Data='{}'.format(ruangan)
			f.write(Data)
			i=i+1
	f.close()
	fo.close()
