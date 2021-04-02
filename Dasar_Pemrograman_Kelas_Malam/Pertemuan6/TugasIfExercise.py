'''
Created on Nov 9, 2020

@author: RICKY
'''
#Program Nilai

while(True):

    nilai = float(input("Masukkan Nilai Anda :"))
    if (0 <= nilai <= 100):
        if (80 <= nilai <= 100):
            print("NIilai",nilai,"Berada pada kategori A")
        elif (74 <= nilai <= 79.9):
            print("NIilai",nilai,"Berada pada kategori AB")
        elif (68 <= nilai <= 73.9):
            print("NIilai",nilai,"Berada pada kategori B")
        elif (62 <= nilai <= 67.9):
            print("NIilai",nilai,"Berada pada kategori BC")
        elif (56 <= nilai <= 61.9):
            print("NIilai",nilai,"Berada pada kategori C")
        elif (41 <= nilai <= 55.9):
            print("NIilai",nilai,"Berada pada kategori D")
        else:
            print("NIilai",nilai,"Berada pada kategori E")
    else:
        print("Nilai yang diinputkan tidak valid")