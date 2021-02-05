print('\t\tPythoning\t')
'''        #Calendar
import calendar
wkDays = calendar.weekheader(3)#This Specifies Mon Tue Wed e.t.c
oct2020 = calendar.month(2020,10,3)
cal2020 = calendar.calendar(2020)
#print("2020 Calender\n",cal2020)
#print(calendar.monthcalendar(2020,3))
        #Casting - Basically changing a datatype to another datatype e.g an integer to a float or a string
    #Datatypes
int = -1
intFloat = float(int)
intStr = str(int)
intBool = bool(int)
#print(intBool) '''
'''        #Lists  ( [], Ordered, Mutable)
lis = [1,2.5,3,99,'fred',[1,'dre',1.4]]
new = [3,2,1,3,4]
#print(lis[3][2])
lis.append('Dave')#Adding to the last element of the list
lis.insert(0,2.3)#Customized type of append
lis.remove(2.5)
lis.reverse()#Basically in a reverse/opposite/descending order of the original sequence of the list.
new.sort()#Basically an ascending order of the supposed shuffled list.
    #Index Slicing and Striding
list = [0,1,2,3,4,5,6,7,8,9,10]
name = ["John Solomon"]
#print(list[:3])#Slicing Strings - (The First three digits)
fName = name[0][0:4]
lName = name[0][5:12]
#print(list[0:6:2])#Striding basically specifies the interval of numbers you want to display if is a negative stride, it goes in a descending order.
list = [0,1,2,3,4,5,6,7,8,9,10]
numSize = 3
#for num in range(len(list)-(numSize-1)):
    #print(list[num:num+numSize])
        #Joining and Splitting Functions
    #Splitting
names = "John Solomon Olorunfemi"
splittedNames = names.split(" ")
#print(splittedNames)
    #Joining
joinedNames = ' =>'.join(splittedNames)
#print(joinedNames)  '''
'''      #Tuples in Python  ( (), Ordered, Immutable)
creditCard1 = (123456789, 'Pete Dave', '10/19', 123)
creditCard2 = (987654321, 'Paul Don' ,'11/20', 321)
creditCards = [creditCard1, creditCard2]
#acctNo1,acctName1,expDate1,cvv1 = creditCard1
#acctNo2,acctName2,expDate2,cvv2 = creditCard2#Basically giving variable names to the values of a tuple
#print('Account Number - ',acctNo2,'\nAccount Name - ',acctName2,'\nExpiry Date - ',expDate2,'\nCVV - ***')
for acctNo,acctName,expDate,cvv in creditCards:
    print('Account Number - ',acctNo)
    print('Account Name - ',acctName)
    print('Expiry Date - ',expDate)
    print('CVV - ***',cvv)
    print()
Basically line 47-49 and 50-55 does the same thing. (47-49) gives the values of the tuple variable names to access them instead of using their index value
(50-55) loopds through the tuple directly allocating their values in the loop and printing them out. [Line 47-49 is preferrable] '''
'''        #Sets in Python  ( {}, Unordered, Mutable)
series1 = {'The Gifted','Shameless','Charmed','Empire'}
series2 = {'Power', 'Game of Thrones', 'Empire'}
series2.add('Money Heist')
seriesUnion = series1.union(series2)#Basically the combination of the two sets.
seriesIntersection = series1.intersection(series2)#Basically similar values in both sets.
seriesDifference1= series1.difference(series2)#values in series1 that are not in series2.
seriesDifference2 = series2.difference(series1)#values in series2 that are not in series1.
print(seriesDifference2)
lists = [144,"Paul",132,'Paul',111,"Pete"]
listSet = set(lists)#Basically casting a list to a set
setList = list(listSet)
lists = setList
#print(lists)'''
'''        #Dictionaries DataStructure ( {} Ordered Mutable)
fruits = {'Banana':2,'Orange':3,'Pineapple':4,'Lemon':0,'Grape':1,'Paw paw':3}
fruits['Apple'] = 3
fruits.pop('Lemon')
fruits.clear()#Empties the dictionary
#print(fruits['Banana'],'- Bananas')
#print(fruits.get('Paw paw'),'- Paw paw')
staff = {
    'teachingStaff':{
        'Paul Philip':{'phone':'+2348198765434','email':'paul.philip@school.com','nationality':'Nigerian'},
        'Pete Jack':{'phone':'+23481987654345','email':'pete.jack@school.com','nationality':'Canadian'},
        'Jacob Jones':{'phone':'+2348198765436','email':'jacob.jones@school.com','nationality':'Portugese'}
        },
    'nonTeachingStaff':{
        'Jane Joseph':{'phone':'+2348198765431','email':'jane@school.com','nationality':'Nigerian'},
        'Rose Pauline':{'phone':'+2348198765432','email':'Rose@gmail.com','nationality':'Ghanian'},
        'Peace Favour':{'phone':'+2348198765433','email':'paul@gmail.com','nationality':'Zambian'},
        }
}
#print(staff['teachingStaff']['Paul Philip'])
print(list(staff['teachingStaff'].items()))
print()
print(list(staff['nonTeachingStaff']['Jane Joseph'].keys()))
print()
print(list(staff['teachingStaff'].values()))'''
'''        #Mutability in Python
print("Mutable DataTypes\nData types that can change (mutate - change)able i.e change-able")
print("e.g\nList\nDictionaries{The keys are immutable while the values are mutable}\nOrdered Dictionaries\nIntegers\n ")
print("Immutable DataTypes\nData types that cannot change (immutate - unchange)able i.e unchange-able")
print("e.g\nTuples\nSets\nStrings\n")
tuples = (2,3,[1,4,2])
print(tuples[2][2])'''
'''        #List Comprehensions Python
persons = ['Pete','Paul','Josh','Posh']
#print([person+' is my friend' for person in persons])
moviesAndRatings = {'Game of Thrones':8,'Power':7,'Money Heist':8,'Shameless':8,'Whiskey Cavalier':2,'Empire':7,'Six':3}
avgMovies = []
for movies in moviesAndRatings:
    if (moviesAndRatings[movies] < 5):
        avgMovies.append(movies)
print('Average Movies')
print(avgMovies)
premiumMovies = [movies for movies in moviesAndRatings if moviesAndRatings[movies] > 5]#List Comprehension(I call it ONE-LINE-FOR-LOOP)
print('Premium Movies')'''
'''        #Regular Expressions - So far RegExp checks for matches found in a string(what searching basically does) these searches are based on a pattern.
    #Email address Text Scraper
import re
person = "A person from people@comp-any.com is here"
group = "A group from oneGroup@community.net Another group from allGroup@community"
personPattern = re.compile("[a-zA-Z0-9\,._-]+\@[a-zA-Z0-9\,._-]+\.[a-zA-Z0-9\,._-]+")
groupPattern = re.compile("[a-zA-Z0-9\.,-_]+@[a-zA-Z0-9\.,_-]+\.[a-zA-Z0-9\,._-]+")
personResult = personPattern.search(person)
groupResult = groupPattern.findall(group)#Findall method basically works with finding similar patterns in the same text
print(personResult)
print(groupResult)
        #Datetime Module with Python
import datetime
import pytz #For timezone sha..
    #Date datetime.date()#(YYYY-MM-DD)
todayDate = datetime.date.today()#(YYYY, MM, DD)
myBirthDate = datetime.date(2002,10,16)
noOfDays = (todayDate-myBirthDate).days
myAge = (todayDate.year)-(myBirthDate.year)
tenDays = datetime.timedelta(days=10)
datetimeToday = datetime.datetime.now(tz=pytz.UTC)
datetimePacific = datetimeToday.astimezone(pytz.timezone('US/Pacific'))
    #Time datetime.time()#(h:m:s:ms)
    #DateTime datetime.datetime() #(YYYY-MM-DD h:m:s:ms )
currentTime = datetime.datetime.now()
tenHours = datetime.timedelta(hours=10)
print('Today Date',todayDate)
print('My Birth Date',myBirthDate)
print('Number of my Days',noOfDays)
print('My Age',myAge)
print('What is the time? - ',currentTime)
print('Ten Hours from now will be - ',currentTime+tenHours)
print('Ten Days from now will be - ',todayDate+tenDays)
print(datetimeToday)
print(datetimePacific)
for tz in pytz.all_timezones:
    print(tz)
print(datetime.datetime.now())
        #String Formatting
#strftime (f=formatting)
print(datetimePacific.strftime('%B, %d, %Y'))
print(datetime.datetime.now().strftime('%B,%d,%Y'))
#strptime (p=parsing)
print(datetime.datetime.strptime('February 02, 2021','%B %d, %Y'))
'''        #Web Scrapping with Python
print('Beautiful Soup\nRequests\nPandas')
''' Questions in line 166 and line 168-173
#Zip Functions in Python
listInt = [1,2,3,4,5,6]
listStr = ['one','two','three','four','five','six']
shoppingList = {'fruits':['Apple','Orange','Grape','Banana'],'prices':[300,150,250,200],'counts':[5,20,15,10]}
fruits = ['Apple','Orange','Grape','Banana']
prices = [300,150,250,200]
counts = [5,20,15,10]
zippedList = list(zip(listInt,listStr))
unZippedList = list(zip(*zippedList))
#text = [(count,fruit,'costs',price) for (fruit,price,count) in (shoppingList['fruits'],shoppingList['prices'],shoppingList['counts'])]
text = [(count,fruit,'costs','$',price) for (fruit,price,count) in zip(fruits,prices,counts)]
sentences= []
for (fruit,price,count) in zip(fruits,prices,counts):
    fruit,price,count = str(fruit),str(price),str(counts)
    sentence = count+fruit+'s costs'+'$'+price+'.'
    sentences.append[sentence]
print(sentences)
print('Zipped List',zippedList)
print('Un Zipped List',unZippedList)
#print(text)'''
        #Project Tic Tac Toe
print('ProjectTicTacToe')
print('Check ticTacToe.py')

        #Project Twillo Texting app
print('ProjectTwilloTextingApp')
print('Check twilioTextingApp.py')

        #Project To-Do List app
print('ProjectToDoListApp')
print('Check toDoListApp.py')

