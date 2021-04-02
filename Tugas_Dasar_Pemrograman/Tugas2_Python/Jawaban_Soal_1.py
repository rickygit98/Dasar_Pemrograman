'''
Created on Oct 20, 2020

@author: RICKY
'''
#----FILE JAWABAN SOAL NOMOR 1-------------------------------------------------------------------------- 
#----I.-------------------------------------------------------------------------- 
print("Ini adalah program Python dengan menggunakan perintah print.")
print("")

#----II.-------------------------------------------------------------------------- 
print("Belajar bahasa pemrograman Python itu    menyenangkan dan Mengasyikan.")
print("")

#----III.-------------------------------------------------------------------------- 
num = int(8)

for i in range (num,0,-1):
    print("*"*i)
print("")

#----IV.-------------------------------------------------------------------------- 
num2 = int(5)

for a in range (1,num2+1):
    print("*"*a)
print("")

#----V.-------------------------------------------------------------------------- 
num3=int(5)
for b in range(num3):
    for c in range(num3-b):
        print(" ",end="")
    for d in range(2*b+1):
        print("*",end="")
    print()
print("")

#----VI.-------------------------------------------------------------------------- 
num4=int(5)
for i in range(num4):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(num4-i)-1):
        print("*",end="")
    print()
print("")

#----VII.-------------------------------------------------------------------------- 
   
for n in range(1,10,1):
    print(n,"",end="")
print()
for n in range(2,18,2):
    print(n,"",end="")
print()
for n in range(3,26,3):
    print(n,"",end="")
print()
for n in range(4,34,4):
    print(n,"",end="")
print()
for n in range(5,45,5):
    print(n,"",end="")
print()
    