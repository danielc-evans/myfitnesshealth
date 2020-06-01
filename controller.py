import SQLStatements


#create tables and database
SQLStatements.createDB()
SQLStatements.createUserTable()
SQLStatements.createFoodTable()
SQLStatements.createExerciseTable()
SQLStatements.createweightChangeTable()

# Read Python File for Application Functions
exec(open('login.py').read())


