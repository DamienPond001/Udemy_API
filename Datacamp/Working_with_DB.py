# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


#Executing a query
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * from Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()


# Close connection
con.close()

#auto close connection
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()
    
    
#ALTERNATIVELY
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)