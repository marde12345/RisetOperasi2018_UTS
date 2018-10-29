import os
import numpy as np
import sys

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
		xy = np.argwhere(list2D == np.min(list2D)).tolist()[0]
		x = xy[1]
		y = xy[0]
		
		sub = min(supply[y],demand[x])
		total = total + (list2D[y][x] * sub)
		supply[y] = supply[y] - sub
		demand[x] = demand[x] - sub
		list2D[y][x] = 9999
		
	return total

def vam(list2D,supply,demand):
	ix = 0
	iy = 0
	total = 0
	alist = []
	blist = []
	
	while (sum(supply)>0):
		alist = []
		blist = []
		rl = []
		#alist supply
		for row in list2D:
			ad = sorted(row,key=lambda x: (x is None, x))
			if set(row) != set([None]) and ad[1] != None:
				a1 = ad[0]
				a2 = ad[1]
				alist.append(int(abs(a1-a2)))
			elif set(row) != set([None]) and ad[1] == None:
				alist.append(ad[0])
			else:
				alist.append(0)

		#blist demand
		for i in range(len(demand)):
			da = sorted(listcol(list2D,i),key=lambda x: (x is None, x))
			if set(xx[i] for xx in list2D) != set([None]) and da[1] != None:
				blist.append(abs(da[0]-da[1]))
			elif set(xx[i] for xx in list2D) != set([None]) and da[1] == None:
				blist.append(da[0])
			else:
				blist.append(0)
		
		if (set(alist)==set([0]) and set(blist)==set([0])):
			return
		print("1",alist,set(alist),blist,set(blist))

		if(max(alist)>max(blist)):
			iy = alist.index(max(alist))
			ix = alist.index(min(list2D[iy]))
			print("1",ix,iy)
		else:
			ix = blist.index(max(blist))
			li = listcol(list2D,ix)
			iy = li.index(min(i for i in li if i is not None))
			print("2",ix,iy)

		sub = min(supply[iy],demand[ix])
		total = total + (list2D[iy][ix] * sub)
		supply[iy] = supply[iy] - sub
		demand[ix] = demand[ix] - sub
		if supply[iy] == 0 and demand[ix] == 0:
			for n in range(len(demand)):
				list2D[iy][n] = None
			for n in range(len(supply)):
				list2D[n][ix] = None
		elif supply[iy] == 0:
			for n in range(len(demand)):
				list2D[iy][n] = None
		elif demand[ix] == 0:
			for n in range(len(supply)):
				list2D[n][ix] = None
		print(list2D)

def listcol(list2D,i):
	lo = []
	for row in list2D:
		lo.append(row[i])
	return lo

def get2val(list2D,row,col):
	print("row",sorted(list2D[row])[1])
	print("col",sorted(x[col] for x in list2D)[1])
	print(list2D)

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
#print(lc(Matrix2D,sup,dem))
#print(np.sort(Matrix2D))
#get2val(Matrix2D,1,2)
vam(Matrix2D,sup,dem)



#x = np.argwhere(Matrix2D == np.min(Matrix2D)).tolist()[0] #y,x
#print(x)

#print(add_supply(row,listpabrik))
#print(create_table(row,col))

#os.system('cls')