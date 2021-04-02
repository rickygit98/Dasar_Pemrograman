'''
Created on Nov 23, 2020

@author: RICKY
'''
n = int(input("masukkan bilangan:"))

if 3 < n < 60 and n % 3 == 0 :
    
    for i in range (1, n+1):
        print(3*i,end="+")

