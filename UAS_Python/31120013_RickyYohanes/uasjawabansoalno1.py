'''
Created on Jan 25, 2021

@author: RICKY
'''
class patternH:
    def inputNilai(self,kalimat):
        n = int(input(kalimat))
        return n
    
    def cetakPatternH(self,n):
        for row in range (n):
            for col in range (n):
                if col == 0 or col == n-1 or (row == n//2 and (col>0 and col<n-1)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()