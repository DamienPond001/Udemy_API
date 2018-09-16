#EG:
   id treatment gender  response
0   1         A      F         5
1   2         A      M         3
2   3         B      F         8
3   4         B      M         9

df.pivot(index = "treatment", columns = "gender", values = "response")
#pivot
gender     F  M
treatment      
A          5  3
B          8  9

#Not specifying the values will pivot all columns