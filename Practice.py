

# -*- coding: utf-8 -*-
import math
import sys
import unicodedata
import random
from random import randrange
a=[int(x)for x in input().split()]
for i in range(len(a)):
    if a[i]%2!=0:
        a[i]=a[i]**2
print(*a,sep=',')


l = []
s=0
while True:
    line = input().split()
    print(line)
    if line:
        l.append(line)
    else:
        break
for i in range(0,len(l)):
    x=l[i]
    x=x.split()
   
    for j in range(0,len(x)):
        if x[j]=='D':
            s+=int(x[j+1])
        elif x[j]=='W':
            s-=int(x[j+1])
print(s)

def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                #print(matrix[i-1][j])
                #print( matrix[i][j-1])
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    cs = matrix[-1][-1]
    return len(cs), cs
print(lcs("", "bayxb"))

ar=[str(x)for x in input().split(',')]
c=0
sm=0
print(ar)
for i in range(0,len(ar)):
    l=0
    u=0
    n=0
    sp=0    
    x=ar[i]
    if len(x)>=6 and len(x) <=12:
        for j in range(0,len(x)):
            if x[j].isalpha():
                if x[j].islower():
                    l=1
                if x[j].isupper():
                    u=1
            elif x[j].isdigit():
                n=1
            else:
                sp=1
        
        if l==1 and u==1 and n==1 and sp==1:
                print(x)
l=[]
while True:
    line = input()
    if line:
        l.append(line)
    else:
        break
l.sort()
x=[]
for i in range(0,len(l)):
    x.append(tuple(l[i].split(',')))
print(x)

class mine:
    def my_gen(x,y):
        for i in range(x,y+1):
            if i%7==0:
                yield i
for item in mine.my_gen(0,100):
    print(item)


x1=0
y1=0
l1=[]
x2=0
y2=0
while True:
    line = input()
    if line:
        l1.append(line)
    else:
        break
for j in range(0,len(l1)):
    x=l1[j].split()
    for i in range(0,len(x)):
        if x[i]=="UP":
            x2+=int(x[i+1])
        if x[i]=="DOWN":
            x2-=int(x[i+1])
        if x[i]=="LEFT":
            y2+=int(x[i+1])
        if x[i]=="RIGHT":
            y2-=int(x[i+1])
print(y2,x2)
print(round(math.sqrt((x1-y2)**2+(y1-x2)**2))) 


a=input() 
w=[]
a=a.split()
res = {i : a.count(i) for i in set(a)}
for i in sorted (res.keys()) :  
    w.append(i)
for i in w :
    print('{}:{}'.format(i,res[i]))



def square(n):
    return n**2
print(square(int(input())))

print(help(abs))
print(help(int))
print(help(input))

def my():
    """fuuuuuuu"""
    return 0
print(help(my))

def i2s(n):
    return str(n)
print(i2s(int(input())))

class ff(object):
    def __init__(self,p):
        self.p=2
    def tt(self):
        return self.p
a=ff(100)
print(a.tt())

def ads(x,y):
    return int(x)+int(y)
print(ads(input(),input()))

def con(x,y):
    return x+y
print(con(input(),input()))

def high(s1,s2):
    if len(s1)==len(s2):
        return s1,s2
    else:
        return max(s1,s2,key=len)
print(high(input(),input()))


def lc(s1,s2):
    c=0
    pp=0
    i=0
    j=0
    while(i<len(s1)):
        while(i<len(s2)):
            if s1[i]==s1[j]:
                i+=1
                j+=1
    print(s1[i:j])
                
                
    for i in range(0,len(s1)):
        #print(s1[:i+1])
        if s1[:i+1] in s2:
            
            c=len(s1[:i+1])
        #print(s1[i:])
        if s1[i:] in s2:
            
            pp=len(s1[i:])
        for j in range(0,len(s1)):
            if s1[i:] in s2 or s1[:j] in s2:
                print(s1[i:],s1[:j])
                xx=len(s1[i:j])
        print(xx)
                
    #pm=c if c>pp else pp   
    #print(s1[:pm])
    
lc('pyopp;[','pooppop')



def pdict():
    d={i : i**2 for i in range(0,21)}
    print(d)
pdict()

def dickeys():
    d1={i : i**2 for i in range(0,21)}
    print(d1.keys())
dickeys()

