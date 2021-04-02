'''
Created on Jan 6, 2021

@author: RICKY
'''

class Lingkaran:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = float(input(self.kalimat))
        return temp
    
    def HitungLuas(self, r):
        self.r = r
        luas = 3.14*r*r
        return luas
    
    def CetakLuas(self, luas):
        print("Luas Lingkaran = ", luas)
        
