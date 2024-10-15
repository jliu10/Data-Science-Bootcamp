"""
Numpy Questions

1. Define two custom numpy arrays, say A and B. Generate two new numpy
arrays by stacking A and B vertically and horizontally.
2. Find common elements between A and B. [Hint : Intersection of two sets]
3. Extract all numbers from A which are within a specific range. eg
between 5 and 10. [Hint: np.where() might be useful or boolean masks]
4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5
and sepallength (1st column) < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

Pandas Questions
5. From df filter the 'Manufacturer', 'Model' and 'Type' for every
20th row starting from 1st (row 0).
```
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```
6. Replace missing values in Min.Price and Max.Price columns with
their respective mean.
```
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
```
7. How to get the rows of a dataframe with row sum > 100?
```
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
"""

import numpy as np
import pandas as pd

#### 1 #########################################################################
A = np.array([[1,2,3,4,5,6]])
B = np.array([[0,2,4,8,16,32]])
print("A: " + str(A))
print("B: " + str(B))

vAB = np.vstack((A,B))
hAB = np.hstack((A,B))
print("vAB: " + str(vAB))
print("hAB: " + str(hAB))

#### 2 #########################################################################
commonAB = np.intersect1d(A,B)
print("commonAB: " + str(commonAB))

#### 3 #########################################################################
rangedA = A[np.where((A >= 5) & (A <= 10))]
print("rangedA: " + str(rangedA))

#### 4 #########################################################################
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt("iris.data.txt", delimiter=',', dtype='float', usecols=[0,1,2,3])
print("iris_2d:")
print(iris_2d)

soln4 = iris_2d[np.where((iris_2d[:,2] > 1.5) & (iris_2d[:,0] < 5.0))]
print("soln4:")
print(soln4)

#### 5 #########################################################################
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df)

soln5 = df[["Manufacturer","Model","Type"]][::20]
print(soln5)

#### 6 #########################################################################

soln6 = df
meanMinPrice = soln6["Min.Price"].mean()
meanMaxPrice = soln6["Max.Price"].mean()
print(soln6["Min.Price"].mean())
print(soln6["Max.Price"].mean())
print(soln6.info())

soln6["Min.Price"].fillna(meanMinPrice, inplace=True)
soln6["Max.Price"].fillna(meanMaxPrice, inplace=True)
print(soln6.info())

#### 7 #########################################################################

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
soln7 = df
print(soln7)
print(soln7.sum(axis=1))
soln7 = soln7.where(soln7.sum(axis=1) > 100).dropna()
print(soln7)