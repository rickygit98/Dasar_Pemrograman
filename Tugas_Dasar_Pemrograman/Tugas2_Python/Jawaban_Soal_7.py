'''
Created on Oct 20, 2020

@author: RICKY
'''
print("PROGRAM LUAS SEGITIGA YANG DI GENERATE RANDOM")

import random

alas = random.randint(1,9)

tinggi = random.randint(1,9)

luas = 0.5*alas*tinggi

print("Luas Segitiga saat ini = 0.5 x",alas,"x",tinggi,"=",luas)