def lis():
    l1=[i**2 for i in range(0,21)]
    print(l1)
lis()

def lis1():
    l1=[i**2 for i in range(0,21)]
    print(l1[:5])
lis1()

def lis2():
    l1=[i**2 for i in range(0,21)]
    print(l1[-5:])
lis2()

def lis2():
    l1=[i**2 for i in range(0,21)]
    print(l1[5:])
lis2()

def tp():
    l1=tuple(i**2 for i in range(0,21))
    print(l1)
tp()

def htp(t):
    x=len(t)/2
    print(t[:int(x)])
    print(t[int(x):])
    
t=[int(x)for x in input().split()]
htp(tuple(t))

def etp(t):
    t1=[]
    for i in t:
        if i%2==0:
            t1.append(i)
    print(tuple(t1))
            
    
t=[int(x)for x in input().split()]
etp(t)

def yes(s):
    if s=="yes" or s=="YES" or s=="Yes":
        print("Yes")
    else:
        print("No")
yes(input())

def sq(n):
    return n**2
x=[int(x)for x in input().split()]
l1=map(sq,x)
print(list(l1))

def filt(n):
    if n%2==0:
        return True
    else:
        return False
def ma(f):
    return f**2
x=[int(x)for x in input().split()]
p=filter(filt,x)
l=map(ma,p)
print(list(l))

def fi(n):
    if n%2==0:
        return True
    else:
        return False
x=[int(x) for x in input().split()]
print(list(filter(fi,x)))

def kadane(a):
    c=m=a[0]
    for i in a[1:]:
        c=max(c+i,i)
        m=max(c,m)
    return m
print(kadane([int(x) for x in input().split()]))

class American:
    @staticmethod
    def printNat():
        print("daaaa")
American.printNat()

class American:
    
    def __init__(self):
        y=10
        return y
        
class NewYorker(American):
    def __init__(self):
        print("hii",super().__init__())
a=NewYorker()


class Circle:
    def __init__(self,l):
        self.l=l
    def area(self,l):
        print(math.pi*self.l**2)
c=Circle(10)
c.area(c.l)

class Rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self,l,w):
        print(l*w)
c=Rect(10,20)
c.area(c.l,c.w)

class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self,l):
        self.l=l
    def area(self,l):
        print(super().area())
        print(self.l*self.l)
s=square(4)
s.area(s.l)

raise RuntimeError("raised")




def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        return sys.maxsize 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    else: 
        return cost[m][n] + min( minCost(cost, m-1, n-1), 
                                minCost(cost, m-1, n), 
                                minCost(cost, m, n-1) )
cost= [ [1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3] ] 
print(minCost(cost, 2, 2))

a=input()
print(a[:a.find('@')])

class Error(Exception):
    pass
class aa(Error):
    pass
try:
   
   raise aa
  
except aa:
   print("duh")

def a():
   try:
       c=5/0
       print(a)
   except:
       print("duh")
a()

def count(S, m, n ): 
    if (n == 0): 
        return 1
    if (n < 0): 
        return 0;  
    if (m <=0 and n >= 1): 
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
arr = [1, 2, 3] 
m = len(arr) 
print(count(arr, m, 4)) 


a=input()
print(a[a.find('@')+1:a.find('.')])

a=[]
b=input()
b=b.split()
try:
    for i in b:
        if i.isdigit():
            
            a.append(i)
except:
    w=1
print(a)

a=u'\xeatre'
b=unicodedata.normalize('NFKD', a).encode('ascii','ignore')
print(b)


n= int(input())
a = 0
for i in range(1,n+1):
    a = a+(i/(i+1))
print(round(a,2))

def f(n):
    if n==0:
        return 0
    else:
        yield f(n-1)+100
xx=int(input())
if xx==0:
    print('1')
else:
    print(f(xx))

def fibo(n):
        f=0
        f1=1
        f3=0
        print(f)
        print(f1)
        for i in range(0,n-1):
            f3=f+f1
            f=f1
            f1=f3
            
            print(f3)
fibo(int(input()))


