'''
Created on Nov 19, 2020

@author: RICKY
'''
#Menanmpilkan n bilangan fibonanci pertama
#1, 1, 2, 3, 5, 8, 13, dst

num = int(input("Masukkan banyak bilangan yang ingin ditampilkan :"))

a = 0
b = 1

if num == 1 :
    print(a,end=" ")
    print(b,end=" ")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range (2,num):
        c = a + b
        a = b
        b = c
        print(c,end=" ")

print("")
#Dengan Menggunakan While

num = int(input("Masukkan banyak bilangan yang ingin ditampilkan :"))
a = 0
b = 1

print(a,end=" ")
print(b,end=" ")

while 2 < num :
    
    c = a + b
    a = b
    b = c
    
    num -= 1
    print(c,end=" ")