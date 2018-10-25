# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')# Create an engine to the census database
engine = create_engine('mysql+pymysql://'+'student:datacamp'+'@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/'+'census')

# Print table names
print(engine.table_names())

#Reflection is the process of reading the database and building the metadata 
#based on that information. It's the opposite of creating a Table by hand and 
#is very useful for working with existing databases. To perform reflection, you need to import 
#the Table object from the SQLAlchemy package. Then, you use this Table object to read 
#your table from the engine and autoload the columns. Using the Table object in this manner 
#is a lot like passing arguments to a function. For example, to autoload the columns with the engine, 
#you have to specify the keyword arguments autoload=True and autoload_with=engine to Table().

# Import Table
from sqlalchemy import Table, MetaData

metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))

# Print census table metadata
print(repr(census))