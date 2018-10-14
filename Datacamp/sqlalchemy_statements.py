# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()

# Build select statement for census table: stmt
stmt = "SELECT * FROM census"

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

#ALTERNATIVELY
# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(connection.execute(stmt).fetchall())

#
#Recall the differences between a ResultProxy and a ResultSet:
#
#    ResultProxy: The object returned by the .execute() method. It can be used in a variety of ways to get the data returned by the query.
#    ResultSet: The actual data asked for in the query when using a fetch method such as .fetchall() on a ResultProxy.

#This separation between the ResultSet and ResultProxy allows us to fetch as much or as little data as we desire.

results = connection.execute(stmt).fetchall()

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])