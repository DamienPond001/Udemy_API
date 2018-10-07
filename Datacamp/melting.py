#melting restores pivoted dfs

visitors = pd.melt(visitors_by_city_weekday, id_vars=['weekday'], value_name='visitors')
#id_vars specify columns to maintain
#value_names specify name of column containing the values

# Set the new index: users_idx
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)
visitors  signups
    city   weekday                   
    Austin Sun           139        7
    Dallas Sun           237       12
    Austin Mon           326        3
    Dallas Mon           456        5
# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)
        variable  value
    0  visitors    139
    1  visitors    237
    2  visitors    326
    3  visitors    456
    4   signups      7
    5   signups     12
    6   signups      3
    7   signups      5