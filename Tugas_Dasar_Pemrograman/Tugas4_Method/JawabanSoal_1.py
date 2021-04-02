'''
Created on Dec 15, 2020

@author: RICKY
'''
def tanya (kalimat):
    angka = int(input(kalimat))
    return angka

def segitiga1 (n):
    for a in range(n):
        for b in range(n-1-a):
            print(" ",end="")
        for c in range(2*a+1):
            print("*",end="")
        print()
    print("")

kalimat = "Masukkan nilai n:"
n = tanya(kalimat)

segitiga1(n)