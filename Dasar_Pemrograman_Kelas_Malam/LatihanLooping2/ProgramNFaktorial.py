'''
Created on Nov 19, 2020

@author: RICKY
'''
#Program N! atau N faktorial

while True:
    n = int(input("Masukkan bilangan anda :"))
    
    if n < 0:
        print("bilangan tidak boleh negatif")
    
    faktorial = 1
    i = n
    while i >= 1 :
        print (i,end=" x ")
        faktorial *= i   
        i -= 1
        
    
    print("")    
    print("Hasil faktorial adalah",faktorial)
