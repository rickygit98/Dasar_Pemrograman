'''
Created on Dec 16, 2020

@author: RICKY
'''
def cek (n):
    
    hasil_cek = True
    if n % 2 == 1 and 1<=n<=49:
        hourglass(n)
        panggil()
    else:
        print("Masukkan bilangan ganjil antara 1 sampai dengan 49")
        panggil()
    
def tanya (kalimat):
    n = int(input(kalimat))
    
    return n
    
def hourglass (n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(n-i)-1):
            print("*",end="")
        print()
    for a in range(n):
        for b in range(n-1-a):
            print(" ",end="")
        for c in range(2*a+1):
            print("*",end="")
        print()
    
def panggil ():
    kalimat = "Masukkan nilai n:"
    n = tanya(kalimat)
    cek(n)

panggil()