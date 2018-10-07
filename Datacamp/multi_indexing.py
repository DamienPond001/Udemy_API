#Sometimes we may want multiple row indexes in a heirachical order
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

sales = 
             eggs  salt  spam
state month                  
CA    1        47  12.0    17
      2       110  50.0    31
NY    1       221  89.0    72
      2        77  87.0    20
TX    1       132   NaN    52
      2       205  60.0    55
      
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1)]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2),:]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2),:]