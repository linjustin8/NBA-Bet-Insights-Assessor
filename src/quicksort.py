# quicksort.py
from data import *
import pandas as pd
import numpy as np
from headshot import *
import time

def normalized_list(pointList):
    for i,j in enumerate(pointList):
        pointList[i] = int(j)
    return pointList

def remove_negatives(pointList):
    temp=[]
    for i in pointList :
        if i < 0 :
            continue
        else :
            temp.append(i)
    return(temp)

def partition(pointList, low, high):
    pivot = pointList[low]
    up, down = low, high
    
    while(up<down):
        for j in range(low, high):
            if(pointList[up] > pivot):
                break
            up+=1
        for j in range(high, low, -1):
            if(pointList[down] < pivot):
                break
            down-=1
        if(up<down):
            pointList[up], pointList[down] = pointList[down], pointList[up]
    
    pointList[up], pointList[down] = pointList[down], pointList[up]
    return down

def quicksort_alg(pointList, low, high):
    pointList = normalized_list(pointList)
    start = time.time()
    
    #quicksort algorithm 
    if(low < high):
        pivot = partition(pointList, low, high)
        quicksort_alg(pointList, low, pivot-1)
        quicksort_alg(pointList, pivot+1, high)
    end = time.time()
    
    pointList = remove_negatives(pointList)
    #return time taken for code to run
    return(end-start, pointList)