import os
import numpy as np

def nwc(list2D,supply,demand):
	total = 0
	x = 0
	y = 0
	k = 0
	sup = supply
	dem = demand
	while(1):
		if (x > len(dem)-1 or y > len(sup)-1):
			break
		if sup[y] < dem[x]:
			total = total + (sup[y] * list2D[y][x])
			dem[x] = dem[x] - sup[y]
			y = y + 1
		elif sup[y] > dem[x]:
			total = total + (dem[x] * list2D[y][x])
			sup[y] = sup[y] - dem[x]
			x = x + 1
		elif sup[y] == dem[x]:
			total = total + (sup[y] * list2D[y][x])
			x = x + 1
			y = y + 1
	return total

def lc(list2D,supply,demand):
	total = 0
	while(sum(supply)>0 and sum(demand)>0):
		print(demand,supply)
		print(list2D)
		xy = np.argwhere(list2D == np.min(list2D)).tolist()[0]
		print(xy)
		x = xy[1]
		y = xy[0]
		
		sub = min(supply[y],demand[x])
		total = total + (list2D[y][x] * sub)
		supply[y] = supply[y] - sub
		demand[x] = demand[x] - sub
		list2D[y][x] = 9999
		
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
sup = add_supply(row,listpabrik)
dem = add_demand(col,listtujuan)
print(dem,sup)

view_table(row,col,Matrix2D,listtujuan,listpabrik,sup,dem)

#a = nwc(Matrix2D,sup,dem)
#print(a)
print("2",dem,sup)
print(lc(Matrix2D,sup,dem))

#x = np.argwhere(Matrix2D == np.min(Matrix2D)).tolist()[0] #y,x
#print(x)

#print(add_supply(row,listpabrik))
#print(create_table(row,col))

#os.system('cls')