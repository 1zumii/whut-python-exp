import shelve

# https://www.ctolib.com/topics-43381.html
db = shelve.open('class-shelve')
sue = db['sue']
sue.pay = 10086
db['sue'] = sue
tom = db['tom']
tom.pay = 10010
db['tom'] = tom
db.close()
