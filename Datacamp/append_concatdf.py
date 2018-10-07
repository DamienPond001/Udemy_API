
# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)
#ignore_index resets the index, else the indices from the original dfs are placed on top of one another


# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max, weather_mean], axis=1)
#axis=1 means concat horizontally (this does something similar to a full outer join)
         Max TemperatureF  Mean TemperatureF
    Apr              89.0          53.100000
    Aug               NaN          70.000000
    Dec               NaN          34.935484
    Feb               NaN          28.714286
    Jan              68.0          32.354839
    Jul              91.0          72.870968
    Jun               NaN          70.133333
    Mar               NaN          35.000000
    May               NaN          62.612903
    Nov               NaN          39.800000
    Oct              84.0          55.451613
    Sep               NaN          63.766667
    
for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns) #names sets the column names
    
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis='columns') #same as axis=1

# Print medals
print(medals)


#using multi level indexes:
for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, axis='rows', keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)
                            Total
           Country               
    bronze United States   1052.0
           Soviet Union     584.0
           United Kingdom   505.0
           France           475.0
           Germany          454.0
    silver United States   1195.0
           Soviet Union     627.0
           United Kingdom   591.0
           France           461.0
           Italy            394.0
    gold   United States   2088.0
           Soviet Union     838.0
           United Kingdom   498.0
           Italy            460.0
           Germany          407.0
           
# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
#A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])

# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)
                             Units
             Company               
    february Acme Coporation     34
             Hooli               30
             Initech             30
             Mediacore           45
             Streeplex           37
    january  Acme Coporation     76
             Hooli               70
             Initech             37
             Mediacore           15
             Streeplex           50
    march    Acme Coporation      5
             Hooli               37
             Initech             68
             Mediacore           68
             Streeplex           40
# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])