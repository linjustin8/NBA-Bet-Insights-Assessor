#heap.py
import pandas as pd
import numpy as np


#default initiator to grab information from csv and organize it into a map
def dataframe_init():
    #use ../assets/___.csv or assets/___.csv depending on files
    filename = 'assets/boxscore_scrape.csv'
    filename_head = 'assets/NBA_Player_IDs.csv'

    originaldf = pd.read_csv(filename) #maintain original dataframe
    modifieddf=originaldf.copy() #modifying new dataframe

    #cleaning up dataframe by assigning NaN to games players didn't play
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Play',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Not With Team',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Dress',np.nan)
    modifieddf['PTS']=modifieddf['PTS'].replace('Player Suspended',np.nan)

    modifieddf=modifieddf.iloc[1:] #remove header

    #organize csv by player name, and organize each player by points
    modifieddf=modifieddf.sort_values(by=['playerName'],ascending=[True])

    #new dataframe, following ISO-8859-1 update
    player_head = pd.read_csv(filename_head,encoding='ISO-8859-1')
    player_head = player_head.iloc[:,[0,6]]

    originaldf = (final_df_frame(modifieddf,player_head))
    cool_row = {'teamName': 'LeGoat', 'playerName': 'Aman Kapoor', 'PTS': 101, 'NBAID': '11111'}
    originaldf.loc[len(originaldf)]=cool_row

    return originaldf
#------------------------------------------------------------------------------------------

def final_df_frame(df1,df2):

    #create local dataframe to be returned, and create new column with all rows NaN
    df_base = df1
    df_base['NBAID']=np.nan
    df_base['NBAID'] = df_base['NBAID'].astype(str)

    #creating a dictionary by zipping two columns and assinging key-value pairs
    dictionary_of_IDs = dict(zip(df2['BBRefName'],df2['NBAID']))

    #manually populating a hashmap (dictionary) alternative
    hashmap_of_IDs = {}

    #alternative to itterows that saves some time and space
    for column in df2.itertuples(index=False):
        hashmap_of_IDs[column.BBRefName] = column.NBAID

    similarity_map = df_base['playerName'].map(hashmap_of_IDs)
    df_base['NBAID'] = similarity_map.astype(str)

    """ 
            slow nested for loop approach to assigning new values
            could be used as an example for increased efficiency of vectorized approach
    for (key,value) in dictionary_of_IDs.items():
        indexs = df_base[df_base['playerName'] == key].index
        for i in indexs :
            df_base.loc[i,'BBRefID'] = value
            print('in')
        print('out')
        """


    return (df_base)
#-----------------------------------------------------------------------------
def checker(df,player):
    return df['playerName'].str.strip().str.lower().isin([player]).any()
#------------------------------------------------------------------------------
def getID(df,player):
    pass


def list_o_point_create(df, name):
    lisp=[]

    pass

def list_o_name_create(df):
    #implement a Nary tree or B+ tree, not sure yet
    pass

"""
#will be removed, using to check code
if __name__ == "__main__":
    dataframe_init()
"""