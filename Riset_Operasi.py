import os

Matrix2D = []
row = int(input("masukkan baris : "))
col = int(input("masukkan kolom : "))

for i in range(row):
	Matrix1D =[]
	for j in range(col):
		Matrix1D.append(int(input()))
	Matrix2D.append(Matrix1D)

print(Matrix2D)

for i in Matrix2D:
	for j in i:
		print(j,end=" ")
	print()

#os.system('cls')