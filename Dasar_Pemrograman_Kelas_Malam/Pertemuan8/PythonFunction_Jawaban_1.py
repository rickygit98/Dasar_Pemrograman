'''
Created on Dec 7, 2020

@author: RICKY
'''

def InputNilai (kalimat):
    temp = float(input(kalimat))
    return temp

def HitungLuasSegitiga(alas,tinggi):
    luas = 0.5 * alas *tinggi
    return luas
    
def CetakLuasSegitiga(Luas):
    print ("Luas Segitiga =",end=" ")
    print(luas)
    

kalimat = "Masukkan Nilai Alas = "
alas = InputNilai(kalimat)
kalimat = "Masukkan Nilai Tinggi = "
tinggi = InputNilai(kalimat)

luas = HitungLuasSegitiga(alas,tinggi)
CetakLuasSegitiga(luas)