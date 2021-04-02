'''
Created on Oct 20, 2020

@author: RICKY
'''
print("PROGRAM KURS MATA UANG")
#1US$ = 9.375IDR = 10.435 Euro = 7000SG$ = 17.000

rupiah = int(input("Masukkan nominal dalam IDR :"))

usd = rupiah/9375
euro = rupiah/10435
sg = rupiah/7000
pound = rupiah/17000
    
print(rupiah,"rupiah sama dengan",usd,"US$")
print(rupiah,"rupiah sama dengan",euro,"Euro")
print(rupiah,"rupiah sama dengan",sg,"SG$")
print(rupiah,"rupiah sama dengan",pound,"Pounds Inggris")