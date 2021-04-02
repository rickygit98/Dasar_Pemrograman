'''
Created on Dec 7, 2020

@author: RICKY
'''
import math

def Inputkalimat (kalimat):
    temp = float(input(kalimat))
    return temp

# Dapatkan nilai T
def HitungNilaiT(s1,s2,s3):
    NilaiT = 0.5*(s1+s2+s3)
    return NilaiT

# Hitung Luas Segitiga :
def HitungLuasSegitiga(t,s1,s2,s3):
    LuasSegitiga = math.sqrt(t*((t-s1)*(t-s2)*(t-s3)))
    return LuasSegitiga

# Cetak Luas Segitiga :
def CetakLuasSegitiga(luas):
    print ("Luas Segitiga =",end=" ")
    print(luas)
    

kalimat = "Masukkan Nilai s1 = "
s1 = Inputkalimat(kalimat)
kalimat = "Masukkan Nilai s2 = "
s2 = Inputkalimat(kalimat)
kalimat = "Masukkan Nilai s3 = "
s3 = Inputkalimat(kalimat)

t = HitungNilaiT(s1,s2,s3)

luas = HitungLuasSegitiga(t, s1, s2, s3)

CetakLuasSegitiga(luas)