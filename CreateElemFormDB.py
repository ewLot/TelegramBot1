import sqlite3

#Создание бд
DateBase = sqlite3.connect("DateBaseForTelegramBot.sql")

#Создание курсора(выполняет запросы к БД(SELECT, CREATE, INSERT...))
cursor = DateBase.cursor()

cursor.execute("")


# cursor.execute("CREATE TABLE History ("
#             "IdRecord INTEGER REFERENCES Record(Id) ON UPDATE CASCADE,"
#             "IdStudent INTEGER REFERENCES Student(Id) ON UPDATE CASCADE,"
#             "Data Text,"
#             "Time Text)")


