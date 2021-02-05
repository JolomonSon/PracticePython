users = [{'id':1,'name':'Paul'},{'id':3,'name':'Pete'},{'id':2,'name':'Jake'}]
connect =[(1,2),(2,3)]
name = []
id_s = ["ID is {}".format(value) for dicts in users for value in dicts.values() if type(value) is int]
name = ["Names are {}".format(value) for dicts in users for value in dicts.values() if type(value) is str]
for tuples in connect:
    if tuples == id:
        print(id,'-',name)
    else:
        print(id,'-',name)