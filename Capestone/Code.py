import pandas as pd
import numpy as np
import csv

f1 = 'anime.csv'
f2 = 'rating.csv'

df = pd.read_csv(f1)
rf = pd.read_csv(f2)

df.head()
rf.head()
rf.shape
fd = df.anime_id.unique()
df.episodes.unique()
df["episodes"] = df["episodes"].map(lambda x: np.nan if x == "Unknown" else x)
df["episodes"].fillna(df['episodes'].median(), inplace=True)
df.episodes.unique()
rf.rating.unique()

rf["rating"] = rf["rating"].map(lambda x: np.nan if x == -1 else x)

rf.rating.unique()


fd = df.anime_id.unique()
np.sort(fd)
fr = rf.anime_id.unique()
np.sort(fr)
len(fr)
len(fd)
