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

def parrtition(pointList, low, high):
    pivot = pointList[low]
    up, down = low, high
    
    while(True):
        while(up<=down and pointList[up]<=pivot):
            up+=1
        while(up<=down and pointList[down]>pivot):
            down-=1
        
        if(up>down):
            break
        else:
            pointList[up], pointList[down] = pointList[down], pointList[up]
    
    pointList[low], pointList[down] = pointList[down], pointList[low]
    return down

def quicksort(pointList, low, high):
    if(low < high):
        pivot = partition(pointList, low, high)
        quicksort(pointList, low, pivot-1)
        quicksort(pointList, pivot+1, high)

def partition(pointList, low, high):
    pivot = pointList[high]
    up, down = low, high
    comp=low

    for i in range(low, high+1):
        if(pointList[i] < pivot):
            i+=1
            pointList[i], pointList[comp] = pointList[comp], pointList[i]
    pointList[low], pointList[high] = pointList[high],pointList[low]
    return pivot

def quicksort_alg(pointList, low, high):
    pointList = normalized_list(pointList)
    start = time.time()
    
    #quicksort algorithm 
    quicksort(pointList, low, high)
    end = time.time()
    
    pointList = remove_negatives(pointList)
    #return time taken for code to run
    return(end-start, pointList)

"""
def partition(pointList, low, high):
    pivot = pointList[high]
    up, down = low, high
    comp=low

    for i in range(low, high+1):
        if(pointList[i] < pivot):
            i+=1
            pointList[i], pointList[comp] = pointList[comp], pointList[i]
    pointList[low], pointList[high] = pointList[high],pointList[low]
    return pivot
"""