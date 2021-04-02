'''
Created on Nov 30, 2020

@author: RICKY
'''
print("Soal nomor 1 , pola kotak")

ulang = True

while(ulang):
    cek = bool()        # Nilai nya bakal False
    
    while not(cek):     # Nilai nya dibalik jadi True
        
        n = int(input("Masukkan nilai n : "))
        
        if (n>=5) and ((n-1) % 2 == 0) :
            for i in range(n):
                for j in range(n):
                    if i == 0 or i == n-1 or j == 0 or j == n-1:
                        print("*", end=" ")
                    elif j == int(n/2) and i == int(n/2):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print(" ")

        else :
            print("Masukkan bialngan ganjil yang sama atau lebih besar dari 5")