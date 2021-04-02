'''
Created on Jan 4, 2021

@author: RICKY
'''
from JawabanSoal_1 import JawabanSoalNo1
from JawabanSoal_2 import Segitiga
from JawabanSoal_3 import Lingkaran
from JawabanSoal_4 import Jajarangenjang
from JawabanSoal_5 import KursMataUang
from JawabanSoal_6 import Segitiga2
from JawabanSoal_7 import SegitigaRandom

print("NO1 ------------------------------------------------------------")       
SoalNo1 = JawabanSoalNo1()
SoalNo1.JawabanNo1_1()
print()
SoalNo1.JawabanNo1_2()
print()
SoalNo1.JawabanNo1_3()
print()
SoalNo1.JawabanNo1_4()
print()
SoalNo1.JawabanNo1_5()
print()
SoalNo1.JawabanNo1_6()
print()
SoalNo1.JawabanNo1_7()
print()

print("NO2 ------------------------------------------------------------")
SoalNo2 = Segitiga()
kalimat = "Masukkan nilai alas = "
a = SoalNo2.InputNilai(kalimat)
kalimat = "Masukkan nilai tinggi = "
t = SoalNo2.InputNilai(kalimat)
luas = SoalNo2.HitungLuas(a, t)
SoalNo2.CetakLuas(luas)
print()

print("NO3 ------------------------------------------------------------")
SoalNo3 = Lingkaran()
kalimat = "Masukkan nilai jari-jari(r) = "
r = SoalNo3.InputNilai(kalimat)
luas = SoalNo3.HitungLuas(r)
SoalNo3.CetakLuas(luas)
print()

print("NO4 ------------------------------------------------------------")
SoalNo4 = Jajarangenjang()
kalimat = "Masukkan nilai alas = "
a = SoalNo4.InputNilai(kalimat)
kalimat = "Masukkan nilai tinggi = "
t = SoalNo4.InputNilai(kalimat)
luas = SoalNo4.HitungLuas(a, t)
SoalNo4.CetakLuas(luas)
print()

print("NO5 ------------------------------------------------------------")
SoalNo5 = KursMataUang()
kalimat = "Masukkan nominal dalam IDR :"
rupiah = SoalNo5.InputNominal(kalimat)

usd = SoalNo5.KursUsd(rupiah)
euro = SoalNo5.KursEuro(rupiah)
sg = SoalNo5.KursSg(rupiah)
pound = SoalNo5.KursPound(rupiah)

SoalNo5.CetakKurs(rupiah,usd,euro,sg,pound)
print()

print("NO6 ------------------------------------------------------------")
SoalNo6 = Segitiga2()
kalimat = "Masukkan nilai s1 = "
s1 = SoalNo6.InputNilai(kalimat)
kalimat = "Masukkan nilai s2 = "
s2 = SoalNo6.InputNilai(kalimat)
kalimat = "Masukkan nilai s3 = "
s3 = SoalNo6.InputNilai(kalimat)
T=SoalNo6.HitungT(s1,s2,s3)
luas = SoalNo6.HitungLuas(T,s1,s2,s3)
SoalNo6.CetakLuas(luas)
print()

print("NO7 ------------------------------------------------------------")
SoalNo7 = SegitigaRandom()
luas = SoalNo7.HitungLuas()
SoalNo7.CetakLuas(luas)