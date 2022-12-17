# -*- coding: utf-8 -*-

import time
import weave
import numpy as np

def test1(entrada):
    a = 0
    for i in range(0,entrada):
        a+=i
    
    return a

def test1_weave(entrada):
    result = 0
    code =  """
            for (int i = 0; i < entrada; i++)
            {
               result += i;
            }
            """
    weave.inline(code,['result','entrada'],compiler='gcc')

    return result

def test2(entrada):
    a = 0

    for i in range(entrada):
        a += i**(1/2)
    
    return a

def test2_weave(entrada):
    result = 0
    code =  """
            for (int i = 0; i < entrada; i++)
            {
               result += sqrt(i);
            }
            """
    weave.inline(code,['result','entrada'],compiler='gcc')

    return result

def test3(entrada):
    
    a=0

    for i in range(len(entrada)):
        a += entrada[i]

    return a

def test3_weave(entrada):
    
    n = len(entrada)
    result = 0

    code =  """
            for (int i = 0; i < n; i++)
            {
                result += entrada[i];
            }
            """
                
    weave.inline(code,['entrada','n','result'],compiler='gcc')
    
    return m


for e in range(1,2**20):

    #Test 1

    t1 = time.time()

    for i in range(e):
        test1(e)

    t1_final = t1 - time.time()

    t1_w = time.time()

    for i in range(e):
        test1_weave(e)

    t1_wf = t1_w - time.time()


    #Test 2

    t2 = time.time()

    for i in range(e):
        test2(e)

    t2_final = t2 - time.time()

    t2_w = time.time()

    for i in range(e):
        test2_weave(e)

    t2_wf = t2_w - time.time()

    #Test 3

    m = list(range(e))

    t3 = time.time()

    for i in range(e):
        test3(m)

    t3_final = t3 - time.time()

    t3_w = time.time()

    for i in range(e):
        test3_weave(m)

    t3_wf = t3_w - time.time()

    print(t1_wf,";",t2_wf,";",t3_wf)
