names = [{'id':1,'name':'Paul'},{'id':3,'name':'Pete'},{'id':2,'name':'Jake'}]
connect =[(1,2),(2,3)]

key_value = [keys,'value is - {}'.format(value) for dicts in names for keys in dicts for value in dicts.values()]