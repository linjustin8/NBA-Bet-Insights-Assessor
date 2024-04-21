#heap.py
import pandas as pd
import numpy as np
import heapq

"""
to download libraries, enter below into terminal : 

    pip install pandas
    pip install numpy

"""


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

