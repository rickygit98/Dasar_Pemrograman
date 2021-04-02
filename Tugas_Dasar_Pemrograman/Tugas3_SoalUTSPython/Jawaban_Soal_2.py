'''
Created on Dec 2, 2020

@author: RICKY
'''

n = 1
tambah0 = 0
tambah3 = 3
tambah5 = 5
prima = []
ctr = 0
a = 2
b = 2
c = 1
d = 0

while not(n >= 3  and n <= 60 and n % 3 == 0):
    n = int(input("Masukkan nilai n antara 3-60 dan n merupakan bilangan kelipatan tiga = "))

for j in range(int(n/3)):
    
    # Baris ke 1 Penjumlahan 3 >>>>> 3 + 6 + 9 + ... + dst
    for i in range(1,n+1):
        if i != n:
            print(tambah3,'+',end=" ")    
        else:
            print(tambah3,'=',end=" ")
        tambah0 += tambah3
        tambah3 += 3
    print(tambah0, end=" ")
    print(" ")
    tambah0 = 0
    tambah3 = 3
    
    # Baris ke 2 Perkalian Prima >>>>> 2 x 3 x 5 x 7 X ... dst
    while len(prima) < n:
        for i in range(1, a+1):
            if b % i == 0:
                ctr += 1
        if ctr == 2:
            prima.append(b)
        b += 1
        ctr = 0
        a += 1
                     
    for i in range(len(prima)):
        c *= prima[i]
        if i!= len(prima)-1:
            print(prima[i],'x',end=" ")
        else:
            print(prima[i],'=',end=" ")
    print(c, end=" "); print(" ")
    c = 1
    
    # Baris ke 3 >>>>> 5 + 10 + 15 + ... dst
    for i in range(2,n+2):
        if i != n+1:
            print(tambah5,'+',end=" ")
        else:
            print(tambah5,'=',end=" ")
        d += tambah5
        tambah5 *= i
    print(d, end=" "); print(" ")
    d = 0
    tambah5 = 5