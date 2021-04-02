'''
Created on Jan 18, 2021

@author: RICKY
'''
from tttjawabansoalno1 import SelisihMenit
from tttjawabansoalno2 import ProgramKasir
#------------------------------ Jawaban Soal no 1 --------------------------------------
print("-----------------------------------Soal No 1---------------------------------------")
SoalNo1 = SelisihMenit()

kalimat = "Masukkan nilai jam ke-1 = "
j1 = SoalNo1.InputNilai(kalimat)

kalimat = "Masukkan nilai menit ke-1 = "
m1 = SoalNo1.InputNilai(kalimat)

kalimat = "Masukkan nilai jam ke-2 = "
j2 = SoalNo1.InputNilai(kalimat)

kalimat = "Masukkan nilai menit ke-2 = "
while j2 >= j1:
    print("jam ke-2 lebih besar daripada jam ke-1")
    j2 = int(input("Masukkan jam-2:"))

m2 = SoalNo1.InputNilai(kalimat)

SelisihJam = SoalNo1.HitungSelisihJam(j1, j2)
SelisihMenit = SoalNo1.HitungSelisihMenit(m1, m2)

SoalNo1.CetakHasil(SelisihJam, SelisihMenit)

#--------------------------------- Jawaban Soal no 2 -----------------------------------

print("-----------------------------------Soal No 2---------------------------------------")
SoalNo2 = ProgramKasir()

kalimat = "Masukkan nomor nota:"
nomor_nota = SoalNo2.InputNilai(kalimat)
kalimat = "Masukkan Kode barang:"
kode_barang = SoalNo2.InputNilai(kalimat)
kalimat = 'masukan nama barang : '
nama_barang = SoalNo2.InputNilai(kalimat)
kalimat = 'masukan harga barang: '
harga_satuan = SoalNo2.InputNilai(kalimat)
kalimat = 'masukan jumlah barang yang anda beli: '
jumlah_beli = SoalNo2.InputNilai(kalimat)

total = SoalNo2.HitungHarga(harga_satuan, jumlah_beli)

diskon = SoalNo2.diskon(total)

grandTotal = SoalNo2.grandTotal(total,diskon)

print("------------------------- Struk Belanja Anda ----------------------")

SoalNo2.CetakHasil(nomor_nota,kode_barang,nama_barang,harga_satuan,jumlah_beli,total,grandTotal,diskon)