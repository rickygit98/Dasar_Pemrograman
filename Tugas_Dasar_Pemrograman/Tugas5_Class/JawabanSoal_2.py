'''
Created on Jan 4, 2021

@author: RICKY
'''

class Segitiga:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = float(input(self.kalimat))
        return temp
    
    def HitungLuas(self, a, t):
        self.a = a
        self.t = t
        luas = 0.5*a*t
        return luas
    
    def CetakLuas(self, luas):
        print("Luas Segitiga = ", luas)
        
