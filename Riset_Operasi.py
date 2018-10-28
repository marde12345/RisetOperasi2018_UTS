import os

def nwc(list2D,supply,demand):
	total = 0
	x = 0
	y = 0
	k = 0
	while(1):
		if (x > len(demand)-1 or y > len(supply)-1):
			break
		if supply[y] < demand[x]:
			total = total + (supply[y] * list2D[y][x])
			demand[x] = demand[x] - supply[y]
			y = y + 1
		elif supply[y] > demand[x]:
			total = total + (demand[x] * list2D[y][x])
			supply[y] = supply[y] - demand[x]
			x = x + 1
		elif supply[y] == demand[x]:
			total = total + (supply[y] * list2D[y][x])
			x = x + 1
			y = y + 1
	return total

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
		if row <= len(supply) :
			print(supply[list2D.index(i)])
		else:
			print()
	print ("Demand",end="\t")
	for i in demand:
		print(i,end="\t")
	print()

row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))
listtujuan,listpabrik = create_city(row,col)
Matrix2D = create_table(row,col)
supply = add_supply(row,listpabrik)
demand = add_demand(col,listtujuan)

s1 = sum(supply)
d1 = sum(demand)

view_table(row,col,Matrix2D,listtujuan,listpabrik,supply,demand)

nwc(Matrix2D,supply,demand)

#print(add_supply(row,listpabrik))
#print(create_table(row,col))

#os.system('cls')