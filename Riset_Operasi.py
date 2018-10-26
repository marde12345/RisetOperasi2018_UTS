import os

def create_table(row,col):
	list2D = []

	for i in range(row):
		list1D =[]
		for j in range(col):
			list1D.append(int(input()))
		list2D.append(list1D)

	return list2D

row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))
Matrix2D = []

print(create_table(row,col))

#os.system('cls')