import sqlite3

# Creating a connection to the database
database = sqlite3.connect("DatabaseForTelegramBot.sql")

# Creating a cursor to execute queries
cursor = database.cursor()

# Function to create tables
async def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS History (
            IdRecord INTEGER REFERENCES Record(Id) ON UPDATE CASCADE,
            IdStudent INTEGER REFERENCES User(Id) ON UPDATE CASCADE,
            Data VARCHAR(12),
            Time VARCHAR(10)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            Id INTEGER,
            FIO VARCHAR(100),
            PhoneNumber VARCHAR(12),
            NumberRoom INTEGER,
            Password varchar(32)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Record (
            Id INTEGER,
            NumberWashingMachine INTEGER
        )
    """)

# Other functions and code related to database operations can be added here

# Function call to create tables (you'd call this function at an appropriate time)
# await create_tables()

# Committing changes and closing the database connection (consider doing this when you're done)
# database.commit()
# database.close()
