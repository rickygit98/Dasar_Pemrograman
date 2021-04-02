'''
Created on Jan 18, 2021

@author: RICKY
'''
class SelisihMenit:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = int(input(self.kalimat))
        return temp
    
    def HitungSelisihJam(self,j1,j2):
        self.j1 = j1
        self.j2 = j2
        SelisihJam = (j1-j2)*60
        return SelisihJam
    
    def HitungSelisihMenit(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        if m1 < m2:
            SelisihMenit = 60 - m1 + m2
        else :
            SelisihMenit = m1 - m2
        return SelisihMenit
    
    def CetakHasil(self, SelisihJam, SelisihMenit):
        SelisihTotal = SelisihJam + SelisihMenit
        print("Selisih waktu adalah ", SelisihTotal," menit")
