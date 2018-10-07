# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF',  'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9 #broadcasting

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = ['Min TemperatureC', 'Mean TemperatureC',  'Max TemperatureC']

# Print first 5 rows of temps_c
print(temps_c.head())


import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', index_col='DATE', parse_dates=True)

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008':, :]

# Print the last 8 rows of post2008
print(post2008.tail(8))
                  VALUE
    DATE               
    2014-07-01  17569.4
    2014-10-01  17692.2
    2015-01-01  17783.6
    2015-04-01  17998.3
    2015-07-01  18141.9
    2015-10-01  18222.8
    2016-01-01  18281.6
    2016-04-01  18436.5
    
# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)
                  VALUE
    DATE               
    2014-07-01  17569.4
    2014-10-01  17692.2
    2015-01-01  17783.6
    2015-04-01  17998.3
    2015-07-01  18141.9
    2015-10-01  18222.8
    2016-01-01  18281.6
    2016-04-01  18436.5
    
# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change()*100

# Print yearly again
print(yearly)
                  VALUE    growth
    DATE                         
    2008-12-31  14549.9       NaN
    2009-12-31  14566.5  0.114090
    2010-12-31  15230.2  4.556345
    2011-12-31  15785.3  3.644732
    2012-12-31  16297.3  3.243524
    2013-12-31  16999.9  4.311144
    2014-12-31  17692.2  4.072377
    2015-12-31  18222.8  2.999062
    2016-12-31  18436.5  1.172707
    
# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', index_col='Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', index_col='Date', parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')
#NOTE: similar add(), subtract(), divide() methods. These offer more flexibility than using standard +, -, / operators

# Print the head of pounds
print(pounds.head())