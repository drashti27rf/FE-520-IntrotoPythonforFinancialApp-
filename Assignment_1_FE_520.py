#!/usr/bin/env python
# coding: utf-8

# # 1. Print 

# In[5]:


# 1. Define a string variable, and print it.

a = "Stevens Institute of Technology"
print(a)

# 2. Define a string (I’m a student), print it.

b = "I'm a Student"
print(b)


# 3. Defind a string: (How do you think of this course? Describe your feeling of this course) print it in multiple line.

c = """ 
This Course contains basic of python.
Professor has amazing understanding
and he teaches so well.
I am very much looking forward to this course.
"""
print(c)


# # 2. Operator

# In[14]:


# Define a = 100, b = 9,

a = 100
b = 9

# 1.
c = a + b
print(c)

# 2. quotient
print(a//b)

# 3. integer part
print(a/b)

# 4. reminder part
print(a%b)

# 5. a to the power of b 
print(a**b)

# 6. a unequal to b 
print(a!=b)

# 7. a greater than b 
print(a>b)


# # 3. List Practice 

# In[43]:


# 1. Define list

List_A = [ 1, 7, 5.7, "D", "Spiderman", 700.100, "NY"]
print(List_A)

# 2. Use of extend and append 

List_A.append("mango") # adding element in list
print(List_A)

List_B = [ 3, "orange", 7.77]
print(List_B)

List_A.extend(List_B) # joing two list 
print(List_A)

# 3. Insert and Delet 
List_A.insert(1, "FE520")
print(List_A)

List_A.pop(1)
print(List_A)

# 4. return and delet last element 

print(List_A[-1])
List_A.pop(-1)
print(List_A)

# 5. new list and slicing

List_C = ["NY", "Stevens", "FE520", 53, 27.97]
print(List_C)

print(List_A[2:])

# 6. Double size

print((List_C) *2)

# 7. reverse list 

print(List_C[::-1])


# # 4. Practice Dictionary

# In[45]:


A = [ 1, 2, 3, 2, 1, 7]

count = {}

for i in A:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)


# # 5. Loop Practice

# In[62]:


A = [1, 2, 3, 4, 5, 6]

total_num = 0
count = 0

for i in A:
    total_num = total_num + i 
    a = len(A)
    count = total_num / a 
    
print(count)


# # 6. Loop Practice: Gradient Decent

# In[88]:


import numpy as np 

m = 0
c = 0
L = 0.001 # learning rate 
ite = 200 # number of iterations 

X = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
Y = [[109.85], [155.72], [137.66], [76.17], [139.75], [162.6], [151.77]]

X = np.array(X)
Y = np.array(Y)
M_list = []
C_list = []

for _ in range(200):
    for i in range(len(X)):
        Y_pre = m * X[i][0] + c 
        M_list.append(X[i][0] * (Y_pre - Y[i][0]))
        C_list.append(Y_pre - Y[i][0])
    dm = sum(M_list)/len(M_list)
    dc = sum(C_list)/len(C_list)
    M_list = []
    C_list = []
    
    m = m - L*dm
    c = c - L*dc
    
print(m,c)

