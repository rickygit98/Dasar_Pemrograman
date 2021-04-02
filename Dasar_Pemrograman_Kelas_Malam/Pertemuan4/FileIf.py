'''
Created on Nov 2, 2020

@author: RICKY
'''
bil1 = 70
bil2 = 80
bil3 = 90

if bil1 <90 :
    print("nilai bil1 < 90")
    if bil2 < bil3:
        print("nilai bil2 < nilai bil3")

elif bil1 > 90 :
    print("nilai bil1 > 90")
    
if bil1 < bil3 :
    print("nilai bil1 < nilai bil3")
    
    
#Operator Logika "and" dan "or"

if bil1 > 50 and bil1 > 10 :
    print("bil1 nilainya lebih besar dari 10 dan 50")

#Not berfungsi untuk membalik hasil
if not(bil1 > 50 or bil1 < 10) :
    print("bil1 nilainya lebih besar dari 50 tapi lebih kecil dari 10")