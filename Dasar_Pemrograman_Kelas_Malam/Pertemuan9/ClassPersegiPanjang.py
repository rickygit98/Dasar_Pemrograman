'''
Created on Dec 21, 2020

@author: indrabt
'''
class PersegiPanjang:
    def InputNilai(self, kalimat):
        n = int(input(kalimat))
        return n
    
    def HitungLuas(self, p, l):
        luas = p * l
        return luas
    
    def CetakLuas(self, luas):
        print("Luas = ", luas)