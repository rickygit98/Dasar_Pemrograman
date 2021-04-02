'''
Created on Nov 23, 2020

@author: RICKY
'''
n = int(input("Masukkan Angka :"))

if (n-1)%2 == 0 and n >= 5:
    for i in range (n):
        if i == 0 or i == n -1 :
            print("* "*n)
        else:
            print("* "+"  "*(n-2)+"*")
            
else:
    print("Angka masukkan angka yang sisa baginya 0")