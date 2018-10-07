#pivot tables aggregate data with duplicate indices

  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index = 'weekday', columns = "city")

# Print by_city_day
print(by_city_day)
            signups        visitors       
    city     Austin Dallas   Austin Dallas
    weekday                               
    Mon           3      5      326    456
    Sun           7     12      139    237
    
    # Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)
             city  signups  visitors
    weekday                         
    Mon         2        2         2
    Sun         2        2         2

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index = "weekday", aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)
             signups  visitors
    weekday                   
    Mon            8       782
    Sun           19       376

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index = "weekday", aggfunc=sum, margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)
             signups  visitors
    weekday                   
    Mon            8       782
    Sun           19       376
    All           27      1158