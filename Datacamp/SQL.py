SELECT * FROM table

SELECT COUNT(*) FROM table
#counts number of rows

SELECT DISTINCT row FROM table
#selects unique entries in row

SELECT COUNT(row) FROM table
#counts non-null entries

SELECT COUNT(DISTINCT row) FROM table
#returns count of distinct entries

SELECT * FROM table
WHERE column_value = 'some_value'  #Use boolean operators, note that <> is !=

SELECT * FROM table
WHERE column1 = 'some_value' AND/OR column2 > some_value; 

SELECT * FROM table
WHERE column BETWEEN value1 AND value2;
#Returns a range (inclusive) 

SELECT * FROM table
WHERE column IN ('...', '....', '....')
#use this instead of multiple ORs

SELECT * FROM table
WHERE column IS NULL\IS NOT NULL
#filter column on null\not null values

SELECT * FROM table 
WHERE column LIKE 'Data%'
# % wildcard matches none, one or many

SELECT * FROM table 
WHERE column NOT LIKE 'Data%'
# % wildcard matches none, one or many. Here we return all entrie that DON'T match

SELECT * FROM table 
WHERE column LIKE 'Data_'
# _ wildcard matches a single char


###AGGREGATION####

SELECT SUM(column) FROM table #AVG, MIN, MAX

SELECT (col1 + col2)*3 AS new_col FROM table #Note: (3/2) = 1, (3.0/2.0) = 1.5

#Can combine aggregations with arithmetic


####ORDERING####
SELECT column FROM table
ORDER BY col1 DESC

#NOTE comes after WHERE clauses


###GROUPING###

SELECT col1, COUNT(col2) FROM table
GROUP BY col1
#NOTE can't SELECT a column that isn't the GROUP BY, unless we aggregate it


###HAVING###

SELECT column FROM table
HAVING AVG(col1) > ...

###FULL EG###
SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross FROM films
WHERE release_year > 1990
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY avg_gross DESC

SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross FROM films
GROUP BY country
HAVING COUNT(title) > 10
ORDER BY country
LIMIT 5