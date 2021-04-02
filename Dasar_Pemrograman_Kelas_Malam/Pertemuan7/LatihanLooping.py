'''
Created on Nov 16, 2020

@author: RICKY
'''
# 1.Mencetak bilangan genap sebanyak n buah

n = int(input("Masukkan nilai n genap:"))
for i in range (1,n+1):
    print(i*2 , end=" ")

print(" ")
# 2.Mencetak bilangan ganjil sebanyak n buah

n = int(input("Masukkan nilai n ganjil:"))
for i in range (1,n+1):
    print(i*2 - 1 , end=" ")

print("")

# 3.Mencetak pola bintang
n = 3

for i in range (1,n+1):
    print("*"*i)
print("")

n = 4

for i in range (1,n+1):
    print("*"*i)
print("")