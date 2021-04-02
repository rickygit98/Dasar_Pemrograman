'''
Created on Jan 6, 2021

@author: RICKY
'''

class KursMataUang:
    def InputNominal(self, kalimat):
        self.kalimat = kalimat
        temp = float(input(self.kalimat))
        return temp
    
    def KursUsd(self, rupiah):
        self.rupiah = rupiah
        usd = rupiah/9375
        return usd
    
    def KursEuro(self, rupiah):
        self.rupiah = rupiah
        euro = rupiah/10435
        return euro
    
    def KursSg(self, rupiah):
        self.rupiah = rupiah
        sg = rupiah/7000
        return sg
    
    def KursPound(self, rupiah):
        self.rupiah = rupiah
        pound = rupiah/17000
        return pound
    
    def CetakKurs(self,rupiah,usd,euro,sg,pound):                   
        print(rupiah,"rupiah sama dengan",usd,"US$")
        print(rupiah,"rupiah sama dengan",euro,"Euro")
        print(rupiah,"rupiah sama dengan",sg,"SG$")
        print(rupiah,"rupiah sama dengan",pound,"Pounds Inggris")