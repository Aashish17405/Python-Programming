import numpy as np
import random
import pyttsx3
a = np.array([[1,2,2],[2,5,4]])
#print(a.shape)
#print(a.dtype)
#print(a[0,1])
#print(a.size)
#print(a.T)

ide=np.identity(3)
#print(ide)

zeros=np.zeros((2,3))
#print(zeros)

b=np.arange(15)
#print(b)

lsapce=np.linspace(1,2,4)
#print(lsapce)

emp=np.empty((1,3))
#print(emp)

emp_like=np.empty_like(emp)
#print(emp_like)

arr=np.arange(16)
#print(arr)
ar2=arr.reshape(2,8)
#print(ar2)
ar3=arr.ravel()
#print(ar3)

x=[[1,2,3],[4,5,6],[7,8,9]]
ar=np.array(x)
#print(ar.sum(axis=1))

one=np.array([1,3,4,634,2])
# print(one.argmax())
# print(one.argmin())
# print(one.argsort())
# for i in one.argsort():
    # print(one[i],end=" ")
# print()
# print(ar.argmax(axis=0))
# print(ar.argmin(axis=1))

"""c="raaraa"
engine=pyttsx3.init()
engine.say(c)
engine.runAndWait()
"""

"""ndim,size,nbytes,itemsize"""
z=np.array([100,100,100] for i in range(0,4))
# print(z)
# y=np.array([[[x for x in range(0,10,2)] for x in range(0,100,5)] for i in range(0,4)])
# print(y)
# print(y.ndim)
# print(y.shape)
# print(y.size)
# print(y.itemsize)
# print(y.nbytes)
y=np.array([[[x for x in range(0,10,2)] for x in range(0,100,5)] for i in range(0,1)])
# print(y)

# m=np.zeros((5,5,5),dtype="float32")
# print(m)

r=np.array([[x for x in range(0,12,2)] for i in range(0,4)])
# print(r)
# print(r.shape)
# print(r.size)
# for i in range(0,4):
#     for j in range(0,6):
#         print(r[i][j],end=" ")
#     print()
# for i in range(2,4):
#     for j in range(2,4):
#         print(r[i][j],end=" ")
#     print()


list=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(list)
# print(list.shape)
# print(list.size)
# print(list.dtype)
# print(list[2][2])
# z=np.zeros((2,5))
# print(z.dtype)
# rng=np.arange(15)
# print(rng)
# lsap=np.linspace(1,10,5)
# print(lsap)
# emp=np.empty((4,2))
# print(emp)


