import os
import json
from readdatamodule import *
import IdentitasPasien
import PesanRuangan
import tampil
from Harga import *
import simpan
import openfile
import view
import DiagnosaPasien
import CetakPembayaran

print('============================================================================')
print('                         Rumah Sakit Mardi Waluyo                           ')
print('                      jl. Soekarno Hatta 276 Lampung                        ')
print('                           Telp : 022-841-999                               ')                     
print('============================================================================')
print()
print("=====================")
print("1. Pasien")
print("2. Staff Rumah Sakit")
print("=====================")
pilih=int(input("Masukkan Pilihan : "))
while pilih != 1 and pilih != 2 :
  pilih = int(input('Masukkan Pilihan : '))
if pilih == 1 :
  L = [] 
  nama = input("Masukkan Kode Pasien Yang Telah Diberikan : ")
  
elif pilih==2 :
  uname =input('username : ')
  password = input('password : ')
  while (uname != "a") or (password != "a") :
    print('username/password salah!')
    uname=input('username : ')
    password=input('password : ')
  else :
    nama = input("Kode Pasien Yang Ingin Dicari : ")
    L = openfile.Buka(nama)

os.system("cls")
pil=tampil.TampilAdmin()
os.system("cls")
while pil != 7 :
  if pil==1:
    L = IdentitasPasien.identitas(L)
    print()
    print("enter untuk kembali ke menu")
    input()
  elif pil==2:
    print()
    HargaKamar(kamar('Harga.txt'))
    print()
    print()
    PesanRuangan.Pesan()
    print()
    print("enter untuk kembali ke menu")
    input()
  elif pil==3:
    L=DiagnosaPasien.Diagnosa(L)
    print()
    print("enter untuk kembali ke menu")
    input()
  elif pil==4:
    simpan.Simpan(L,nama)
    print("Data berhasil di simpan, enter untuk kembali ke menu")
    input()
  elif pil==5 :
    view.viewAll(L)
    print()
    print("enter untuk kembali ke menu")
    input()
  elif pil==6 :
    CetakPembayaran.pembayaran(L)
    input()

  os.system("cls")
  pil=tampil.TampilAdmin()
  os.system("cls")