# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index = 'Edition', columns='NOC', values= "Athlete", aggfunc='count')

# Slice medals_won_by_country: cold_war_usa_urs_medals
cold_war_usa_urs_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]
NOC        USA    URS
Edition              
1952     130.0  117.0
1956     118.0  169.0
1960     112.0  169.0
1964     150.0  174.0
1968     149.0  188.0
1972     155.0  211.0
1976     155.0  285.0
1980       NaN  442.0
1984     333.0    NaN
1988     193.0  294.0

# If .max() returns the maximum value of Series or 1D array, .idxmax() returns the index of the maximizing element. 
# Create most_medals 
most_medals = cold_war_usa_urs_medals.idxmax(axis='columns')
Edition
1952    USA
1956    URS
1960    URS
1964    URS
1968    URS
1972    URS
1976    URS
1980    URS
1984    USA
1988    URS
dtype: object
# Print most_medals.value_counts()
print(most_medals.value_counts())


In [5]: cold_war_usa_urs_medals.idxmax()
Out[5]: 
NOC
USA    1984
URS    1980
dtype: int64