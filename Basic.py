'''Basic data Types==>int  float  str  list  bool dict  sets  tup'''
'''Ordered-->can be indexed[x] or sliced[x:y]==>str list tup'''

import random

'''String methods'''
strr='This is a string'
#Capitalize,lower,upper,islower(LOWER ONLY),isupper(UPPER ONLY),isalpha(ALPHABET ONLY),isnumeric(NUMS ONLY)
#count---->strr.count('i')--->3
#endswith--->strr.endswith('g')-->True    strr.endswith('k)-->False    strr.startswith('k')
#find---->strr.find('stri')----->10       strr.find('is')--->2       SAME AS INDEX-->strr.index('stri')-->10
#replace--->strr.replace("i",'q')---->Thqs qs a strqng
#rfind and rindex--->Like find and index but for LAST value instead of FIRST
#split---->strr.split(" ")---->['This', 'is', 'a', 'string']
#strip--->" This is a string  ".strip()--->'This is a string'  lstrip(ONLY LEFT SIDE)  rstrip(ONLY RIGHT SIDE)
#translate--->table=strr.maketable("s","q")  strr.translate(table)---->Thiq iq a qring


'''String formatting--->format and f strings'''
# name='Austine Ogola'
# age=2200
# print('My name is {} and I am {} years old'.format(name,age))
# print('My name is {b} and I am {a} years old'.format(b='Austine',a=2222))
# print(f'My name is {name} and I am {age} years old')


'''List methods'''
mylist=[12,'boys','kittens','234',45,68,'Mary',90]
another_list=[50,'John',600,1000,45,68,'Mary','bus']
#append,extend,pop,remove,
#sort,reverse==>INPLACE


'''dict methods'''
#keys,values,items


#multiplevalue assignment
name,age='Austine',566

del age

#Data types
#Strings,,Numbers(int and float,complex),,Lists,,Sets,,Tuples,,Dictionaries,,bool


#Functions
def greet(name,greeting):
     print(f'{greeting} {name}')

#Positional and Keyword
'''
positional arguments--->greet('Austin','How are you')
keyword arguments--->greet(greeting='How are you',name='Austin')
If mixed,positional has to come first--->greet('Austin',greeting='How are you')
'''
#Arbitary arguments--->When we dont know number of arguments
def showNames(*names):
    for name in names:
        print(name)

#lambda Functions---->anonymous nameless functions.Usuallly made for arguments for higher-order fxns
double=lambda x:x**5
#print(double(45))

#filter(),,map()
#filter()---->Used to filter out items in a list based on a condition accepts 2 arguments-->a fxn and a list
my_list=[6,9,12,15,18,21,24]
new_list=list(filter(lambda x:x%2==0,my_list))  #-->new_list=[x for x in my_list if x%2==0]
#print(new_list)

#map()---->Used to map items--> accepts 2 arguments-->a fxn and a list
newer_list=list(map(lambda x:x**4,my_list))   #newer_list=[x**2 for x in my_list]
#print(newer_list)





#File IO
# f=open("C:/Coding/JAVASCRIPT/Python/test.txt",'r')

#Reading a file
'''for line in f:
    print(line)'''
#print(f.read())

#Writing a file(Creates new if it doesnt exist)
# f=open("C:/Coding/JAVASCRIPT/Python/test.txt",'w')
# f.write('It replaces the text in file with this')

# f=open("C:/Coding/JAVASCRIPT/Python/test.txt",'a')
# f.write('It adds this text to the existing text file')

# f=open("C:/Coding/JAVASCRIPT/Python/test.txt",'r')
# print(f.read())

# #Create a new file
# g=open('test2.txt','x')


# f.close()


#List comprehensions
# list1=[10,20,30,40,50,60,70,80,90,100]
# list2=[i*3 for i in list1]
# list3=[i for i in list1 if i>50]
# list4=[i*2 if i<50 else i**2 for i in list1]
# list5=[i**5 for i in list1 if i>50 if i>70]


#String Methods
string='This is a string'
#capitalize,,endswith,,lower,,upper,,
#string1=string.count('i')--->3
#string.center(30,'k')--->kkkkkkkThis is a stringkkkkkkk







'''tuples methods'''
#count and index


'''set methods'''
#add,clear,pop,remove,union,

'''enumerate'''
word="abcdefg"
#for i in enumerate(word):------>(1,'a')....(6,'g')
    #print(i)


'''random'''
new_list=[1,2,3,4,5,6,7,8,9,10]
#randomint(x,y)
#shuffle(INPLACE)---->shuffle(new_list)---->new_list---->[5, 1, 2, 3, 8, 4, 10, 7, 6, 9]


'''list comprehension'''
#new_list2=[i*2 for i in new_list]
#new_list2=[i*2 for i in new_list if i<6]
#new_list2=[i*2 if i<6 else i**2 for i in new_list]


'''lambda expressions'''
#One time use functions with no defined name
def square(x):
    return x**2

def check_even(x):
    return x%2==0

my_nums=[20,25,30,35,40,45,50,55,60]

#for item in map(square,my_nums):---->400,624,900,1225,1600,2025,2500,3025,3600
    #print(item)

#my_nums_squared=list(map(square,my_nums))---->[400, 900, 1600, 2500, 3600]

#for n in filter(check_even,my_nums):--->20,30,40,60
    #print(n)

#def square(x):-------->square=lambda x:x**2
    #return x**2

'''Using lambda'''
newwww=map(lambda x:x**2,[1,2,3,4,5])
#print(list(newwww))

'''OOP'''
class Dog():
    def __init__(self,value,age,time):
        self.value=value
        self.age = age
        self.time = time

    def bark(self):
        print(f'The {self.value} dog is barking')

dog=Dog('German',400,'kkkkkk')
dog.bark()

"""Inheritance"""
# class Cat(Dog):
#     def __init__(self):
#         Dog.__init__(self)

"""Polymorphism-->different objects from same class or diff classes share same method name with diff. fxnality"""


"""Decorators--->adding/removing extra fxnality to fxns"""
def func():
    return 1

def hello():
    return 'hello'


