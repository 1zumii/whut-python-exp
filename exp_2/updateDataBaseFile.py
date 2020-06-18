from makeDataBaseFile import readDB, writeDB
from fileEnum import dbFileName

dataBase = readDB(dbFileName)
dataBase['sue']['pay'] *= 1.1
dataBase['tom']['name'] = 'Tom Tom'
writeDB(dataBase)
