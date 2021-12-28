#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def number_sum(n1, n2):
    result = n1 + n2
    return result


# In[ ]:


def cal(num1, num2, op):
    '''덧셈과 뺄셈을 계산하는 함수'''
    if op == '+':
        return num1+num2
    elif op == '-' :
        return num1-num2
    else :
        return '뭐여! 시방 지금 장난하냐'


# In[ ]:


def add(*n):
    return sum(n)


# In[ ]:


def add_sub(num1, num2):
    return num1+num2, num1-num2


# In[ ]:


def power_of_N(num, power=2):
    return num**power

