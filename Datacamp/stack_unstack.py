#stack does something similar to pivot using the indices
# Unstack users by 'weekday': byweekday

users = 
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12
       
byweekday = users.unstack(level = 'weekday')

# Print the byweekday DataFrame
print(byweekday)
           visitors      signups    
    weekday      Mon  Sun     Mon Sun
    city                             
    Austin       326  139       3   7
    Dallas       456  237       5  12
       
# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level = 'weekday'))
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
           Sun           139        7
    Dallas Mon           456        5
           Sun           237       12
           
# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level = "city")

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()