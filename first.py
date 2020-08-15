# المتغيرات
'''
x=x+' the best!'
x=x[:2]+x[ :6] +' cr7'+x[-1]
y='chicho',7
u='the','king' ,'is', "ronaldo",12,56
print (x)
# "some func[len,upper,lower,find,replace]        # دوال محجوزة
s= 'hicham '*6
'''
# format str
'''
first_name="hisham "
last_name="benghedier "

# message=first_name + "" + last_name +"is engineer"
msg=f'{first_name}{last_name}is a engineer'
print(msg)
'''
# list []  القوائم
'''
numbers =[5,10,15,20,25]
names = ['shisho','cr7','ronaldo']
print(numbers[2])
print(names[1])
numbers[0]='ali'
#_____________________ for القوائم مع
numbers =[5,10,15,20,25]
names = ['shisho','cr7','ronaldo']
for item in numbers: print(item)
for i in numbers: print(i)
#_____________________ mix
variables =[1,4,'shisho',8,'cr7',10]
print(variables[:])
اهم الدوا المستخدمة مع القوائم___________#
item =[1,5,3,10,15,12,25]
item.sort()
item.append(99)
item.remove(5)
item.clear()
rus=item.index(15)
f=item.copy()
print(item)
print(rus)
print(f)
انشاء اكثر من بعد للقائمة (مصفوفة)______________#
item=[[1,3,5],['shisho','cr7','ronaldo']]
print(item[1][2])
'''
# dictionaries{} القواميس
'''
# dict = {'s':'shisho','c':'cr7','r':'ronaldo'}
# print(dict['r'])
   اهم الدوال المستخدمة مع القواميس _____
# dict = {'s':'shisho','c':'cr7','r':'ronaldo'}
# print(dict.values())
# print(dict.keys())
# print(dict.__len__())
# print(dict.get('phone','this key is not exist'))
# dict.update({'age':20,'club':'RMD'})
# print(dict)
'''
# mutable & immutable المتغيرات و الغير متغيرات
'''
# immutables (str & int) ; mutables [List & dictionary]
name='shisho'
print(id(name))
name='cr7'
print(id(name))
# ______________
numbers =[5,10,15,20,25]
numbers[0]='hisham'
print(numbers)
'''
# tuples () "immutable variables" الصفوف
# inputs المدخلات
'''
__________________________1 ط
name =input()
print('my name is',name)
__________________________2 ط
number =input()
print('my favorite number is '+number)
__________________________3 ط
name1 =input('inter name1: ')
name2 =input('inter name2: ')
print(name1,name2)
__________________________4 ط
num1=int(input('inter num1: '))
num2=int(input('inter num2: '))
print(num1+num2)
'''
# الادات الشرطية if و else وelif
'''
if (a<y):
    print('ok')
    f= a+y
    print(f)
elif (a>y):
    print('no')
    r= a*y
    print(r)
else:
    print('oh shiiit..."x=y"!')
'''
#الشروط
'''
< ,> ,== ,<= ,>= ,~= 
'''
# for الادات الشرطية
'''
 1)العمل الاول:          
for i in range(7):
    print('shisho')
------------------------
# 1)العمل االثاني:
for item in x:
    print(item)
    '''