def gen(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
x=[]
for i in gen(10):
    x.append(i)
print(*x,sep=',')


def gen(n):
    for i in range(0,n+1):
        if i%5==0 and i%7==0:
            yield i
x=[]
for i in gen(100):
    x.append(i)
print(*x,sep=',')

f=0
a=[int(x) for x in input().split()]
for i in a:
    try:
        assert i%2==0
        f+=1
    except AssertionError:
        print("no")
        
if f==len(a):
    print("yes")


a=input()
print(eval(a))

print (random.uniform(10,100))

import random
print(random.choice([i for i in range(11) if i%2==0]))


import random
print(random.choice([i for i in range(150) if i%5==0 and i%7==0]))


import random
print (random.sample(range(100), 5))

import random
print (random.sample([i for i in range(100,201) if i%2==0], 5))

import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))

def compress(string):
    temp={}
    result=" "
    for x in string:
        if x in temp:
            temp[x] = temp[x]+1
        else:
            temp[x] = 1
    for key, value in temp.items():
        result += str(key) + str(value)
    return result
s = input("Enter the string:")
print(compress(s))
   

# coding: utf-8

# In[12]:


a=[int(x) for x in input().split()]
def ev(a):
    return [x for x in a if x % 2 != 0] 
ev(a)


# In[18]:


a=[int(x) for x in input().split()]
def ev(a):
    return [x for x in a if ( x % 5 != 0 or x % 7 != 0 )] 
ev(a)


# In[19]:


a=[int(x) for x in input().split()]
def ev(a):
    return [x for x in a if ( a.index(x)%2!=0 )] 
ev(a)


# In[23]:


a=[int(x) for x in input().split()]
def ev(a):
    del a[1:5]
    return a
ev(a)


# In[26]:


a=[int(x) for x in input().split('*')]
def genar(a):
    for i in range(0,4):
        x= [[[0 for y in range(a[i])]for yy in range(a[i+1])]for yyy in range(a[i+2])]
        return x
print(genar(a))


# In[27]:


a=[int(x) for x in input().split()]
def ev(a):
    del a[4:6]
    del a[0]
    return a
ev(a)


# In[28]:


a=[int(x) for x in input().split()]
def ev(a):
       return [x for x in a if x!=24]
ev(a)


# In[31]:


a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
def inter(a,b):
    return [x for x in a if x in b]
print(inter(a,b))


# In[36]:


def remdup(x):
    return list(reversed(list(dict.fromkeys(x))))
remdup([int(x) for x in input().split(',')])


# In[38]:


class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print (aMale.getGender())
print (aFemale.getGender())


# In[39]:


test_str = input ()
res = {} 
res1 = ''.join(sorted(test_str))
res2 = str(res1)
for keys in res2: 
    res[keys] = res.get(keys, 0) + 1

for i in res:
    if i!=' ':
        print(f'{i},{res[i]}')


# In[ ]:


a=input()
print(a[::-1])


# In[2]:


a=input()
def ev(a):
       return a[::2]
print(ev(a))


# In[5]:


from itertools import permutations
a=[int(x) for x in input().split()]
print(list(permutations(a)))


# In[4]:


def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        for j in range(numheads+1):
            if 2*i+4*j==numlegs:
                if i+j==numheads:
                    return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print (solutions)


# In[10]:


i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))


# In[19]:


i=input()
w=int(input())
for y in range(0,len(i)):
    print(i[:w])
    i=i[w:]
    if i=='':
        break


# In[68]:




n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3,'-'))
for i in range(n,1,-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i-1))
    print((s+s[::-1][1:]).center(n*4-3,'-'))    




# In[74]:


import datetime 
import calendar 
  
def findDay(date): 
    x = datetime.datetime.strptime(date, '%m %d %Y').weekday() 
    print(x)
    return (calendar.day_name[x]).upper()
date = '08 05 2015'
print(findDay(date)) 


# In[90]:


a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
def inter(a,b):
    a1=[x for x in a if x not in b]
    b1=[x for x in b if x not in a]
    a1.sort()
    b1.sort()
    c1=a1+b1
    c1.sort()
    yield c1
for i in inter(a,b):
    print(*i,sep='\n')


# In[ ]:


from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range(n):
    word = input()
    d[word] = d.get(word, 0) + 1
    print(d)
print(len(d))
for v in d.values():
    print(v, end=' ')


# In[9]:


test_str = input ()
res = {} 
res1 = ''.join(test_str)
res2 = str(res1)

for keys in res2: 
    res[keys] = res.get(keys, 0) + 1

for i in {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}:
    if i!=' ':
        print(f'{i} {res[i]}')

     



