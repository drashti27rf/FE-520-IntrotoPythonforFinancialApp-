#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Is Palindrome Number

def is_palindrome(x):
    z = str(x)
    if z == z[::-1]:   # reverse string
        return True 
    return False
    

# Test Question 1
        
print("\nQ1")
q1_test1 = 121
q1_test2 = -121
q1_test3 = 0
q1_answer1 = is_palindrome(q1_test1)
q1_answer2 = is_palindrome(q1_test2)
q1_answer3 = is_palindrome(q1_test3)
print(q1_answer1 )
print("right answer: True")
print("--------------")
print(q1_answer2)
print("right answer: False")
print("--------------")
print(q1_answer3)
print("right answer: True")


# In[2]:


# 2. Dict Practice

def is_anagrams(s, t):
    d1 = {}
    d2 = {}
    # converting both string into lower case
    s = s.lower()
    t = t.lower()
    
    # converting both string into dict 
    
    for i in s:   
        if i in d1:
            d1[i] += 1
        else:
            d1[i] =1
            
    for w in t:
        if w in d2:
            d2[w] += 1
        else:
            d2[w] =1
    
    # sorting dict
    
    x = sorted(d1)
    y = sorted(d2)
    
    # comparing both the dict 
    
    if x == y:
        return True
    return False

print("\nQ2")
q2_test1_s = "anagram"
q2_test1_t = "nagaram"
q2_answer1 =  is_anagrams(q2_test1_s, q2_test1_t)
print(q2_answer1)
print("right answer: True")

print("--------------")
q2_test2_s = "python"
q2_test2_t = "py"
q2_answer2 =  is_anagrams(q2_test2_s, q2_test2_t)
print(q2_answer2)
print("right answer: False")
print("--------------")


# In[3]:


# 3. String Practice

import re 

from collections import Counter

def top_k_words(s, k):
    
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for pun in s:  
        if pun in punctuations:  
            s = s.replace(pun, "") 

    s = re.sub(' +', ' ', s)   # to remove extra spaces
    s = s.strip()              # to remove first and last space in a string 
    s = list(s.split(" "))     # coverting into list    
    
    con = Counter(s)
    
    em = []
    for key, value in con.items(): 
   
        if value >= k: 
            em.append(key)
        x = em[::-1]
    return x
    
    
    
    
    
# test question 3
print("\nQ3")
q3_test1_s = "   i love python, he    love coding python. the course is about python. "
q3_test1_k = 2
q3_answer = top_k_words(q3_test1_s, q3_test1_k)
print(q3_answer)
print("right: answer:")
print("['python', 'love']")



# In[12]:



def gradient_descent(x, y, m, c, epochs, L=0.001):
   
   global m_list
   global c_list
   
   m_list = []
   c_list = []
   
   for _ in range(epochs):
   
       for i in range(len(x)):
           Y_pre = m * x[i][0] + c
           m_list.append(x[i][0] * (Y_pre - y[i]))
           c_list.append(Y_pre - y[i])
       dm = sum(m_list)/len(m_list)
       dc = sum(c_list)/len(c_list)
       m_list = []
       c_list = []

       m = m - L*dm
       c = c - L*dc
   
   return (m,c)
   

print ("\nQ4")

x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
m = 0
c = 0
q4_epochs200 = 200
q4_epochs500 = 500
q4_epochs1000 = 1000
q4_epochs2000 = 2000
q4_epochs3000 = 3000
q4_answer1 = gradient_descent(x,y,m,c,q4_epochs200)
q4_answer2 = gradient_descent(x,y,m,c,q4_epochs500)
q4_answer3 = gradient_descent(x,y,m,c,q4_epochs1000)
q4_answer4 = gradient_descent(x,y,m,c,q4_epochs2000)
q4_answer5 = gradient_descent(x,y,m,c,q4_epochs3000)

print(q4_answer1)
print("right answer:")
print("17.724810647355827, 22.97599012903927")
print("--------------")
print(q4_answer2)
print("right answer:")
print("35.97890301691016, 46.54235227399102")
print("--------------")
print(q4_answer3)
print("right answer:")
print("52.816639894324545, 68.05971340716786")
print("--------------")
print(q4_answer4)
print("right answer:")
print("64.56549666509812, 82.46678636085996")
print("--------------")
print(q4_answer5)
print("right answer:")
print("67.42648874428104, 85.32444456113602")
print("--------------")

