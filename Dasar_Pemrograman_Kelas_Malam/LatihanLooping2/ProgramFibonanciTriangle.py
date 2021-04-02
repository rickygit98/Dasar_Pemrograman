'''
Created on Nov 19, 2020

@author: RICKY
'''
# Bilangan Fibonanci 
# 1,1,2,3,5,8,13,dst

n = int(input('Masukkan bilangan ke-n Fibonnaci : '))

x = 1
y = 1
z = 0

fib = []

for i in range(n+1):
    
    x = y
    y = z
    z = x + y
    
    fib.append(z)
    
    for j in range(i):
        
        print(fib[j], end=" ")
        
    print(" ")