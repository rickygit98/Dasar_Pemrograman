'''
Created on Dec 21, 2020

@author: indrabt
'''
from ClassPersegiPanjang import PersegiPanjang

x = PersegiPanjang()
kalimat = "Masukkan nilai panjang = "
p = x.InputNilai(kalimat)
kalimat = "Masukkan nilai lebar = "
l = x.InputNilai(kalimat)
luas = x.HitungLuas(p, l)
x.CetakLuas(luas)