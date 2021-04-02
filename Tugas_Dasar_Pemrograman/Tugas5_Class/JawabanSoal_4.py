'''
Created on Jan 6, 2021

@author: RICKY
'''

class Jajarangenjang:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = float(input(self.kalimat))
        return temp
    
    def HitungLuas(self, a, t):
        self.a = a
        self.t = t
        luas = a*t
        return luas
    
    def CetakLuas(self, luas):
        print("Luas Jajarangenjang = ", luas)
        