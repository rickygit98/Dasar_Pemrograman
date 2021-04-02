'''
Created on Jan 18, 2021

@author: RICKY
'''
'''
Created on Jan 18, 2021

@author: RICKY
'''

class ProgramKasir:
    def InputNilai(self, kalimat):
        self.kalimat = kalimat
        temp = input(self.kalimat)
        return temp

    def HitungHarga(self,harga_satuan,jumlah_beli):
        total = int(harga_satuan) * int(jumlah_beli)
        return total
    
    def diskon(self,total):
        if total < 10000:
            diskon = total * (0/100)
        elif 10000 <= total < 20000 :
            diskon = total * (10/100)
        elif 20000 <= total < 30000 :
            diskon = total * (15/100)
        elif total >= 30000 :
            diskon = total * (18/100)
        
        return diskon
    
    def grandTotal (self,total,diskon):
        grandTotal = total - diskon
        return grandTotal
    
    def CetakHasil(self,nomor_nota,kode_barang,nama_barang,harga_satuan,jumlah_beli,total,grandTotal,diskon):
        print("Nota Nomor :",nomor_nota)
        print("Kode Barang :",kode_barang)
        print("Barang :",nama_barang)
        print("Harga per Pcs :",harga_satuan)
        print("Quantity :",jumlah_beli)
        print("SubTotal :",total)
        
        if grandTotal<10000:
            print("diskon : 0 %")
        elif 10000 <= total < 20000 :
            print("diskon : 10% ---",diskon)
        elif 20000 <= total < 30000 :
            print("diskon : 15% ---",diskon)
        elif total >= 30000 :
            print("diskon : 18% ---",diskon)
            
        print("GrandTotal : ",grandTotal)                 