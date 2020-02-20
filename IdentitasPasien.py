def identitas(L) :
	print('============================================================================')
	print('                          Identitas Pasien                                  ')                       
	print('============================================================================')
	print("Nama : ",end="")
	nama=input()
	print("umur : ",end="")
	umur=int(input())
	i,Jenis = 0,input("Jenis Kelamin(perempuan/laki-laki) : ")
	while Jenis != ("perempuan") and Jenis != ("laki-laki") and Jenis !=("Perempuan") and Jenis !=("Laki-laki") :
		print("Masukan dengan (perempuan/laki-laki)")
		Jenis = input("Jenis Kelamin(perempuan/laki-laki) : ")
		i=i+1
	print("No. KTP : ",end="")
	KTP=int(input())
	print('Alamat : ',end="")
	Alamat=input()

	record=[nama,umur,Jenis,KTP,Alamat]
	L.append(record)
	return L

