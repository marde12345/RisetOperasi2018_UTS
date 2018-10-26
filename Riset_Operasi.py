import os

def create_city(row,col):
	listtujuan = []
	listpabrik = []
	num = 65
	for i in range(col):
		listtujuan.append(num)
		num = num + 1
	for i in range(row):
		listpabrik.append(num)
		num = num + 1
	return listtujuan,listpabrik

def create_table(row,col):
	list2D = []
	listtujuan,listpabrik = create_city(row,col)

	for i in range(row):
		list1D =[]
		for j in range(col):
			list1D.append(int(input("Masukkan nilai : ")))
		list2D.append(list1D)
		view_table(row,col,list2D,listtujuan,listpabrik)
		if input("Apakah benar matrix seperti diatas?(y/n) : ") != "y" :
			return create_table(row,col)
	return list2D

def view_table(row,col,list2D,listtujuan,listpabrik):
	os.system('cls')
	print ("Pb \ Tj\t",end="")
	for i in listtujuan:
		print ( chr(i) ,end="\t")
	print()

	for i in list2D:
		print(chr(listpabrik[list2D.index(i)]),end="\t")
		for j in i:
			print(j,end="\t")
		print()

row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))
Matrix2D = []

print(create_table(row,col))

#os.system('cls')