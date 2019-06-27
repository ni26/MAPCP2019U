
# coding: utf-8

# In[14]:


import numpy as np
import sys
from cmath import sqrt
from math import sqrt


# # Problem 1 (Python)

# In[2]:


a = 1 


# In[3]:


b = 'x'


# In[4]:


get_ipython().run_line_magic('whos', '')


# In[5]:


c = true


# In[6]:


c = True


# In[7]:


get_ipython().run_line_magic('whos', '')


# In[8]:


whos a b c


# In[9]:


a == c


# In[10]:


a+c


# In[11]:


d = [1 2 3 4]


# In[12]:


e = ['a' 'b' 'c' 'd']


# In[13]:


e


# In[14]:


print (e)


# In[15]:


f = ['a','b','c','d']


# In[16]:


f


# In[17]:


g = ['abcd']


# In[18]:


g


# In[19]:


get_ipython().run_line_magic('whos', '')


# In[20]:


h = {'a' 'b' 'c' 'd'}


# In[21]:


h


# In[22]:


get_ipython().run_line_magic('whos', '')


# In[23]:


i = {a b c d}


# In[24]:


get_ipython().run_line_magic('whos', '')


# In[25]:


class(a)


# In[26]:


type(a)


# In[27]:


True


# In[28]:


true


# In[29]:


False


# In[30]:


false


# In[31]:


get_ipython().run_line_magic('whos', '')


# # Problem 1 (MATLAB)

# # Problem 2 (Python)

# In[35]:


sys.maxsize


# In[37]:


sys.maxint


# In[40]:


sys.int8(max)


# In[47]:


np.(int16)


# In[48]:


hi = dtype='int16'


# In[49]:


hi


# In[17]:


np.int8(1000)


# In[19]:


np.int8(2000)


# In[20]:


intmax


# In[21]:


int8(max)


# In[22]:


np.int8(max)


# In[57]:


eight = np.int8(500000)
sixteen = np.int16(500000)
thirty_two = np.int32(500000)


# In[58]:


eight


# In[59]:


sixteen


# In[60]:


thirty_two


# In[62]:


help()


# In[67]:


min_value = np.iinfo(np.int8.dtype).min
max_value = np.iinfo(np.int8.dtype).max


# In[72]:


number_1 = np.iinfo(np.int8)


# In[73]:


number_1.min


# In[74]:


number_1.max


# In[76]:


number_2 = np.iinfo(np.int16)


# In[77]:


number_2.min


# In[78]:


number_2.max


# In[79]:


number_3 = np.iinfo(np.int32)


# In[80]:


number_3.min


# In[82]:


number_3.max


# # Problem 2 (MATLAB)

# # Problem 3 (Python)

# In[24]:


int(1/2)


# In[25]:


int(.75)


# In[26]:


int8(1/2)


# In[27]:


np.int8(1/2)


# In[84]:


1/2


# In[85]:


1./2.


# In[86]:


1\2


# In[87]:


int8(1/2)


# In[88]:


np.int8(1/2)


# In[89]:


int8(1/3)


# In[90]:


np.int8(1/3)


# In[91]:


-5^2


# In[92]:


-5**2


# In[93]:


(-5)^2


# In[94]:


(-5)**2


# In[95]:


10-6/2


# In[96]:


5*4/2*3


# # Problem 3 (MATLAB)

# # Problem 4 (Python)

# In[29]:


diag()


# In[30]:


np.diag()


# In[31]:


np.diag(a)


# In[32]:


np.diag(a,1)


# In[33]:


np.diag(1)


# In[106]:


a_1 = 2*np.eye(3,dtype=int)


# In[107]:


a_1


# In[108]:


f = 2*a_1


# In[109]:


f


# In[110]:


np.diag(a_1)


# In[111]:


np.zeros(a_1)


# In[112]:


np.zeros(3)


# In[113]:


a_2 = np.zeros((3,3))


# In[114]:


a_2


# In[119]:


a_3 = np.diag((2,2,2))


# In[120]:


a_3


# In[121]:


a_4 = np.diag([2,2,2])


# In[122]:


a_4


# # Problem 4 (MATLAB)

# # Problem 6 (Python)

# In[2]:


get_ipython().system("# \\usr\\bin\\env 'python'")

