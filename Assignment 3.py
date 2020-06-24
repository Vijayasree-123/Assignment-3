#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1.To find area of a circle using math module
import math
r= float(input("Enter the radius of circle:"))
area = math.pi*(r**2)
print("The Area of circle is : ",area)


# In[9]:


# 2. To find area of regular polygon
from math import tan, pi
n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
a=(n*(l**2))/(4*math.tan(math.pi/n))
print("The area of the polygon is: ",a)


# In[10]:


# 3. To find areea of a segment of a circle formula using math module
import math
t=float(input("enter the angle measure"))
r=float(input("enter the radius of circle"))
if t>=360:
    print("the angle is not possible")
else:
    a=(math.pi*(r**2)*(t/360))-((1/2)*(r**2)*math.sin((t*math.pi)/180))
    print("the area of segment=",a)


# In[7]:


# 4. To generate random number from the list
import random
print("A random from list is")
print(random.choice([100,1,2,3,30,40]))


# In[11]:


# 5. To generate random numbers between 1,10000 and difference between each random number is 50
import random
print("the random numbers between 1 to 10000",random.randrange(1,10000,50))


# In[12]:


#6. Calculating using math module
import math
print("the value of sin(60) is",math.sin(60))
print("the value of cos(pi)is",math.cos(math.pi))
print("the value of tan(90) is",math.tan(90))
print("the angle of sin(0.8660254037844386)is",math.degrees(math.asin(0.8660254037844386)))
print("the value of 5^8 is",5**8)
print("the value of squareroot of 400is",math.sqrt(400))
print("the value of 5^e is",5**math.e)
print("the value of log(1024)base 2 is",math.log(1024,(2)))
print("the value of log(1024)base 10 is",math.log(1024,(10)))
print("the floor value of 23.56 is",math.floor(23.56))
print("the ceiling value of 23.56 is",math.ceil(23.56))


# In[ ]:




