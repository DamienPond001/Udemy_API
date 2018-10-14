#Dataframes are made up of Series objects. Each Series is labelled 1D numpy array

import pandas as pd
#df is some DataFrame
df.head()
df.tail()

df.iloc[1, :]
df.loc['row_index', :]

#to return column info
df.info()

#to convert DataFrame to numpy array:
df.values

#note though that many numpy methods work on pandas dfs

########
#creating Dataframes from scratch
########

d = {"col1" :[1,3,4,5], "col2" : [4,5,6,7]}
df = pd.DataFrame(d)

col1 = [1, 3, 5, 6]
col2 = [6, 7, 8, 9]

cols = [col1, col2]
indices = ["col1", "col2"]

d = zip(indices, cols)
d = dict(list(d))
df = pd.DataFramed

df.columns = ["newcol1", "newcol2"]

#Broadcasting
df['col3'] = "M"

d = {"col1" : [1, 3, 4, 5], "col2" : "M"}
df = pd.DataFrame(d) #Broadcasts col2