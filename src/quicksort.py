# quicksort.py
from data import *
import pandas as pd
import numpy as np
from headshot import *
import time

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
    start = time.time()
    
    #quicksort algorithm 
    if(low < high):
        pivot = partition(pointList, low, high)
        quicksort_alg(pointList, low, pivot-1)
        quicksort_alg(pointList, pivot+1, high)
    end = time.time()
    
    #return time taken for code to run
    return(end-start, pointList)