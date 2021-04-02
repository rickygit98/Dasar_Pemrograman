'''
Created on Nov 19, 2020

@author: RICKY
'''

#ProgramIterasi sederhana
#atau penjumlahan sederhana
# 1 + 2 + 3 + ... + n

angka = int(input("Masukkan bilangan Anda:"))

total = 0

for i in range (1,angka+1):
    total = total + i

print("jumlah",angka,"bilangan pertama adalah",total)

#atau dengan menggunakan while

n = int(input("Masukkan bilangan Anda:"))

total = 0
i = 1

while i <= n :
    total = total + i
    i = i + 1
    
print("jumlah",i-1,"bilangan pertama adalah",total)
    