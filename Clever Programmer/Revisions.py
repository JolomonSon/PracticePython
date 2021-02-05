        #Calandar
print('\tCalendar')
import calendar
generalCalendar = calendar.calendar(2020)
octoberCalendar = calendar.month(2020,10,3)
print(generalCalendar)
print(octoberCalendar)
        #Casting in DataTypes
print('\tDataType Casting')
_int,_float,_str,_bool = 5,5.5,'five',True
intToStr = str(_int)
floatToInt = int(_float)
strToBool = bool(_str)
boolToFloat = float(_bool)
print(_int,'Integer to String',intToStr)
print(_float,'Float to Integer',floatToInt)
print(_str,'String to Boolean',strToBool)
print(_bool,'Boolean to Float',boolToFloat)
        #Lists
print('\tLists')
names = ['Pete','Jones','Paul','Dave']
names.remove('Dave')
names.append('Josh')
names.insert(0,'Posh')
names.sort()
print(names)
print(names[2],'is my friend')
    #Index Slicing and Striding
print('\tIndex Slicing and Striding')
friends = ['Job','Paul','Silas',['Pete','Paow','Posh'],'Fred','Josh','Kane']
numbers = [0,1,2,3,4,5,6,7,8,9,10]
#oddNumbers = 'Odd Numbers from 1-10',numbers[0:10:]
evenNumbers = 'Even Numbers from 1-10',numbers[0:10:2]
firstThreeFriends = friends[0:3]
secondTwoFriends = friends[3][0:2]
fiveFriends = [firstThreeFriends+secondTwoFriends]
print(fiveFriends)
#print(oddNumbers)
print(evenNumbers)
        #Joining and Splitting Functions
    #Splitting
names = "John Solomon Olorunfemi"
splittedNames = names.split(" ")
print(names)
print(splittedNames)
    #Joining
joinedObject = ("=>").join(splittedNames)
print(joinedObject)
        #Tuples
print('\tTuples')
creditCard = ('123****123','John Doe','08/20','***','Access Bank')
cardNumber,acctName,expDate,cvv,bank = creditCard
print('Bank-',bank,'\nAccount Holder-',acctName,'\nCard Number-',cardNumber,'\nExpiry Date',expDate,'\nCVV-',cvv)
        #Sets
print('\tSets')
library1 = {'Origin','Alligent','Insurgent','Cryptography','Jumanji'}
library2 = {'Canes','Jumanji','Pretty Little Liars','Cryptography'}
print(library1.union(library2))
print(library1.intersection(library2))
print(library1.difference(library2))
print(library2.difference(library1))
'''        #Dictionaries
print('\tDictionaries')
seniorClass = {'SS1':18,'SS2':15}
juniorClass = {'JS1':32,'JS2':19,'JS3':22}
seniorClass['SS3'] = 13
print([keys+'-'+values for keys,values in seniorClass.keys(),seniorClass.values()])'''
        #List Comprehension
print('List Comprehension')
people = ['Posh','Pete','Paul','Pane','Paer']
bestFriends = [bFriends+' is my best Friend' for bFriends in people[0:2]]
print(bestFriends)
        #Regular Expressions
    #Email address Text Scraping
import re
text = 'My name is John Solomon and my email address is jolomonson@gmail.com i am 17 years old.'
myEmailPattern = re.compile("[a-zA-Z0-9\,._-]+@[a-zA-Z0-9\,._-]+\.[a-zA-Z0-9\,._-]+")
myEmailResult = myEmailPattern.search(text)
print(myEmailResult)
'''        #Datetime
    #datetime.date

    #datetime.time

    #datetime.datetime'''

