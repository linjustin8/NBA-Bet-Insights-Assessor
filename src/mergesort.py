# mergesort.py
from data import *
import pandas as pd
import numpy as np
from headshot import *
import time

def normalized_list(listo):
    for i,j in enumerate(listo):
        listo[i] = int(j)
    return listo

def clean_again(listo):
    lll=[]
    for i in listo :
        if i < 0 :
            continue
        else :
            lll.append(i)
    return(lll)

def mergesort_alg(listo):
    new_list = normalized_list(listo)
    start = time.time()
    lister = merge_base(new_list)
    end = time.time()
    tstat = end-start
    lister = clean_again(lister)
    return(tstat,lister)

def merge_base(listo):
    if len(listo) <= 1 :
        return(listo)
    else :
        mid = len(listo)//2
        left = merge_base(listo[:mid])
        right = merge_base(listo[mid:])
        return(merge_rec(left,right))

def merge_rec(left,right):
    lindex=0
    rindex=0
    sort=[]

    while lindex<len(left) and rindex<len(right) :
        if right[rindex]>left[lindex]:
            sort.append(left[lindex])
            lindex+=1
        else :
            sort.append(right[rindex])
            rindex+=1

    sort.extend(left[lindex:])
    sort.extend(right[rindex:])
    return(sort)
