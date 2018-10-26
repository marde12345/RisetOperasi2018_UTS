import os

def create_table(row,col):
	list2D = []

	for i in range(row):
		list1D =[]
		for j in range(col):
			list1D.append(int(input("Masukkan nilai : ")))
		list2D.append(list1D)
		view_table(row,col,list2D)
		if input("Apakah benar matrix seperti diatas?(y/n) : ") != "y" :
			return create_table(row,col)
	return list2D

def view_table(row,col,list2D):
	os.system('cls')
	for i in range(col):
		print("\t",i,end='\0')
	print()

	for i in list2D:
		print(list2D.index(i),end="\t")
		for j in i:
			print(j,end="\t")
		print()

row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))
Matrix2D = []

print(create_table(row,col))

#os.system('cls')