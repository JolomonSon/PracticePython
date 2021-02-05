names = [{'id':1,'name':'Paul'},{'id':3,'name':'Pete'},{'id':2,'name':'Jake'}]
connect =[(1,2),(2,3)]
new_connect = []
#for dicts in names:
    #print(dicts['id'])
for tuples in connect:
    for values in tuples:
        #print(values)
        new_connect.append(tuples)
for new_values in new_connect:
    print(new_values)
    