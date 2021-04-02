'''
Created on Jan 25, 2021

@author: RICKY
'''
class patternW:
    def inputNilai(self,kalimat):
        n = int(input(kalimat))
        return n
    
    def cetakPatternW(self,n):
        for row in range (n):
            for col in range (n):
                if col == 0 or col == n-1 or col == n//2 or (row == n-1 and (col>0 and col<n-1)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()