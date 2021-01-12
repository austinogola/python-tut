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

numz=[20,30,40,60]
numz2=list(filter(lambda n:n%3==0,numz))
print(numz2)




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





