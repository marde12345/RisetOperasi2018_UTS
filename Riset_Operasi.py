import os

def add_supply(row,listpabrik):
	list = []
	for i in range(row):
		print ("Masukkan Supply dari Pabrik %s : "%chr(listpabrik[i]))
		list.append(int(input()))
		return list

def add_demand(col,listtujuan):
	list = []
	for i in range(col):
		print ("Masukkan Demand dari Pabrik %s : "%chr(listtujuan[i]))
		list.append(int(input()))
		return list

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
	supply = []
	demand = []
	listtujuan,listpabrik = create_city(row,col)
	for i in range(row):
		list1D =[]
		for j in range(col):
			list1D.append(int(input("Masukkan nilai : ")))
		list2D.append(list1D)
		view_table(row,col,list2D,listtujuan,listpabrik,supply,demand)
		if input("Apakah benar matrix seperti diatas?(y/n) : ") != "y" :
			return create_table(row,col)
	supply = add_supply(row,listpabrik)
	print (supply)
	input()
	view_table(row,col,list2D,listtujuan,listpabrik,supply,demand)
	demand = add_demand(col,listtujuan)
	view_table(row,col,list2D,listtujuan,listpabrik,supply,demand)
	return list2D

def view_table(row,col,list2D,listtujuan,listpabrik,supply,demand):
	os.system('cls')
	print ("Sb \ Tj\t",end="")
	for i in listtujuan:
		print ( chr(i) ,end="\t")
	print("Supply")

	for i in list2D:
		print(chr(listpabrik[list2D.index(i)]),end="\t")
		for j in i:
			print(j,end="\t")
		if len(i) < len(supply) :
			print(supply[list2D.index(i)])
		else:
			print()
	print ("Demand")

row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))
Matrix2D = create_table(row,col)
listtujuan,listpabrik = create_city(row,col)


#print(add_supply(row,listpabrik))
#print(create_table(row,col))

#os.system('cls')