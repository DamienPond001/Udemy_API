# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())

# Import pandas
import pandas as pd

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)

           Mean TemperatureF
    Month                   
    Jan            32.133333
    Feb                  NaN
    Mar                  NaN
    Apr            61.956044
    May                  NaN
    Jun                  NaN
    Jul            68.934783
    Aug                  NaN
    Sep                  NaN
    Oct            43.434783
    Nov                  NaN
    Dec                  NaN
           Mean TemperatureF
    Month                   
    Jan            32.133333
    Feb            32.133333
    Mar            32.133333
    Apr            61.956044
    May            61.956044
    Jun            61.956044
    Jul            68.934783
    Aug            68.934783
    Sep            68.934783
    Oct            43.434783
    Nov            43.434783
    Dec            43.434783
    
    # Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)