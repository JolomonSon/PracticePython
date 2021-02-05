'''
Strings and Variables
name = "John Solomon"
length = len(name)                                                    
fname = name[0:4]
fna = "My first name is "
nam = "My name is "
print(nam+name+'\n'+fna+fname)
        Data Types
#Lists
names = ['Paul','Jethro','Samson','Delilah']
print(names[3]+' Killed Samson')
print('These are the names of my friends'+names)
#Tuples
name = tuple(('John','Pete','Dave','Paul'))
print(name)
print(num)
#Sets
cutleries = {'spoons','forks','cups','knives'}
cutleries.add('plates')
cutleries.update(['bowl','mugs'])
#The difference between update and add is the first(update) refers to addition of more than one data into the set while the latter,
is specifically for one data
print(cutleries)
#Dictionaries
cars = {
    'name':'Sienna',
    'brand':'Toyota',
    'color':'silver and white',
    'weight':'800g',
    'year':2015
}
name = cars.get('name')
cars['year'] = 2018
print(name)
print(cars['year'])
print('Keys','\t\t\t','Values')
print('-----','\t\t\t','-------')
for x in cars:
    print(x,'\t\t\t',cars[x])
if 'color' in cars:
    _color = cars['color']
    _name = cars['name']
    print('I have a ',_color,' ',_name)
cars['size'] = 'Large'
_length = len(cars)
_myObject = cars
print('The Length of my object \n',_myObject,'\n.. is ',_length)
print(_myObject.clear())
Differences between:
     List                               Tuples                             Set                  Dictionaries                   
Uses Square brackets[]                Uses Circle Brackets()       Uses Curly Brackets{}        Use Curly Braces {}
Have Indexed                          Unindexed                    Unindexed                    Unindexed
e.g listName[3]
It is Mutable(Changeable)             Immutable                    Mutables                     Mutable andthey are key value pairs
Conditional Statements                                                                                              e.g _cars = {'name':'Sienna','brand':'Toyota'}etc
#If Else...
name = input("Enter your name\n>>")
age = input("Enter your age\n>>>")
if (age <= 17):
    _name = "Hey ",name
    print(_name,'you are not eligible to vote and be voted for')
elif (age >= 18):
    print(_name,'you are eligible to vote and be voted for')
else:
    print('Invalid age')
Loops
#While Loop
print("Welcome to Jay's Food Spot")
name = str(input("Enter your name please\n>> "))
print("Hey",name,"What would you like Order")
items = {'1':"Fries and Egg",'2':"Noodles and Sausage",'3':"Rice and Chicken",'4':"Sharwama and Suya"}
prices = {'1':"#600",'2':"#500",'3':"#700",'4':"#400"}
for x in items:
    print(x,' ',items[x])
print('..Contact our website for other informations\n')
totalOrder = 1
while totalOrder < 5:
    print("TotalOrder is ",totalOrder)
    order = input('Select Order by selecting numbers\n>> ')
    if (order == '1'):
        print('Order','\t\t\t','Price')
        print(items['1'],"\t\t\t",prices['1'])
    elif(order == '2'):
        print('Order','\t\t\t','Price')
        print(items['2'],'\t\t\t',prices['2'])
    elif(order == '3'):
        print('Order','\t\t\t','Price')
        print(items['3'],'\t\t\t',prices['3'])
    elif(order == '4'):
        print('Order','\t\t\t','Price')
        print(items['4'],'\t\t\t',prices['4'])
    else:
        print("Invalid Option\nKindly Select Order Ranging from 1 to 4")
    checkout = input('Press Q to exit or A to Order more Items')
    totalOrder += 1
    if (checkout == 'A'):
        print("TotalOrder is",totalOrder)
        order = input('Select More Orders following number sequence\n>>')
        totalOrder += 1
        print("TotalOrder is",totalOrder)
        if (order == '1'):
            print('Ordered Twice...')
        elif(order == '2'):
            print(items['2'],'\t\t\t',prices['2'])#OMO THIS IS A HUGE PROJECT OH  I CAN ONLY DO IT WHEN I HAVE THE TIME
    elif (checkout == 'Q'):
        print('CheckOut Successful')
    else:
        print('Invalid Input\n',checkout)
Functions
def myNames():
    fName = input("Enter Your First Name Please\n>> ")
    sName = input('Enter Surname Name\n>> ')
    print('Welcome',fName,sName)
    
myNames()
Arrays
cars = ['Volvo','Benz','Honda']
print(cars)
cars.pop(0)
print(cars)
cars.remove('Benz')
print(cars)
cars.append('Toyota')
print(cars)
cars.sort()
Classes amd Objects

Modules
#Import Index2
from index2 import Toyota
car = Toyota['name'],' is the name of my father\'s new car'
print(car)
#Import Index2
from index3 import name
name()
#Directory(Index3)
import index3
direc = dir(index3)
print(direc)
Modules #Import Date
import datetime
date = datetime.datetime.now()
print(date.time)

Python JSON

Python RegEx

try.. except

try:
    fname = input("Enter your first name ")
    if fname == "John":
        sname = input("Enter your second name ")
        if sname == "Solomon":
            print(fname,sname)
    elif fname != "John":
        print('Wrong name')
except:
            print("An error occured\n>> names not defined")
File Handling

file = open('Todo List/python.txt')
    #Read whole File
#print(file.read())
    #Read first Line
print(file.readline())
    #Read first two lines e.t.c..
    #Looping a file
for x in file:
    print(x)
print(file.readline())

file = open('Todo List/demo.txt','w')
new_file = file.write('Jusrt appended this line')
new_file = file.write('File overwritten')
print(new_file.read())

Python MySQL

You need to download stuffs

So.. you'll have to stop here and continue with other tutorials

'''
import mysql.connector