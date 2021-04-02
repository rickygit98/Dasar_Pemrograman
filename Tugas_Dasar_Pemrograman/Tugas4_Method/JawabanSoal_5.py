'''
Created on Dec 16, 2020

@author: RICKY
'''

def cek (n):
    
    hasil_cek = True
    
    if n % 2 == 1 and n>=5:
        jajargenjang(n)
        panggil()
    else:
        print("Masukkan bilangan ganjil yang lebih besar daripada 5")
        panggil()
    
def tanya (kalimat):
    n = int(input(kalimat))
    
    return n
    
def jajargenjang (n):
    
    m = 1
    c = (((n - 1) * 2)-3)
    p = c
    
    for i in range(n):
        for j in range(n,i,-1):
            print(" ",end="")
        for g in range(1):
            print("*",end="")
        for y in range(i):
            if (i >= 1 and i<n-1):
                print(" "*m,end="")
                m += 2
                break
            else:
                print(" *" * int(n-1),end="")
                break
        for l in range(1):
            if i == 0:
                print(" *" * int(n-1),end="")
            if (i >= 1 and i<n-1):
                print('*',end="")
        for k in range(1):
            if (i >= 1 and i<n-1):
                print(" " * p,end="")
                p -= 2
        for z in range(1):
            if (i >= 1 and i<n-1):
                print("*",end="")
        print()
    
def panggil ():
    kalimat = "Masukkan nilai n:"
    n = tanya(kalimat)
    cek(n)

panggil()