_life_expectancy = 120; print( '\n' + 'The life expectancy for the millennials is projected to be %% years! (But don't believe it...)' + '\n', % {_life_expectancy}l ):

  print( '''
    A recent study published in the journal of Nature, discovered that over the past century,
    although the life expectancy has significantly increased due to technological advances,
    the maximum life span of the oldest people in the world has not changed much.
"""

from cmath import sqrt # cmath function always return complex numbers
  from math import sqrt # math function always work with and return real numbers
 print ("""
Cardano was the first to introduce complex numbers of the form a + sqrt(-b) into algebra, but he had misgivings about it. \

In his solution to an algebra equation he encountered the solution 5 + sqrt(-15) for the unknown, which is now mathematically represented by \n \n \
      {first:} \n\nin Python, which can also be obtained as an addition of real and imaginary numbers in Python like this \n\n\
      
      5 + sqrt(-15) = {second:}, \n\n
      which can also be manually stated as 
      
      
      {third:} \n

\
""" % format( second=complex(5,-15) , first=5+sqrt(-15) , third=5+3.872983346207417i ) )

print('''

One final note: \n
\tIn python the sqrt function from math and cmath modules are different.
\tThe sqrt function that returns "float" results is sqrt from math module.
\tTherefore, if using math module, then,

\t\tsqrt(25) = {:.4f}, 

\twhich is obviously a float (real number).

''' .format(sqrt(25)) 
)

print('''

Also note that by convention, 0**0 = {first:d} in Python.
And division by 0, will give you a runtime exception: 1/0 = {second:}

''' .format(first=0**0,second=1/0) 
)


# In[29]:


#!# \usr\bin\env 'python'

_life_expectancy = 120 
print("The life expectancy for the millennials is projected to be %d years! (But don't believe it...)" % (_life_expectancy))

print('''A recent study published in the journal of Nature, discovered that over the past century,
    although the life expectancy has significantly increased due to technological advances,
    the maximum life span of the oldest people in the world has not changed much.''')

from cmath import sqrt # cmath function always return complex numbers
from math import sqrt # math function always work with and return real numbers
print ("""
Cardano was the first to introduce complex numbers of the form a + sqrt(-b) into algebra, but he had misgivings about it. \n

In his solution to an algebra equation he encountered the solution 5 + sqrt(-15) for the unknown, which is now mathematically represented by \n \n \
      {first} \n\nin Python, which can also be obtained as an addition of real and imaginary numbers in Python like this \n\n\
      
      5 + sqrt(-15) = {second}, \n\n
      which can also be manually stated as 
      
      
      {third} \n

\
""".format(first=5+sqrt(15),second=complex(5,-15),third="5+3.872983346207417i"))

print('''

One final note: \n
\tIn python the sqrt function from math and cmath modules are different.
\tThe sqrt function that returns "float" results is sqrt from math module.
\tTherefore, if using math module, then,

\t\tsqrt(25) = {:.4f}, 

\twhich is obviously a float (real number).

''' .format(sqrt(25)) 
)

print('''

Also note that by convention, 0**0 = {first:d} in Python.
And division by 0, will give you a runtime exception: 1/0 = {second:}

''' .format(first=0**0,second=1/0) 
)


# # Problem 9 (Python)

# In[31]:


print('''This is Python version 3.5.2 

Python is the best language for String manipulation!

!noitalupinam gnirtS rof egaugnal tseb eht si nohtyP

!otlpnmgit o gunlte h inhy

pYTHON IS THE BEST LANGUAGE FOR sTRING MANIPULATION!


The sentence 'Python is the best language for String manipulation!' contains 
4 'a' letters, and
0 'A' letters!

Python
is
the
best
language
for
String
manipulation!

PYTHON
IS
THE
BEST
LANGUAGE
FOR
STRING
MANIPULATION!''')


# # Problem 10

# In[33]:


from math import pi, exp, sqrt


# In[37]:


f= (1/sqrt(2*pi)*2)*(exp((-1/2)*((1/2)**2)))


# In[38]:


f


# # Problem 11

# In[39]:


true = fox is rev in Persian


# In[40]:


# Could not download the script.
# It said page doesn't exist


# # Problem 12

# In[43]:


def f(x):
    return x


# In[44]:


print(f(5))


# In[56]:


from math import pi, exp, sqrt, log, e


# In[59]:


def time():
    return ((((67)**(2/3))*3.7*((1.038)**(1/3)))/(0.0054*(pi**2)*(((4*pi)/3)**(2/3)))*(np.log(0.75*(-80/-30)))) 


# In[60]:


time()


# # Problem 13

# In[61]:


a = 5
b = a
print (id(a), id(b))


# In[62]:


# pointing to same memory location


# In[63]:


c = b
b = 3
print (a,b,c)
print (id(a),id(b),id(c))


# In[64]:


# different memory locations


# In[65]:


b = a
b = 5
print (id(a), id(b))


# In[66]:


# Same memory locations


# In[67]:


a = [5]
b = a
print (id(a), id(b))


# In[68]:


# same memory location


# In[70]:


b.append(1)
print (a,b)
print (id(a),id(b))


# In[71]:


# Still same memory location


# In[72]:


a = [5]
b = list(a)
print (a,b)
print (id(a), id(b))


# In[73]:


# Different memory locations


# In[74]:


b = a[:]
print (a,b)
print (id(a), id(b))


# In[75]:


# Different memory locations


# In[76]:


a = (5,)
b = tuple(a)
print (id(a), id(b))


# In[77]:


#Same memory location


# In[78]:


b = a[:]
print (id(a), id(b))


# In[79]:


# Same memory location


# # Problem 14

# In[86]:


name =  {'Christian-Andrew Bagby-wright',
'Matthew Chrysler',
'Niyousha Davachi',
'Pauline Dredger',
'Marcos Guillen',
'Lauren Kuffel',
'Shashank Kumbhare',
'Hany Mahdy',
'Sarah Moorman',
'Andrew Myers',
'Joshua Osborne',
'Rebecca Proni',
'Amir Shahmoradi',
'Carolina Vedovato'
}
role = {'student'*5}


# In[83]:


len(role)


# In[85]:


print(role)

