#!/usr/bin/env python3
import numpy as np

## import math for python lists (sqrt, log, exp...)
import math

print("Python list")
alist = [1,2,3]
print(alist)

print("for loop over list")
for item in alist:
  print(item)

print("Append to list")
alist.append(4)
print(alist)

print("Add number(7 in this case) to each element of list using list comprehensions")
clist = [e + 7 for e in alist]
print(clist)

print("Add two lists using list comprehensions")
dlist = [alist[i] + clist[i] for i in range(len(alist))]
print(dlist)

print("Multiply each list item by scalar")
elist = [2*e for e in dlist]
print(elist)


print("Square each list item using comprehensions")
flist = [e**2 for e in elist]
print(flist)

print("Square root (math.sqrt) of each list item")
glist = [math.sqrt(e) for e in flist]
print(glist)

print("math.log2 is same as log(x,2)")
hlist = [math.log2(e) for e in glist]
print(hlist)

print("\n=====================================\n")

print("Numpy array")
aarr = np.array([1,2,3])
print(aarr)

print("for loop over array")
for item in aarr:
  print(item)

print("Arrays are fixed size, so you can't append, so use concatenate")
barr = np.array([4])
carr = np.concatenate((aarr, barr))
print(carr)

print("Add number (7 in this case) to each element of array")
darr = carr + 7
print(darr)

print("Add two arrays")
darr += carr
print(darr)

print("Multiply scalar * array")
earr = 2 * darr
print(earr)

print("Square each element in array **")
farr = earr**2
print(farr)

print("Square root (np.sqrt) all items in array")
garr = np.sqrt(farr)
print(garr)

print("np.log2")
harr = np.log2(garr)
print(harr)
#!/usr/bin/env python3
import numpy as np


### ===========================================================================
### ===========================================================================

## import math for python lists (sqrt, log, exp...)
import math

a = np.array([1,2])
print(a)
b = np.array([3,4])
print(b)
c = a * b
print(c)

print("===================")
print("dot product using for loop. sum of products")
dot = 0
for e,f in zip(a,b):
  dot += e * f
print(dot)

print("dot product using * and np.sum. sum of products")
prod = a * b
sum_of_prod = np.sum(prod)
print(sum_of_prod)

print(f"dotprod = np.dot(a,b) = {np.dot(a,b)}")
print(f"dotprod = a@b = {a@b}")
print(f"dotprod = (a * b).sum() = {(a*b).sum()}")

print("\n========================\n")
amag = np.sqrt( (a*a).sum() )
print(f"amag = np.sqrt((a*a).sum()) = {amag} - this is the norm of the vector")
anorm = np.linalg.norm(a)
print(f"norm = np.linalg.norm(a) = {anorm} = np.sqrt(a@a) = {np.sqrt(a@a)}")

bmag = np.sqrt( (b*b).sum() )
bnorm = np.linalg.norm(b)
print(f"bmag = np.sqrt((b*b).sum()) = {bmag} = np.linalg.norm(b) = {bnorm}")

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(f"cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b) = {cosangle}")

ang_radians = np.arccos(cosangle)
print(f"ang_radians = np.arccos(cosangle) = {ang_radians}")


print("\n=========================")
print("Speed Test - Dot Product in Numpy vs Pure Python")

# from datetime import datetime
#
# a = np.random.randn(100)
# b = np.random.randn(100)
# T = 100000
#
# def dot_python(a,b):
#   result = 0
#   for e,f in zip(a,b):
#     result += e*f
#   return result
#
# def dot_numpy(a,b):
#   result = np.dot(a,b)
#   return result
#
# t1 = datetime.now()
# for i in range(T):
#   dot_python(a,b)
# t2 = datetime.now()
# t_python = t2 - t1
# print(f"dot_python took: {t_python} seconds")
#
# t1 = datetime.now()
# for i in range(T):
#   dot_numpy(a,b)
# t2 = datetime.now()
# t_numpy = t2 - t1
# print(f"dot_numpy took: {t_numpy} seconds")
#
# print(f"numpy dot is faster than pure python by: {t_python/t_numpy}")


print("\n=========================")
print("Matrices - 2d")

list1 = [[1,2],[3,4]]
print(f"python list1 = {list1}")

element = list1[0][1]
print(f"element = list1[0][1] = {element}")

mat1 = np.array([[1,2],[3,4]])
print(f"mat1 = np.array([[1,2],[3,4]]) =\n{mat1}")

element = mat1[0][1]
print(f"element = mat1[0][1] = {element}")

element = mat1[0,1]
print(f"element = mat1[0,1] = {element}")

col = mat1[:,0]
print(f"col = mat1[:,0] = {col}")

row = mat1[0,:]
print(f"row = mat1[0,:] = {row}")

transpose = mat1.T
print(f"transpose = mat1.T = \n{transpose}")

print(f"exp = np.exp(mat1) =\n{np.exp(mat1)}")
print(f"exp = np.exp(list1) = converts python list to numpy array\n{np.exp(list1)}")


A = np.array([[1,2],[3,4]])
print("A = np.array([[1,2],[3,4]]) = {A}")

B = np.array([[1,2,3],[4,5,6]])
print(f"B = np.array([[1,2,3],[4,5,6]]) =\n{B}")

C = A.dot(B)
print(f"C = A.dot(B) = performs matix multiply\n{C}")

det = np.linalg.det(A)
print(f"det = np.linalg.det(A) = {det} determinant of matrix")

Ainv = np.linalg.inv(A)
print(f"Ainv = np.linalg.inv(A) = matrix inverse\n{Ainv}")

identity = A.dot(Ainv)
print(f"identity = A.dot(Ainv) = returns identity matrix\n{identity}") 

tr = A.trace()
print(f"tr = A.trace() = {tr} = np.trace(A) = {np.trace(A)}-- sum of elements on the diagonal")

diag = np.diag(A)
print(f"diag = np.diag(A) = {diag}  -- returns vector")

D = np.diag([1,2,3])
print(f"D = diag([1,2,3]) = return matrix\n{D}")

eig, V = np.linalg.eig(A)
print(f"eig, V = np.linalg.eig(A) = Eigenvalues of A, followed by Eigenvectors\n{eig}\n{V}")


print("\n=========================")
print("Solve Linear Equations")

A = np.array([[1,1],[1.5,4]])
print(f"A = np.array([[1,1],[1.5,4]]) =\n{A}")

b = np.array([2200, 5050])
print(f"b = np.array([2020, 5050])] =\n{b}")

x = np.linalg.inv(A).dot(b)
print(f"x = np.linalg.inv(A).dot(B) = DON'T USE THIS METHOD\n{x}")

X = np.linalg.solve(A,b)
print(f"X = np.linalg.solve(A,b) = USE THIS METHOD TO SOLVE \n{X}")


print("\n=========================")
print("Generating Data")

z = np.zeros((2,8))
print(f"z = np.zeros((2,8)) = \n{z}")

ones = np.ones((5,3))
print(f"ones = np.ones((5,3)) = \n{ones}")

tens = 10 * np.ones((4,4))
print(f"tens = 10 * np.ones((4,4)) = {tens}")

eye = np.eye(5)
print(f"eye = np.eye(5) creates Identity Matrix \n{eye}")


r = np.random.random((2,4))
print(f"r = np.random.random((2,4)) = uniform in range 0 to 1\n{r}")


n = np.random.randn(4,2)
print(f"normal = np.random.randn((4,2)) = normal/gaussian\n{n}")

R = np.random.randn(10000)
print(f"R = np.random.randn(1000) = ")
mean = R.mean()
print(f"mean = R.mean() = {mean} = np.mean(R) = {np.mean(R)}")

R = np.random.randn(1000,3)
mean_col = R.mean(axis=0)
print(f"mean_col = R.mean(axis=0) = calculates mean of each column\n{mean_col}")

mean_of_each_row = R.mean(axis=1)
print(f"mean_of_each_row = R.mean(axis=1) = mean of each row. 1000 means in this case")


variance = R.var()
print(f"variance = R.var() = {variance} = np.var(R) = {np.var(R)}")

std = R.std()
print(f"std = R.std() = {std} = np.std(R) = {np.std(R)} -- sqrt of variance")

Rint = np.random.randint(0,100,size=(2,4))
print(f"Rint = np.random.randint(0,100,size=(2,4)) = \n{Rint}")







