'''
Created on Jan 4, 2021

@author: RICKY
'''
class JawabanSoalNo1:
    def JawabanNo1_1(self):
        print("Program Python OOP pertama")
    def JawabanNo1_2(self):
        print("Belajar bahasa pemrograman Python dengan menggunakan konsep OOP itu    menyenangkan dan Mengasyikan")
    def JawabanNo1_3(self):
        num = int(8)
        for i in range (num,0,-1):
            print("*"*i)
    def JawabanNo1_4(self):
        num2 = int(5)
        for a in range (1,num2+1):
            print("*"*a)
    def JawabanNo1_5(self):
        num3=int(5)
        for b in range(num3):
            for c in range(num3-b):
                print(" ",end="")
            for d in range(2*b+1):
                print("*",end="")
            print()
    def JawabanNo1_6(self):
        num4=int(5)
        for i in range(num4):
            for j in range(i):
                print(" ",end="")
            for k in range(2*(num4-i)-1):
                print("*",end="")
            print()
    def JawabanNo1_7(self):
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
    