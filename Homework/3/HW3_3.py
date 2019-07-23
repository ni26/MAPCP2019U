
# coding: utf-8

# # Problem 2

# ## A

# In[2]:


abbr = input ("What is the three letter abbreviation of this course? ")

answer_status = 'wrong'
if abbr == 'ECL':
    answer_status = 'correct'

if answer_status=='correct':
    print('Your answer is correct!')
else:
    print("wrong buddy...try again")


# In[4]:


abbr = input ("What is the three letter abbreviation of this course? ")

answer_status = 'wrong'
if abbr == 'ECL': answer_status = 'correct'    

if answer_status=='correct':
    print('Your answer is correct!')
else:
    print("wrong buddy...try again")


# ## B

# In[7]:


# Tuple notation
abbr = input ("What is the three letter abbreviation of this course? ")

print('Your answer is correct!' if abbr == 'ECL' else "wrong buddy...try again")


# # Problem 3

# ## A

# In[132]:


data = input ("Enter the first name, last name, and the city of the person (comma-separated):")


# In[146]:


hi = 'Niyousha, Davachi, Arlington'


# In[147]:


print(hi)


# In[152]:


my_tuple = ()
for i in range(len(new_hi)):
    element = (new_hi[i]).lower()
    my_tuple = my_tuple + (element,)
print (my_tuple)


# ## B

# In[153]:


def dummy(i):
    if i==0:
        j=0
    elif i==1:
        j=1
    elif i==2:
        j=2
    else: j = 'j is not in [0,1,2]' 
    return j


# In[154]:


dummy (5)


# In[155]:


dummy(1)


# In[158]:


print (range(0,3))


# In[157]:


type(range(0,3))


# In[161]:


print(i if i ==0 or 1 or 2 else 'j is not in [0,1,2]')


# In[171]:


def dummy (i):
    return i if -1<i<=2 else 'j is not in [0,1,2]'


# In[172]:


dummy (5)


# In[173]:


dummy (0)


# In[174]:


dummy (-1)


# In[175]:


dummy (1)


# In[176]:


dummy(2)


# # Problem 4

# In[197]:


def get_triangle_area(vertices):
    """
    Getting the area of a triangle.
    """
    v1=(0,0); v2=(0,0); v3=(0,0)
    vertices = [v1, v2, v3]
    return abs((1/2)*(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1]))
    


# In[198]:


vertices =  [(0,0), (1,0), (0,2)]


# In[199]:


get_triangle_area(vertices)


# In[187]:


v1=(0,0); v2=(0,0); v3=(0,0)
vertices = [v1, v2, v3]


# In[188]:


type(vertices)


# In[177]:


import math


# In[178]:


abs(-1)


# In[179]:


v4=(3,4)


# In[181]:


print(v4[0])
print(v4[1])


# In[203]:


def get_triangle_area(v1,v2,v3):
    """
    Getting the area of a triangle.
    """
    return abs((1/2)*(v2[0]*v3[1]-v3[0]*v2[1]-v1[0]*v3[1]+v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1]))


# In[201]:


get_triangle_area((0,0),(1,0),(0,2))


# # Problem 5

# In[252]:


def is_prime(n):
    is_prime = True
    if n == 1:
        print('{} is a prime number'.format(n))
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                is_prime = False
                break
        print ('{} is not a prime number'.format(n) if is_prime == False else '{} is a prime number'.format(n))


# In[253]:


is_prime(1)


# In[254]:


is_prime(2)


# In[255]:


is_prime(3)


# In[256]:


is_prime(4)


# In[257]:


is_prime(5)


# In[258]:


is_prime(6)


# In[259]:


is_prime(6)


# In[260]:


is_prime(7)


# In[261]:


is_prime(8)


# In[262]:


is_prime(16)


# In[263]:


is_prime(13)


# In[264]:


is_prime(23)


# # Problem 7

# In[271]:


q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]


# In[272]:


my_string = ''


# In[267]:


type(my_string)


# In[269]:


new_string = my_string + 'hi'


# In[270]:


print(new_string)


# In[292]:


q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]


# In[293]:


m_str = ''
for i in range(len(q)):
    for j in range(len(q[i])):
        m_str = m_str+(q[i])[j]
print(m_str)


# In[294]:


type(m_str)


# In[283]:


print(range(len(q)))


# In[284]:


for i in range(len(q)):
    print('i currently is {}'.format(i))


# In[286]:


print (q[0])


# In[287]:


print(range(len(q[0])))


# In[289]:


for j in range(len(q[0])):
    print('j currently is {}'.format(j))


# In[291]:


print((q[0])[0])


# # Problem 8

# In[295]:


from math import sqrt
for n in range(1, 60):
    r_org = 2.0
    r = r_org
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print ('With {} times sqrt and then {} times **2, the number {} becomes: {:.16f}'.format(n,n,r_org,r))


# In[296]:


# This tells us that depending on the type of float we pick, the round off error can wind up giving us something
# completely different than what we started from. This is extremely important as in computations this can completey
# change the results of what we have. 


# # Problem 9

# In[297]:


eps = 1.0
while 1.0 != 1.0 + eps:
    print ('...............', eps)
    eps /= 2.0
print ('final eps:', eps)


# In[298]:


# we would imagine that this code would be infinite, but it is not. The reason is round off errors again. Each time that we
# divide epsilon by two, we are introducing a round off error which eventually makes the code to stop.


# # Problem 11

# In[299]:


numbers = list(range(10))
print(numbers)


# In[300]:


for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del {}'.format(n,i), numbers)


# In[ ]:


# First, the i is defined which is half of what we see in numbers (elements divided by 2). This means i is 5. But it jumps
# the n = 4 step and it prints something else. We would expect those numbers to be 0,1,2,3,4,5, but they are not. 


# In[1]:


4//2


# # Problem 12

# In[2]:


def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<(divisor-1)*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    count = 0
    if n == 1:
        return count
    else:
        if is_prime(n):
            count = 1
        n -= 1
        return count + get_primes(n)


# In[3]:


get_primes(13)


# In[4]:


get_ipython().run_line_magic('timeit', 'get_primes')


# In[5]:


get_ipython().run_line_magic('timeit', 'is_prime')

