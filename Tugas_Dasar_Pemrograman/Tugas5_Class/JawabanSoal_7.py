'''
Created on Jan 7, 2021

@author: RICKY
'''
import random

class SegitigaRandom:

    def HitungLuas(self):
        a = random.randint(1,9)
        t = random.randint(1,9)
        luas = 0.5*a*t
        return luas
    
    def CetakLuas(self, luas):
        print("Luas Segitiga = ", luas)