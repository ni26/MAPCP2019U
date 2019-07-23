
# coding: utf-8

# In[ ]:


def fibo(n_int):
    if n_int == 0:
        return 0
    if n_int == 1:
        return 1
    if n_int >= 2:
        return (fibo(n_int-1)+fibo(n_int-2))       


# In[ ]:


def fib(n):
    my_input = input ("Please enter a non-negative integer: ")
    if my_input ==  'stop':
        if isinstance(n,float):
            print('The input argument {} is not a non-negative integer!'.format(n))
        elif isinstance(n,str):
            print('The input argument {} is not a non-negative integer!'.format(n))
        else:
        return fibo(n)
    else:
        abbr = input ("What is the three letter abbreviation of this course? ")


# In[ ]:


fib ('hi')


# In[ ]:


fib(5.2)


# In[ ]:


fib(12)


# In[ ]:


def fib(n):
    my_signal = 'go'
    while my_signal == 'go':
        if isinstance(n,float):
            print('The input argument {} is not a non-negative integer!'.format(n)) 
            return input ("Please enter a non-negative integer: ")
        elif isinstance(n,str):
            print('The input argument {} is not a non-negative integer!'.format(n))
            return input ("Please enter a non-negative integer: ")
        elif n<0:
            print('The input argument {} is not a non-negative integer!'.format(n))
            return input ("Please enter a non-negative integer: ")
        else:
            print ('Fib({}) = {}'.format(n,fibo(n)))
            return input ("Please enter another non-negative integer or type stop: ")       


# In[ ]:


fib ('hi')


# In[ ]:


fib (-123)


# In[ ]:


fib(12.2)


# In[ ]:


fib(12)


# In[ ]:


fib ('hi')


# In[ ]:


fib (-123)


# In[ ]:


fib (12.2)


# In[ ]:


fib (0)


# In[ ]:


fib('hi')


# In[ ]:


def test(m):
    if m == 1:
        print('hi')
        return 'bye'


# In[ ]:


test(1)


# In[ ]:


# not a good idea:
# while True:
    # print ('hi')


# In[ ]:


my_input = 'hi'
m = 1
while my_input != 'bye':
    print ('input not bye yet')
    m = m+1
    if m == 5:
        my_input = 'bye'


# In[ ]:


def fib(n):
    my_signal = 'go'
    while my_signal == 'go':
        if isinstance(n,float):
            print('The input argument {} is not a non-negative integer!'.format(n)) 
            n = input ("Please enter a non-negative integer: ")
            return n
        elif isinstance(n,str):
            print('The input argument {} is not a non-negative integer!'.format(n))
            n = input ("Please enter a non-negative integer: ")
            return n
        elif n<0:
            print('The input argument {} is not a non-negative integer!'.format(n))
            n = input ("Please enter a non-negative integer: ")
            return n
        else:
            print('Fib({}) = {}'.format(n,fibo(n)))
            n = input ("Please enter another non-negative integer or type stop: ")    
            # return


# In[ ]:


fib ('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib('hi')


# In[ ]:


type(12)


# In[ ]:


fib(12)


# In[ ]:


fib('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib(12)


# In[ ]:


def fibo(n_int):
    if n_int == 0:
        return 0
    if n_int == 1:
        return 1
    if n_int >= 2:
        return (fibo(n_int-1)+fibo(n_int-2))       


# In[ ]:


def fib(n, my_signal = 'go'):
    while my_signal == 'go':
        if isinstance(n,float):
            print('The input argument {} is not a non-negative integer!'.format(n)) 
            n = input ("Please enter a non-negative integer: ")
            #return n
        elif isinstance(n,str):
            print('The input argument {} is not a non-negative integer!'.format(n))
            n = input ("Please enter a non-negative integer: ")
            #return n
        elif n<0:
            print('The input argument {} is not a non-negative integer!'.format(n))
            n = input ("Please enter a non-negative integer: ")
            #return n
        elif type(n) == int and n>=0:
            print('Fib({}) = {}'.format(n,fibo(n)))
            n = input ("Please enter another non-negative integer or type stop: ")    
            # return


# In[ ]:


fibo(12)


# In[ ]:


fibo(11)


# In[ ]:


fib('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib(12)


# In[ ]:


n == 1 
if n is int:
    print('hi')


# In[ ]:


type (n)


# In[ ]:


n = 2
if n>0:
    print('hi')


# In[ ]:


type(n)


# In[ ]:


type(type(n))


# In[ ]:


m = 12
if type(m) == int:
    print('hi')


# In[ ]:


fib('hi')


# In[ ]:


fib(12)


# In[ ]:


print('hi')


# In[ ]:


def my_fun(x):
    print('hi func')


# In[ ]:


my_fun(2)


# In[ ]:


def my_fun(x):
    print('hi func')
    return


# In[ ]:


my_fun(3)


# In[ ]:


def my_fun(x):
    print('hi func')
    return x


# In[ ]:


my_fun(5)


# In[39]:


def fibo(n_int):
    if n_int == 0:
        return 0
    if n_int == 1:
        return 1
    if n_int >1:
        return (fibo(n_int-1)+fibo(n_int-2))  


# In[40]:


def fib(n):
    n = input ("1 Please enter a non-negative integer: ")
    while True:
        if round(n) != n and n<0:
            print('1 The input argument {} is not a non-negative integer!'.format(n)) 
            fib
        if type(n) == str:
            print('2 The input argument {} is not a non-negative integer!'.format(n))
            n = input ("2 Please enter a non-negative integer: ")
        return 'go'
        if type(n) == int and n>=0:
            print('Fib({}) = {}'.format(n,fibo(n)))
            n = input ("Please enter another non-negative integer or type stop: ")    
        return 'go'
        #else:
            #print('3 The input argument {} is not a non-negative integer!'.format(n))
            #n = input ("3 Please enter a non-negative integer: ")
        #return n


# In[41]:


fibo(4)


# In[42]:


round(4.2)


# In[43]:


round(4.9)


# In[32]:


fib(1.1)


# In[34]:


fib(1.1)


# In[38]:


fib(1.1)


# In[4]:


fib(12.1)


# In[5]:


fib(12.2)


# In[6]:


fib (13.1)


# In[10]:


fib(14.2)


# In[13]:


fib(1.1)


# In[19]:


fib(1.1)


# In[29]:


my_word = 5
while my_word == 5:
    print('hi')
    my_word = my_word-1


# In[1]:


def fib(n):
    def fibo(n_int):
        if n_int == 0:
            return 0
        if n_int == 1:
            return 1
        if n_int >1:
            return (fibo(n_int-1)+fibo(n_int-2))
    if n == 'stop':
        return None
    elif round(n) == n and n>=0:
        print('Fib({}) = {}'.format(n,fibo(n)))
        n = input ("Please enter another non-negative integer or type stop: ")
        return fib(n) 
    else:
        print('The input argument {} is not a non-negative integer!'.format(n))
        n = input ("Please enter a non-negative integer: ")        
        return fib(n)


# In[2]:


fib(0)