# breck and continue
'''
#              break:
for item in x:
    if item == 'cr7' :
        break
    print(item)
print (a)
-----------------------
#            continnue:
for item in x:
    if item == 'ali' :
        continue
    print(item)
print (a)
'''
# append and remove
'''
المتغيرات يجب ان تكون بين عارضتين وليس اقواس !!
print(x)
x.append("jo")
print(x)
x.remove("chicho")
print(x)
'''
#الادات الشرطية while
'''
while a < 10:
    print('stile working')
    a=a+1
print('finish')
'''
#for loops
'''
for i in range(3):
    print('shisho')
    for i in range(2):
        print('هشام')
'''
# Nested loop
'''
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            for h in range(10):
                                print(f'{a}{b}{c}{d}{e}{f}{g}{h}')
'''
#while loops
'''
while a < 10:
    print('stile working')
    a=a+1
    y=3
    while y < 5:
        print('please wait..!')
        y = y + 1
'''
#function الدالة
'''
  call        العمل الاول
  
def shisho() :
    y = 3
    a = 5
    k =a+y
    print(k)
shisho()
'''
'''
العمل الثاني   paramerts 

def shisho(u,h,c) :
    print(u,h,c)

shisho('the best','hisham','cr7')
'''
'''
العمل الثالث        args  

def shisho(*args) :
    print(args[1])

shisho('the best','hisham','cr7')
'''
'''
العمل الرابع      kwargs  

def shisho(**kwargs) :
    print(kwargs['u'],kwargs['r'])

shisho(u='the best',t ='hisham',r='cr7')
'''
'''
 return values   العمل الخامس
def returnXandY():
    x=17
    y=5
    return x,y
v_X,v_Y =returnXandY()
print(v_X,v_Y)
_________________________
def count(l) :
    even = 0
    odd = 0
    for i in l:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd

numbers = [1,4,5,7,6,15,8,10]
even,odd = count(numbers)
print('even: {} and odd: {}'.format(even,odd))
'''
'''
 return values   العمل السادس
funSum = lambda x,y: x+y
result = funSum(10,4)
print(result)
'''
# CLASS & OOP البرمجة الكائنية
'''
class car:
    speed= 0
    color= 'none'

    def info(self):
        print(self.speed,self.color)
    def info2(self):
        print(self.model,self.price)

#  call variables     مثال عن
bmw=car()
bmw.speed=240
bmw.color='black'
bmw.model=2019
bmw.price=100000
print(bmw.color)
'''
'''
#  call variables     مثال ثاني
camry=car()
camry.speed=250
camry.color='blue'
camry.model=2020
camry.price=200000
print(camry.color)
'''
'''
# call functions    مثال عن
bmw = car()
bmw.speed=240
bmw.color='black'
bmw.info()
'''
'''
# call functions مثال ثاني عن
camry=car()
camry.model=2020
camry.price=200000
camry.info2()
'''
'''
مثال عن علاقة بين var & fun  #
class car:
    speed= 0
    color= 'none'

    def info(self,accelerations):
        self.speed = accelerations
        print(self.speed)
    def info2(self,slowdown):
        self.speed = self.speed - slowdown
        print(self.speed)

bmw = car()
bmw.speed=240
bmw.color='black'
bmw.info(100)
bmw.info2(40)
'''
'''
طريقة بايثون بوضع المتغيرات داخل الدالة #
class car:
    speed= 0
    color= 'none'

    def info(self,v,c,m,p):
        self.speed = v
        self.color = c
        self.model = m
        self.price = p
        print(self.speed,self.model,self.color,self.price)

bmw = car()
bmw.info(220,'green',2010,10000)
'''
'''
#      constructor  دالة ال
class car:

    def __init__(self,v,c,m,p):
        self.speed = v
        self.color = c
        self.model = m
        self.price = p
        print(self.speed,self.model,self.color,self.price)

bmw=car(240,'black',2020,20000)
camry=car(200,'green',2018,10000)
'''
'''
# class variables & instant variables الفرق بين
class car:
    n=0
    def __init__(self,v,c,m,p):
        self.speed = v
        self.color = c
        self.model = m
        self.price = p
        car.n=car.n+1
        print(self.speed,self.model,self.color,self.price)

bmw=car(240,'black',2020,20000)
camry=car(200,'green',2018,10000)
print(car.n)
'''
'''
# class method     دالة الكلاس
class car:
    n=0
    def __init__(self,v,c):
        self.speed = v
        self.color = c
        car.n=car.n+1
        print(self.speed,self.color)
    @classmethod
    def cars_number(cls):
        print(cls.n)

bmw=car(240,'black')
camry=car(200,'green')

car.cars_number()
'''
'''
# multi class  اكثر من كلاس
class A:
    def printA(self):
        print('class A')
class B:
    def printB(self):
        print('class B')
class C:
    def printC(self):
        print('class C')

Obj_A=A()
Obj_A.printA()

Obj_B=B()
Obj_B.printB()

Obj_C=C()
Obj_C.printC()
'''
'''
# inheritance الوراثة
class A:                       # super class
    def printA(self):
        print('class A')
class B(A):                    # sub class
    def printB(self):
        print('class B')

Obj_A=A()
Obj_B=B()
Obj_B.printA()
'''
'''
# inheritance parent class
class A:                       # super class
    def printA(self):
        print('class A')
    def anatherFun(self):
        print('anather')
class B(A):                    # sub class
    def printB(self):
        print('class B')
        super().printA()
        super().anatherFun()

Obj_A=A()
Obj_B=B()
Obj_B.printB()
'''
'''
# multi inheritance اكثر من وراثة
class A:
    def printA(self):
        print('class A')
class B:
    def printB(self):
        print('class B')
class anather:
    def anather(self):
        print('anather class')
class C(A,B,anather):
    def printC(self):
        print('class C')
Obj_C=C()
Obj_C.anather()
Obj_C.printA()
'''
'''
#   constructor with inheritance 
class CAR:

    def __init__(self,v,c):
        self.speed = v
        self.color = c
        print(self.speed,self.color)
    def printCAR(self):
        print('print a CAR')

class BUS(CAR):

    def __init__(self,v,c):
        super().__init__(v,c)
    def printBUS(self):
        print('print a BUS')

car1=CAR(220,'red')
bus1=BUS(200,'black')
bus1.printCAR()
bus1.printBUS()
'''
'''
# inheritance "override" تجاوز
class A:                       # super class
    def printA(self):
        print('class A')
class B(A):                    # sub class
    def printA(self):
        print('class B')
class C(A):                    # sub class
    def printA(self):
        print('class C')

Obj_A=A()
Obj_A.printA()

Obj_B=B()
Obj_B.printA()

Obj_C=C()
Obj_C.printA()
'''
'''
# class int & str    اهمية 
 class int(): [__add__,__sub__,__eq__,,,,,,,,,,,,,]
 class str(): [ replace,finde,__len__,uper,,,,,,,,] 
'''
# import & random عشوائي
'''
import random

names = ['shisho','cr7','ronaldo','hisham','city']
numbers =[5,10,15,20,25]

students = random.choices(names,k=3)
results = random.choice(numbers)
print(students)
print(results)
'''
# exception  الاستثناء
'''
y= input('inter num1: ')
n= input('inter num2: ')
try:
    z=int(y)/int(n)
except Exception as ax:
    z='not defined..!'
print('result is:',z)
'''
# I/O files
'''
f = open('test.py','w')
f.write('i love ronaldo')
f.close()
#_____________________
f = open('test.py','a')
f.write(' \n my name is hisham\nshisho')
f.close()
#_____________________
f = open('test.py','r')
content = f.read() # or readlines ..
print(content)
f.close()
'''
try:
    # h=int(input('enter a name: '))
    # print(h)
    f = open('test.py','r')
    print(f.read())
except:FileNotFoundError
# except ValueError:
#     print('value error found...!')
#
# except FileExistsError:
#     print(f.read())