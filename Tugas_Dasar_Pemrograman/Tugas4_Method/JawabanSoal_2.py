'''
Created on Dec 15, 2020

@author: RICKY
'''

def tanya (kalimat):
    angka = int(input(kalimat))
    return angka

def segitiga2 (n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(n-i)-1):
            print("*",end="")
        print()
    print("")

kalimat = "Masukkan nilai n:"
n = tanya(kalimat)

segitiga2(n)