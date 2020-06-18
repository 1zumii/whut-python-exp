from makeDataBaseFile import readDB
from fileEnum import dbFileName

dataBase = readDB(dbFileName)
print(dataBase['sue'])
