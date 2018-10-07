#Used for mereging when there is an ordering (eg dates)

# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin, houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus','_hus'], fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)

#Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge 
#values in order using the on column, but for each row in the left DataFrame, 
#only rows from the right DataFrame whose 'on' column values are less than the 
#left value will be kept.
#This function can be used to align disparate datetime frequencies without having to first resample.

oil.head()
        Date  Price
0 1970-01-01   3.35
1 1970-02-01   3.35
2 1970-03-01   3.35
3 1970-04-01   3.35
4 1970-05-01   3.35

auto.head()
    mpg  cyl  displ   hp  weight  accel         yr origin  \
0  18.0    8  307.0  130    3504   12.0 1970-01-01     US   
1  15.0    8  350.0  165    3693   11.5 1970-01-01     US   
2  18.0    8  318.0  150    3436   11.0 1970-01-01     US   
3  16.0    8  304.0  150    3433   12.0 1970-01-01     US   
4  17.0    8  302.0  140    3449   10.5 1970-01-01     US   

                        name  
0  chevrolet chevelle malibu  
1          buick skylark 320  
2         plymouth satellite  
3              amc rebel sst  
4                ford torino


# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

          mpg  cyl  displ  hp  weight  accel         yr  origin             name  \
    387  27.0    4  140.0  86    2790   15.6 1982-01-01      US  ford mustang gl   
    388  44.0    4   97.0  52    2130   24.6 1982-01-01  Europe        vw pickup   
    389  32.0    4  135.0  84    2295   11.6 1982-01-01      US    dodge rampage   
    390  28.0    4  120.0  79    2625   18.6 1982-01-01      US      ford ranger   
    391  31.0    4  119.0  82    2720   19.4 1982-01-01      US       chevy s-10   
    
              Date  Price  
    387 1982-01-01  33.85  
    388 1982-01-01  33.85  
    389 1982-01-01  33.85  
    390 1982-01-01  33.85  
    391 1982-01-01  33.85 
# Resample merged: yearly
yearly = merged.resample('A', on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

                      mpg  Price
    Date                        
    1970-12-31  17.689655   3.35
    1971-12-31  21.111111   3.56
    1972-12-31  18.714286   3.56
    1973-12-31  17.100000   3.56
    1974-12-31  22.769231  10.11
    1975-12-31  20.266667  11.16
    1976-12-31  21.573529  11.16
    1977-12-31  23.375000  13.90
    1978-12-31  24.061111  14.85
    1979-12-31  25.093103  14.85
    1980-12-31  33.803704  32.50
    1981-12-31  30.185714  38.00
    1982-12-31  32.000000  33.85

# print yearly.corr()
print(yearly.corr())

                      mpg  Price
    Date                        
    1970-12-31  17.689655   3.35
    1971-12-31  21.111111   3.56
    1972-12-31  18.714286   3.56
    1973-12-31  17.100000   3.56
    1974-12-31  22.769231  10.11
    1975-12-31  20.266667  11.16
    1976-12-31  21.573529  11.16
    1977-12-31  23.375000  13.90
    1978-12-31  24.061111  14.85
    1979-12-31  25.093103  14.85
    1980-12-31  33.803704  32.50
    1981-12-31  30.185714  38.00
    1982-12-31  32.000000  33.85