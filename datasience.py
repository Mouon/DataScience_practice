import matplotlib.pyplot as plt
import numpy as np
import random
import time
import pandas as pd

csv_file = 'imdb_clean.csv'
df = pd.read_csv(csv_file)

for index, r in df.iterrows():
    print(r['title'] , r['release_year'] , r['genre'])


# x_values = np.linspace(0,2*np.pi,100)
# y_values = np.tan(x_values)
# a= np.arange(15).reshape(3,5)
# print(a)
# print(a.shape)
# print(a.ndim)

# print(a.dtype.name)

# test_array = [[1,2,3,4],[1,2,3,4]]

# test_matrix = np.array(test_array)
# test_matrix.shape

# print(a.itemsize)

# print(a.size)

# print(type(a))

# 그래프 그리기

# np.array([20,30,40,50])

# A=np.array([20,30,40,50])
# B=np.arange(4)
# C=A-B
# D=B**2
# print(A<35)
# print(A)
# print(B)
# print(C)
# print(D)

###########################################
#ndarray 벡터화 계산(vectorized computation)효과
#############################################

# a=[r for r in range(10000000)]
# b=[r for r in range(10000000)]
# c=[]

# start = time.time()
# for i in range(10000000):
#     c.append(a[i]*b[i])
# end=time.time()

# print("elasped timr =",end-start)

##############################################
# a = np.arange(10000000)
# b = np.arange(10000000)
# start = time.time()
# c = a*b
# end = time.time()
# print("elasped time =", end-start)
###########################################
###########################################


# a= [random.randint(0,1001) for _ in range(10000000)]
# modified_num_list =[1 if n >500 else 0 for n in num_list]
# list_duration = time.time() - start_time
# c=[]
# print(a)
  
# end=time.time()

A = np.array ( [[1,1],
                [0,1]] )
B = np.array( [[2,0],
                [3,4]] )

C = A*B
D = A@ B

X = [1,2,3,4]
Y = [1,0,1,0]
F = np.inner(X,Y)

print(C)
print(D)
print(F)



######################################
# plt.plot(x_values, y_values)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sin Plot')
# plt.legend()
# plt.show()

# data = np.array([1, 2, 3, 4, 5])
# mean = np.mean(data)

# a,b=0,1
# while b<100:
#     print(b)
#     a,b=b,a+b

# a,b=1,2
# print(a,b)
# a,b=b,a
# print(a,b)

# x=1
# while x > 0:
#     x = int(input("Please enter number:"))
# if x <= 0:
#     print ('프로그램을 중단합니다.')
# elif x % 2 == 1:
#     print (x, '홀수입니다.')
# else:
#     print (x, '짝수입니다')


# for i in range(10):
#     print (i, i**2)

# def compute_two(N):
#     sum = 0
#     multiply = 1
#     for k in range(1, N):
#         sum += k
#         multiply *= k
#     return sum, multiply

# a, b = compute_two(11)  
# print(a)
# print(b)

# s = 'hello world'

# world=s+'!'

# print(world)


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

# if __name__=="__main__":
#     origin_list=[ random.randint(1, 1001) for _ in range(10)]
#     print(origin_list)

#     sorted_list = bubble_sort(origin_list)
#     print(sorted_list)



# print(d['a'])
# for key in d:
#     print(key)
# for v in d.values():
#     print(v)

# for k, v in d.items():
#     print(k, v)
# d['d'] = 4
# del d['b']

# s=input()
# print(list(s))
# i=0
# for i in len(s):
#     if(s[i]==)

