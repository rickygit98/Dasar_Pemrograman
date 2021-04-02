'''
Created on Dec 15, 2020

@author: RICKY
'''

def cek (n):
    
    hasil_cek = True
    if n % 2 == 0 and 2<=n<=50:
        diamond(n)
        panggil()
    else:
        print("Masukkan bilangan genap antara 2 sampai dengan 50")
        panggil()
    
def tanya (kalimat):
    n = int(input(kalimat))
    
    return n
    
def diamond (n):
    for a in range(n):
        for b in range(n-1-a):
            print(" ",end="")
        for c in range(2*a+1):
            print("*",end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(n-i)-1):
            print("*",end="")
        print()

def panggil ():
    kalimat = "Masukkan nilai n:"
    n = tanya(kalimat)
    cek(n)

panggil()