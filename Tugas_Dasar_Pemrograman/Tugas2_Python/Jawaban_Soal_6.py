'''
Created on Oct 20, 2020

@author: RICKY
'''
print("PROGRAM RUMUS KHUSUS")

import math

s1 = int(input("Masukkan Nilai S1 :"))
s2 = int(input("Masukkan Nilai S2 :"))
s3 = int(input("Masukkan Nilai S3 :"))

T=0.5*(s1+s2+s3)

L=math.sqrt(T*(T-s1)*(T-s2)*(T-s3))

print(L)