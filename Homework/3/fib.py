
# coding: utf-8

# In[1]:


def fibo(n_int):
    if n_int == 0:
        return 0
    if n_int == 1:
        return 1
    if n_int >= 2:
        return (fibo(n_int-1)+fibo(n_int-2))       


# In[4]:


def fib(n):
    if isinstance(n,float):
        print('The input argument {} is not a non-negative integer!'.format(n))
    elif isinstance(n,str):
        print('The input argument {} is not a non-negative integer!'.format(n))
    else:
        return fibo(n)


# In[13]:


fib ('hi')


# In[14]:


fib(5.2)


# In[5]:


fib(12)

