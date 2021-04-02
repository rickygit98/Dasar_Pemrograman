'''
Created on Jan 6, 2021

@author: RICKY
'''
import math

class Segitiga2:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = float(input(self.kalimat))
        return temp
    
    def HitungT(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        T = 0.5*(s1+s2+s3)
        return T

    def HitungLuas(self,T,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.T=T
        luas = math.sqrt(T*(T-s1)*(T-s2)*(T-s3))
        return luas
    
    def CetakLuas(self, luas):
        print("Luas Segitiga = ", luas)
        