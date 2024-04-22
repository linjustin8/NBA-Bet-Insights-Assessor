#heap.py
import pandas as pd
import numpy as np
import heapq


#default initiator to grab information from csv and organize it into a map
def dataframe_init():
    filename = '../assets/boxscore_scrape.csv'

    originaldf = pd.read_csv(filename) #maintain original dataframe
    modifieddf=originaldf.copy() #modifying new dataframe

    #cleaning up dataframe by assigning NaN to games players didn't play
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Play',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Not With Team',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Dress',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Player Suspended',np.nan)

    modifieddf=modifieddf.iloc[1:] #remove header

    #organize csv by player name, and organize each player by points
    modifieddf=modifieddf.sort_values(by=['playerName','PTS'],ascending=[True,False])

    print(originaldf.head())
    print(modifieddf.head())

    return modifieddf



def list_o_point_create(df):
    #will implement either a map or a heap here
    pass

def list_o_name_create(df):
    #implement a Nary tree or B+ tree, not sure yet
    pass


#will be removed, using to check code
if __name__ == "__main__":
    dataframe_init()