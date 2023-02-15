# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "admin",
	password = "admin"
)

# Printing the connection object
print(mydb)


# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
 
# Creating a database with a name
# 'localhost' execute() method
# is used to compile a SQL statement
# below statement is used to create
# the 'localhost' database
cursor.execute("CREATE DATABASE localhost")