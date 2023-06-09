# -*- coding: utf-8 -*-
"""Copy of basketball fp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPmAurTTzpWgWWQS0xacnd-9c9VofVFv
"""

import matplotlib.pyplot as plt, numpy as np
import seaborn as sns
import pandas as pd
!pip install pandas
!pip install --upgrade xlrd

from google.colab import drive
drive.mount('/content/drive')

#!ls"/content/drive/My Drive/fp_521"
df=pd.read_excel('drive/My Drive/fp_421/suns_data.xls')
df.head()

team_dict = {'hawks_data': 'Hawks'
,'celtics_data' : 'Celtics'
,'wizards_data' : 'Wizards'
,'Hornets_data' : 'Hornets'
,'Bulls_data' : 'Bulls'
,'Cavaliers_data' : 'Cavaliers'
,'Mavericks_data' : 'Mavericks'
,'Nuggets_data' : 'Nuggets'
,'Pistons_data' : 'Pistons'
,'Warriors_data' : 'Warriors'
,'Rockets_data' : 'Rockets'
,'Pacers_data' : 'Pacers' 
,'Clippers_data' : 'Clippers'
,'Lakers_data' : 'Lakers'
,'Grizzlies_data' : 'Grizzlies'
,'Heat_data' : 'Heat'
,'Bucks_data' : 'Bucks'
,'Timberwolves_data' : 'Timberwolves'
,'Pelicans_data' : 'Pelicans'
,'Knicks_data' : 'Knicks'
,'Thunder_data' : 'Thunder'
,'Magic_data' : 'Magic'
,'76ers_data' : '76ers'
,'Suns_data' : 'Suns'
,'Trail_Blazers_data' : 'Blazers'
,'Kings_data' : 'Kings'
,'Spurs_data' : 'Spurs'
,'Raptors_data' : 'Raptors'
,'Jazz_data' : 'Jazz'}

team_dict =  {k.lower(): v for k, v in team_dict.items()}
team_dict_len = len(team_dict)

print(team_dict)

master_df = pd.read_excel('drive/My Drive/fp_421/nets.xls')
cols_to_check = master_df.columns
master_df['is_na'] = master_df[cols_to_check].isnull().apply(lambda x: all(x), axis=1) 
master_df = master_df[master_df['is_na']==False]
master_df['TEAM'] = 'Nets'
for key in team_dict:
    xls_name = key + '.xls'
    data = pd.read_excel('drive/My Drive/fp_421/'+xls_name)
    cols_to_check = data.columns
    data['is_na'] = data[cols_to_check].isnull().apply(lambda x: all(x), axis=1) 
    data = data[data['is_na']==False]
    data['TEAM'] = team_dict[key]
    master_df = master_df.append(data)

"""# New Section"""

master_df.shape

master_df.head(40)

"""Checking for null values:"""

master_df.isnull().sum()

master_df[master_df.isna().any(axis=1)]

master_df = master_df.fillna(0) #filled null with zeroes since most of the players with null values had zeroes everywhere else.
master_df.isnull().sum() #no more null values

"""Manipulating our dataframe: """

#adding in teams that made it to the final four manually since this is simpler than webscraping

master_df['Final_Four']=np.where(((master_df["TEAM"] == "Warriors") | (master_df["TEAM"] == "Mavericks") | (master_df["TEAM"] == "Heat") | (master_df["TEAM"] == "Celtics")), 1, 0)
master_df.head()
master_df['Final_Four'].value_counts()

"""Separating our data into 2: one df with 'active players' which we defined as players that played more than 30 mins during the season. """

active_players = master_df[master_df['MP']>=30]
active_players

"""Visualizations:"""

plt.hist(master_df['MP'])
plt.title("Distribution of Minutes Played")
plt.show()

plt.hist(master_df['Age'])
plt.title("Distribution of Player Ages")
plt.show()

"""That's odd, why do we have players that are between 0-4? Let's take a look at this"""

master_df[master_df['Age']<18] #looks some players have 0's as their name, maybe we concatenated the data incorrectly?

"""Checking for collinearity: 
We can see that there may be some collinearity concerns between features. Specifically, ORB and TRB, TRB and STL, TOV and ORB, TOV and TRB, TOV and STL, TOV and MP, MP and FGA, MP and 3P, etc.
"""

correlation_features = master_df.drop(['Player_name', 'TEAM'], axis=1)
corr = correlation_features.corr()
heatmap = sns.heatmap(corr)
plt.show()

cols = df.columns
for i in team_dict_len():

