import sqlite3

#Создание бд
DateBase = sqlite3.connect("DateBaseForTelegramBot.sql")

#Создание курсора(выполняет запросы к БД(SELECT, CREATE, INSERT...))
cursor = DateBase.cursor()

async def Create


cursor.execute("")





























# cursor.execute("Create TABLE History ("
#             "IdRecord INTEGER REFERENCES Record(Id) ON UPDATE CASCADE,"
#             "IdStudent INTEGER REFERENCES User(Id) ON UPDATE CASCADE,"
#             "Data VARCHAR(12),"
#             "Time VARCHAR(10))")
#
#
# cursor.execute("CREATE TABLE User ("
#             "Id INTEGER,"
#             "FIO VARCHAR(100),"
#             "PhoneNumber VARCHAR(12),"
#             "NumberRoom INTEGER,"
#             "Password varchar(32))")
#
# cursor.execute("CREATE TABLE Record ("
#             "Id INTEGER,"
#             "NumberWashingMachine INTEGER)")



