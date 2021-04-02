'''
Created on Nov 16, 2020

@author: RICKY
'''

print("Mencetak 1 sampai 10 dengan for")
for i in range(1,11) :
    print(i,end=" ")

print("")
print("Mencetak 1 sampai 10 dengan while")

i = 1

while i < 11:
    print(i, end=" ")
    i = i + 1

print('contoh mencetak angka menggunakan while')
#contoh perulangan tidak pasti dengan while

i = 1
lagi = "y"

while lagi == "y":
    print(i,end = "")
    lagi = input(" Apakah mau mencetak bilangan lagi (y/l):")
    print("")
    i = i+1
    