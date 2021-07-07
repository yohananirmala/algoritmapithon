import os
import sys
import datetime
from time import process_time_ns

x = datetime.datetime.now()

gol = [1,2,3]
gaji_p = [2500000,4500000,6500000]
os.system('cls')
print("="*70)
print(" "*10,"PERHITUNGAN GAJI KARYAWAN CV.LOGOS")
print("="*70)
print(" "*10,"!!! DIWAJIBKAN MENGISI DATA DIBAWAH !!!")
nama =         input("NAMA                 " + " "*10)
golongan = int(input("golongan             " + " "*10))
jk =           input("JENIS KELAMIN (L/P)  " + " "*10)
sk =           input("STATUS KAWIN         " + " "*10)
ja =       int(input("JUMLAH ANAK          " + " "*10))
os.system('cls')
if golongan == 1:
	i = 0
	tun = 0.01
elif golongan == 2:
	i = 1
	tun = 0.03
elif golongan == 3:
	i = 2
	tun = 0.05
if jk.upper() == "L" and sk.lower() == 'kawin':
	tun_istri = gaji_p[i]*tun
else : tun_istri = 0
if sk.lower() == 'kawin' and ja > 0:
	tun_anak = gaji_p[i] * 0.02
else: tun_anak = 0
gaji_brt = gaji_p[i] + tun_anak + tun_istri
biaya_jbtn = gaji_brt * 0.005
iuran_p = 15000
iuran_o = 3500
gaji_net = gaji_brt - biaya_jbtn - iuran_o - iuran_p
print(" ")

print(" ")
print(" "*10,"SLIP GAJI")
print(" "*10,"Tanggal : ",x.strftime("%x"))
print(" ")
print(" ")
print("Nama            "," "*10,nama)
print("Golongan        "," "*10,golongan)
print("Jenis Kelamin   "," "*10,jk)
print("Status Kawin    "," "*10,sk)
print("Gaji Pokok      "," "*10,gaji_p[i])
print("Tunjangan Istri "," "*10,tun_istri)
print("Tunjangan Anak  "," "*10,tun_anak)
print(">>Gaji Bruto    "," "*10,gaji_brt)
print("-"*15)
print("Biaya Jabatan   "," "*10,biaya_jbtn)
print("Iuran Pensiun   "," "*10,iuran_p)
print("Iuran Organisasi"," "*10,iuran_o)
print(">>Gaji Netto    "," "*10,gaji_net)