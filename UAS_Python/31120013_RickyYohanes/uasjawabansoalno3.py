'''
Created on Jan 25, 2021

@author: RICKY
'''
from uasjawabansoalno1 import patternH
from uasjawabansoalno2 import patternW

def menuUtama():     
    print("------PROGRAM CETAK PATTERN--------")
    print("1. Buat Pattern H")
    print("2. Buat Pattern W")
    print("-----------------------------------")
    print()
    nomor = int(input("Masukkan Nomor program yang ingin dijalankan:"))
    print()
    return nomor

cek = "y"
while cek == "y":
    
    nomor = 0
    while not(nomor == 1 or nomor == 2) :
        nomor = menuUtama()
    
    if nomor == 1 :
        count="y"
        while count == "y":
            
            x = patternH()
            
            print("Anda memilih program cetak pattern H")
            print("-----------------------------------")
            kalimat = "Masukkan nilai n antara 5-48 dan n merupakan bilangan ganjil ="
            n = x.inputNilai(kalimat)
            
            while not(n >= 5  and n <= 48 and n % 2 == 1):
                kalimat = "Masukkan nilai n antara 5-48 dan n merupakan bilangan ganjil ="
                n = x.inputNilai(kalimat)
                 
            x.cetakPatternH(n)
            print()
            count = input("Ingin mengulang program lagi?(y/n)")
            print()
            
    elif nomor == 2 :
        count="y"
        while count == "y":
            
            x = patternW()
            
            print("Anda memilih program cetak pattern W")
            print("-----------------------------------")
            kalimat = "Masukkan nilai n antara 5-48 dan n merupakan bilangan ganjil ="
            n = x.inputNilai(kalimat)
            
            while not(n >= 5  and n <= 48 and n % 2 == 1):
                kalimat = "Masukkan nilai n antara 5-48 dan n merupakan bilangan ganjil ="
                n = x.inputNilai(kalimat)
                 
            x.cetakPatternW(n)
            
            print()
            count = input("Ingin mengulang program lagi?(y/n)")
            print(
                )
    else :
        print("Salah!")
    
    cek = input("ingin kembali ke menu?(y/n)")

print("Program diakhiri , Terima kasih!")