# Quiz 3    
## a)  
def sum_fun(m):  
    my_sum = 0  
    if m ==0:  
        my_sum = my_sum + 1  
        return my_sum  
    else:  
        return (1/2)**(m) + sum_fun(m-1)      
## b)  
def sum_fun_loop(m):  
    my_sum = 0  
    if m == 0:  
        my_sum = my_sum + 1  
        return my_sum  
    else:  
        while True:  
            my_sum = my_sum + (1/2)**(m)  
        return my_sum  
## c) 
%timeit sum_fun  
31.4 ns ± 2.24 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)  		


