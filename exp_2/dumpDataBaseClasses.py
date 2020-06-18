import shelve

db = shelve.open('class-shelve')
for k, v in db.items():
	print(k)
	print("\t{}\n\t{}\n\t{}\n\t{}".format(v.name,v.age,v.pay,v.job))
db.close()
