#heap.py
import pandas as pd
import numpy as np
import heapq


#default initiator to grab information from csv and organize it into a map
def dataframe_init():
    filename = '../assets/boxscore_scrape.csv'
    filename_head = '../assets/NBA_Player_IDs.csv'

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

    #new dataframe, following ISO-8859-1 update
    player_head = pd.read_csv(filename_head,encoding='ISO-8859-1')
    player_head = player_head.iloc[:,[0,2]]

    originaldf = (final_df_frame(modifieddf,player_head))

    print(originaldf)

    return originaldf


def final_df_frame(df1,df2):

    #create local dataframe to be returned, and create new column with all rows NaN
    df_base = df1
    df_base['BBRefID']=np.nan

    #creating a dictionary by zipping two columns and assinging key-value pairs
    dictionary_of_IDs = dict(zip(df2['BBRefName'],df2['BBRefID']))
    for (key,value) in dictionary_of_IDs.items():



    return (df_base)


def list_o_point_create(df):
    #will implement either a map or a heap here
    pass

def list_o_name_create(df):
    #implement a Nary tree or B+ tree, not sure yet
    pass


#will be removed, using to check code
if __name__ == "__main__":
    dataframe_init()