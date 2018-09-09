o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')
#This will handle 1-to-1, many-to-1 and many-to-many merges