# li1 = [1,2,3,4,6,4,5,7,8,9]
# li2 = li1.copy()
# li1.clear()
# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
# print(lst.count('Cat'))
# lst.extend("Pravin")
# print(lst.index('Cat',1))
# lst.insert(0,'Dog')
# print(lst)
# print(lst.pop(0),lst)
# lst.sort(reverse=

# def get_count(num_list):
#     count = 0
#
#     # Write your logic here
#
#     for i in range(0, len(num_list) - 1):
#         if (num_list[i] == num_list[i + 1]):
#             count = count + 1
#
#         else:
#             continue
#     return count
#
#
# num_list = [1, 1, 5, 100, -20, -20, 6, 0, 0]
# print(get_count(num_list))


# Creating a string
# pancard_number = "AABGT6715H"
# # Length of the string
# print("Length of the PAN card number:", len(pancard_number))
# # Concatenating two strings
# name1 = "PAN "
# name2 = "card"
# name = name1 + name2
# print(name)
# print("Iterating the string using range()")
# for index in range(0, len(pancard_number)):
#     print(pancard_number[index])
#
# print("Iterating the string using keyword in")
# for value in pancard_number:
#     print(value)
# print("Searching for a character in string")
# if "Z" in pancard_number:
#     print("Character present")
# else:
#     print("Character is not present")
# # Slicing a string
# print("The numbers in the PAN card number:", pancard_number[5:9])
# print("Last but one 3 characters in the PAN card:", pancard_number[-4:-1])
# pancard_number[2] = "A"  # This line will result in an error, i.e., string is immutable
# print(pancard_number)


# passengers_list = ["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
# unique_passengers = set(passengers_list)
# li1 = list(unique_passengers)
# print(type(li1),f"/n {li1}")

# def transform(a = 2):
#     if a == 1:
#         return a +- 2
#     return a
#
# total = 1
#
# for x in [3,5,1]:
#     total = total + transform(x)

# print(total)
# flight_set = {500, 520, 600, 345, 520, 634, 600, 500, 200, 200}

# passengers_list = ["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
# unique = set(passengers_list)
# setA = {1,2,3,4,5,6}
# setB = {7,8,9,1,2,3}
# setC = setA|setB
# print(setC)
# print(f"common elements in the setA and setB: {setA&setB}")
# print(setA- setB)


# crew_details = {"Pilot": "Kumar","Co-pilot": "Raghav", "Head-Strewardess": "Malini", "Stewardess": "Mala"}
# for key,value in crew_details.items():
#     print(f"{key}: {value}")

# def proper_divisors(num):
#     Proper_divisors = []
#     for i in range(1,num):
#         if num%i==0:
#             Proper_divisors.append(i)
#         else:
#             continue
#     return Proper_divisors
#
# print(proper_divisors(220))

# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1
#
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()

# def generate_fibanacci(n):
#     num1 = 0
#     num2 = 1
#     next_number = num2
#     count = 1
#     f_list =[]
#     while(count<=n):
#         f_list.append(next_number)
#         count+=1
#         num1,num2 = num2, next_number
#         next_number = num1+num2
#     print(f_list)
# generate_fibanacci(10)
#
# def fobb(n):
#     f_list = []
#     a = 0
#     b = 1
#     for i in range(0,n):
#         f_list.append(a)
#         c = a+b
#         a=b
#         b=c
#     print(f_list)
# fobb(10)

# def find_leap_years(given_year):
#     count = 0
#     list_of_leap_years = []
#
#     while (count < 15):
#         if (given_year % 4 == 0 or given_year % 400 == 0 and given_year % 100 == 0):
#             list_of_leap_years.append(given_year)
#             count = count + 1
#         given_year = given_year + 1
#     return list_of_leap_years
#
#
# list_of_leap_years = find_leap_years(2023)
# print(list_of_leap_years)

# list1=[5,10,15,20,25]
# print(len(list1))
# print(list1[4])
# print(list1[5])
# print(list1[4:5])
# list1[2]=12
# print(list1)
# list1=list1+[8,9]

# message="welcome to Mysore"
# word=message[-7:]
# if(word=="Mysore"):
#     print("got it")
# else:
#     message=message[3:14]
#     print(message)

# list1=[5,10,15,20,25]
# print(len(list1))
# print(list1[4])
# # print(list1[5])
# print(list1[4:5])
# list1[2]=12
# print(list1)
# list1=list1+[8,9]

# import random
# print(random.randrange(10,560))
# import math
# num1=234.01
# num2=6
# num3=-27.01
# print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
# print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
# print("The factorial of num2,",num2,":", math.factorial(num2))
# print("The absolute value of num3",num3,":",math.fabs(num3))
# boarding_call="Good Evening, this is the final call to AL passengers for the flight AL 466 which is planned to take off at 8.40A.M."
# if(boarding_call.startswith("Good Evening")):
#     print(boarding_call.replace("Good Evening","Good Morning"))
# if(boarding_call.find("AL"))>=0:
#     print("Welcome to Air Lines.")
# if(boarding_call.endswith("A.M.")):
#     print("Passengers are requested to have their breakfast.")
# a=boarding_call.split(" ")
# for i in a:
#     if(i.isdigit()):
#         print("Flight Number is specified to the passengers.")
# print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AL"))
# message="Thank you allHave a nice journey!"
# print(message.upper())
# print(message.lower())
# all =boarding_call.split(" ")
# print(all)
# name = "123"
# al = name.isdigit()
# print(type(al))
# name = "PravinBalasahebKorde"
# print(name.find("a"))
# crew_details={
#     "Pilot":"Kumar",
#     "Co-pilot":"Raghav",
#     "Head-Strewardess":"Malini",
#     "Stewardess":"Mala"
# }
# print("Before update:")
# print("Co-pilot:",crew_details.get("Co-pilot"))
# crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
# print("\nAfter update:")
# print("Co-pilot:",crew_details.get("Co-pilot"))
# print("Flight Attendant:",crew_details["Flight Attendant"])
# print(crew_details)

# import re
# if(re.search(r"A\d*","A2234line")!=None):
#     print("Pattern found")
# else:
#     print("Pattern not found")
# flight_details="Flight Savana Airlines a2134"
# print(flight_details)
# print(re.sub(r"Flight",r"Plane",flight_details))
# song.upper()
# song_words=song.split()
# count=0
# for word in song_words:
#     if(word.startswith("jingle")):
#         count=count+1
# print(count)
# sample_dict={'a':1,'b':2}
# sample_dict.update({'b':5, 'c':10 })
# print(sample_dict.get('a'),sample_dict.get('b'),sample_dict.get('c'))
# word="New Airlines4"
# if(re.search(r"^N",word) and re.search(r"e$",word)):
#     print(re.sub(r"New",r"Old",word))
# else:
#     print(re.sub(r"s(\d{1})",r"S\1",word))

# import math
# num_list=[100.5,30.465,-1.22,20.15]
# num_list.insert(1, -100.5)
# num_list.pop(0)
# num_list.sort()
# print(math.ceil(math.fabs(num_list[0])))

# file_obj = open('data.txt','r')
# print(file_obj.readline(),end="")
# print(file_obj.readline(),end="")
# print(file_obj.readline(),end="")
# list_var = file_obj.readlines()
# for line in list_var:
#     print(line,end="")
# print(file_obj.read(4))
# print(file_obj.read())
# for line in file_obj:
#     print(line,end="")
# file_obj.close()

# f = open("data.txt","r")
# content =f.read()
# print(content)
# f.close()

# f = open("data.txt","w")
# line1 = f.write("This is the first new line")
# line2 = f.write("This is the second new line")
# f.close()

# f =open("data.txt","r")
# content = f.read()
# print(content)
# f = open("data.txt","a")
# line1 = f.write("Appending the first line")
# lin2 = f.write("Appending the Second line")
# f.close()

# fhw=open("data.txt","a")
# num=fhw.write("this new first line written\n")
# num1=fhw.write("this new second line written\n")
# print("num:",num)
# print("num1:",num1)
# fhw.close()
# fhr=open("data.txt","r")
# data =fhr.read()
# print("After writing:")
# print(data)
# fhr.close()


# Exception handling
# def calculate_expenditure(list_of_expenditure):
#     total=0
#     for expenditure in list_of_expenditure:
#         total+=expenditure
#     print(total)
# list_of_values=[100,200,300,"400",500]
# calculate_expenditure(list_of_values)

# def calculate_expenditure(list_of_expenditure):
#     total=0
#     for expenditure in list_of_expenditure:
#         if(type(expenditure) is int):
#             total+=expenditure
#         else:
#             print("Wrong data type")
#             break
#     print(total)
# list_of_values=[100,200,300,"400",500]
# calculate_expenditure(list_of_values)

# def calculate_expenditure(list_of_expenditure):
#     total=0
#     try:
#         for expenditure in list_of_expenditure:
#             total+=expenditure
#         print(total)
#     except:
#         print("Some error occured")
#     print("Returning back from function.")
# list_of_values=[100,200,300,"400",500]
# calculate_expenditure(list_of_values)

# def calculate_expenditure(list_of_expenditure):
#     total=0
#     try:
#         for expenditure in list_of_expenditure:
#             total+=expenditure
#         print("Total:",total)
#         avg=total/num_values
#         print("Average:",avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
#     except:
#         print("Some error occured")
# list_of_values=[100,200,300,"400",500]
# num_values=0
# calculate_expenditure(list_of_values)

# def calculate_sum(list_of_expenditure):
#     total=0
#     try:
#         for expenditure in list_of_expenditure:
#             total+=expenditure
#         print("Total:",total)
#         avg=total/no_values
#         print("Average:",avg)
#     except ZeroDivisionError:
#         print("Divide by Zero error")
#     except TypeError:
#         print("Wrong data type")
# try:
#     list_of_values=[100,200,300,400,500]
#     num_values=len(list_of_values)
#     calculate_sum(list_of_values)
# except NameError:
#     print("Name error occured")
# except:
#     print("Some error occured")
#

# balance=1000
# amount="300Rs"
# def take_card():
#     print("Take the card out of ATM")
# try:
#     if balance>=int(amount):
#         print("Withdraw")
#     else:
#         print("Invalid amount")
# except TypeError:
#     print("Type Error Occurred")
# except ValueError:
#     print("Value Error Occurred")
# except:
#     print("Some error Occurred")
# finally:
#     take_card()

# def division(a,b):
#     try:
#         return int(a)/b
#     except TypeError:
#         print("Type error")
#     except ValueError:
#         print("Value error")
#     finally:
#         print("Finally")
#     print("Done")
# division('A',10)
#

# def find_sum(a,b):
#     try:
#         print(a+c)
#     except NameError:
#         print("Function name error")
#     finally:
#         print("Sum finally")
# try:
#     find_sum(12,13)
# except NameError:
#     print("Invocation name error")
# finally:
#     print("Invocation finally")
#
# def sample(value):
#     sum1= 0
#     for i in value:
#         if i%2 == 0:
#             sum1+=value[i]
#         else:
#             sum1-=i
#     print(sum1)
#
# dict1 = {1:2,2:4,3:6,5:8}
# sample(dict1)
# fhw = open("data.txt", "w")
# fhw.write("written somw thing")
# print(fhw.tell())
# print("closed?",fhw.closed)
# fhw.close()
# print("aftee closing the file closed?", fhw.closed)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person('Pravin',24)
# print(p1.name)
# print(p1.age)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# numlist = [1,2,3,4,6,5,7,12,14,16,18]
# newlist = [x for x in fruits if "a" in x]
# newnum = [x for x in numlist if x%2==0 ]
# print(newnum)

# newlist = [x if x!="banana" else "orange" for x in fruits]
# print(newlist)
# num = [[3,4],[1,2],[0,5]]
# num.sort()
# print(num)
# if __name__ == '__main__':
#     pythonstudents = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.21], ['Akriti', 41], ['Harsh', 39]]
#     marks = []
#     for i,j in pythonstudents:
#         marks.append(j)
#     list_of_second_lowest =[]
#     highest = min(marks)
#     marks.remove(highest)
#     secondLowest = min(marks)
#     for name, scores in pythonstudents:
#         if scores==secondLowest:
#             list_of_second_lowest.append(name)
# list_of_second_lowest.sort()
# for n in list_of_second_lowest:
#     print(n)

# student_marks = {"alpha":[20,30,40],
#                  "beta":[30,50,7]
#                  }
# query_name = input()
# markslist =[]
# for key,value in student_marks.items():
#     if query_name ==key:
#         # markslist.append(value)
#         for i in value:
#             markslist.append(i)
# a=0
# for n in markslist:
#     a += n
# number = float(a/len(markslist))
# print(format(number,".2f"))
# name = "123456"
# num = int(name)
# for i in name:
#     print(int(i), type(i))
# print(type(num))
# print(num + 1)
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# x = zip(a,b)
# print(list(x))
# for i,j in x:
#     print(i[0])
# import datetime
# print(datetime.time())
# a = ("John", "Charles", "Mike")
# b= []
# j = 0
# for i in a:
#     for j in i:
#         print(j)
# print(datetime.time())
# c= [ x for x in range(10) if x%2==0]
# print(c)
# hght = lambda a,b,c: max(a,b,c)
# print(hght(12,45,78))
# def max_number(a,b,c):
#     print(max(a,b,c))
# max_number(12,45,78)
# class Animal:
#     def eat(self):
#         print("I can eat")
#     def sleep(self):
#         print("I can sleep")

# class Dog(Animal):
#     def bark(self):
#         print("I can Bark")

# dog1 = Dog()
# dog1.eat()

# class Student:
#     def __init__(self,name,age,):
#         self.name = name
#         self.age = age
#
#     def printStudentInfo(self):
#         return f"My name is {self.name} and i`m {self.age} years old"
#     def age(self):
#         return self.age
#     def name(self):
#         return self.name
#
#
#
# s1 = Student('Pravin',23)
# print(s1.printStudentInfo())
# name1 =list( "Pravin")
# print(name1)
# import pandas as pd
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar)
# a= [1,2,7]
# myvar = pd.Series(a,index = ["x", "y", "z"])
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# data1 = pd.DataFrame(data)
# print(data1.loc[[0,1]])

# linear search


# def linear_search(list,value):
#     for i in range(0,len(list)):
#         if list[i] == value:
#             return i
#     return -1
#
#
# list = [1,2,52,4,5]
# value = 52
# res = linear_search(list,value)
#
# if res == -1:
#     print("Element is not found")
# else:
#     print(f"Element is found at index:{res}")
# dict1= {
#     "fname":"pravin",
#     "lname":"Korde",
# }
# for key,value in dict1.items():
#     if value =="pravin":
#         dict1[key] = "Pravin Balasaheb"
# print(dict1)

# x,y,z = 1,2,3
#
# list1 = [x,y,z]
# list2= list1
#
# items = [["rice",2.4,8],["flour",1.8,5],["Corn",4.7,6]]
# for item in items:
#     print(f"Product :{item[0]} \nPrice: {item[1]} \nQuntity:{item[2]}\n***************************")

# def multiply(data,factor):
#     for j in range(len(data)):
#         data[j] *= factor
#     print(data)
#
# multiply([1,2,3,4,5,6],5)

# class CreditCard:
#     def __int__(self,customer  ,bank ,acnt ,limit):
#         self._account = acnt
#         self._bank = bank
#         self._costumer = customer
#         self._limit = limit
#         self._balance = 0
#
#     def get_customer(self):
#         return self._costumer
#
#     def get_bank(self):
#         return self._bank
#
#     def get_account(self):
#         return self._account
#
#     def get_limit(self):
#         return self._limit
#
#     def get_balance(self):
#         return self._balance
#
#     def charge(self,price):
#         if price+ self._balance> self._limit:
#             return False
#         else:
#             self._balance+=price
#             return  True
#
#     def make_paymane(self,amount):
#         self._balance -= amount
#
# cc = CreditCard( "John Doe", "1st Bank", "5391037593875309", 1000)

# from time import time
# list1 =[1,2,3,4,5,6,7,8,9,0,12,34,45,56,67,675]
# list2 = []
# start_time = time()
# for i in list1:
#     list2.append(i)
# print(list2)
# for k in list2:
#     print(k)
#
# end_time = time()
# alapse_time = end_time-start_time
# print(alapse_time)

# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

# a= 5+8j
# print(int(a.real))
# print(int(a.imag))

# list  =[1,2,3,4,5,6,7]
#
# def remove(lts,element):
#     finalist = []
#     for i in lts:
#         if i != element:
#             finalist.append(i)
#         else:
#             continue
#     return finalist
#
# print(remove(list,2))


# def fact(n):
#     if n==0 or n==1:
#         return  1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))


# def printList(list1,list2):
#     new_list =[]
#     for i in range(len(list1)):
#         c= list1[i]+list2[i]
#         new_list.append(c)
#     print(new_list)
#
# num1 = [1,2,4,3,5]
# num2=[6,7,8,9,10]
# printList(num1,num2)

# def sum(some_array):
#     sum_total =0
#     for i in some_array:
#         sum_total+=I
#     return sum_total
#
# if __name__=="__main__":
#     arr = [12, 3, 4, 15]
#     res = sum(arr)
#     print(f"sum of the arrey is: {res}")

# def largets(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i]> max:
#             max = arr[i]
#     return max
# arr = [10, 324, 45, 90, 9808]
# n = len(arr)
# ans = largets(arr,n)
# print(ans)

# def revers_arry(arr,d):
#     c=(arr[d:])+(arr[:d])
#     return c
# arr = [1, 2, 3, 4, 5, 6, 7]
# d=2
# ans = revers_arry(arr,d)
# print(ans)

# arr = [1,2,3,4,5,6,7,8]
# shift= 5
# a = arr[:shift]
# b = arr[shift:]
# print(b+a)
# def creating_gen(index):
#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
#     yield months[index]
#     yield months[index+2]
#
# next_month = creating_gen(3)
# print(next(next_month), next(next_month))

# month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
# convert_into_tuple = tuple(month)
# print(convert_into_tuple)
# text = "I am a programmer and love to solve the coding quesions"
# x = text.find("coding")
# y = text.replace("coding","programmimg")
# print(x)
# print(y)

# def list_prin(arr):
#     for i in arr:
#         yield i
# x= list_prin([1,2,3,4,6,8,9,8,9,9])
# print(x)
# for num in list_prin([1,2,3,4,6,8,9,8,9,9]):
#     print(num)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = next
# n1 = Node("egg")
# n2 = Node("ham")
# n3 = Node("spam")
# n1.next = n2
# n2.next= n3
#
# current = n1
# while current:
#     print(current.data)
#     current = current.next


# def recurrence(n):
#     if(n>0):
#         print(n)
#         recurrence(n-1)
# recurrence(5)

# Binary Search in python


# def binarySearch(array, x, low, high):
#
#     # Repeat until the pointers low and high meet each other
#     while low <= high:
#
#         mid = (high + low)//2
#
#         if array[mid] == x:
#             return mid
#
#         elif array[mid] < x:
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return -1
# arr= [1,2,3,4,5,6,7,8]
# x = 8
# low = 0
# high = len(arr)
# result=binarySearch(arr,x,low,high)
#
# if result != -1:
#     print(f"Element is present in the array: {result}")
# else:
#     print("Element is not present in the list")


# def binarySearch(array, x, low, high):
#
#     if high >= low:
#
#         mid = low + (high - low)//2
#
#         # If found at mid, then return it
#         if array[mid] == x:
#             return mid
#
#         # Search the left half
#         elif array[mid] > x:
#             return binarySearch(array, x, low, mid-1)
#
#         # Search the right half
#         else:
#             return binarySearch(array, x, mid + 1, high)
#
#     else:
#         return -1
#
# arr= [1,2,3,4,5,6,7,8]
# x = 8
# low = 0
# high = len(arr)
# rs =binarySearch(arr,x,0,high)
#
# if rs != -1:
#     print(f"Element is present in the array: {rs}")
# else:
#     print("Element is not present in the list")
# def reverse(arr):
#     new_list = []
#     for i in arr:
#         rs = i[::-1]
#         new_list.append(rs)
#     return new_list
#
# arr= ["pravin","Punam","Shubham","Uday"]
# print(reverse(arr))

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# numlist = [a for a in range(1,11)]
# list1 = []
# for b in fruits:
#     if "a" in b:
#         list1.append(b)
# print(list1)
# print(newlist)
# print(numlist)
# newfruite = [x.upper() for x in fruits]
# print(newfruite)
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict["colors"][0])
# newdict = dict(name="pravin",age=24,country= "india")
# print(newdict)

# x = thisdict.keys()
# for a in x:
#   print(a)
# thisdict["brand"] = "TATA"
# print(thisdict)
# x = thisdict.items()
# print(x)
# thisdict.update({"love":"Punam"})
# print(thisdict)
# for x in thisdict.values():
#   print(x)

# for x in thisdict.keys():
#   print(x)

# for key,value in thisdict.items():
#   print(f"{key} = {value}")
# wife = {
#   "name":"Punam",
#   "year":2000
# }
# husbund = {
#   "name": "Pravin",
#   "year":1999
# }
# family = {
#   "wife": wife,
#   "husbund": husbund
# }
# for key,value in family.items():
#   x=value.values()
#   for i in x:
#     print(i)

# numlist = [1,2,3,2,3,1,4,5]
# mewdict ={}
# for i in numlist:
#   x = numlist.count(i)
#   mewdict[i]= numlist.count(i)
# print(mewdict)
# num = int(input("enter the number:"))
# newstring = str(num)
# compare= newstring[::-1]
# final = int(compare)
# if num == final:
#   print("It is palindrome")
# else:
#   print("its not an palindrome")
# def fct(s):
#
#   new_strint= s.split()
#   dict ={}
#   for i in new_strint:
#     dict[i] = new_strint.count(i)
#   print(dict)
#
# n = "pravin korde i am pravin"
# fct(n)

# def isPalindrome(name):
#     if name == name[::-1]:
#         print(True)
#     else:
#         print(False)

# def fact(num):
#     if num ==0 or num == 1:
#         return 1
#     else:
#         return (num * fact(num -1))
#
# print(fact(5))

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# y= json.dumps(x)
# print(y)
#
# NAME = "Evaluating Market Potential Awareness for Agrochemicals and Micronutrient Fertilizers in Nashik for Poorva Chemtech Pvt Ltd."
# print(NAME.capitalize())

# c = 8
# def add(a,b):
#   global e
#   e= 4
#   print(c)
#   print(a+b)
# add(8,8)
# print(e)

# a="hello"
# print(a[start:end:step])
# a="hello"
# b=" world"
# print(a,end="")
# print(b)
#
# list1=[1,2,3,4,5]
# for x in list1:
#       print(x)
#       print(list1)

# list1=[5,2,3,4,5]
# list2=[]
# print(len(list1))
# for x in range(0,len(list1)):
#     list2.append(list1)
# print(list2[x])
# list1=[1,2,3,4,5,6,7,8,9,10]
# n=2
# for x in list1:
#     print(n*x)

# count=0
# for x in range(1,50):
#     if x%2==1:
#         # print(str(x)+"is odd")
#         count=count+1
# print(count)
# else:
 #     print("number is even")
#
# count=0
# list=[1,2,3,4,5,6,7,8,9,10]
# print(len(list))
# for x in list:
#     count=count+x
# average=count/len(list)
# print(average)

# list=[1,-2,3,-4,5,6,-7,8,-9,10]
# for x in list:
#     if x>0:
#         print(str(x)+"positive")
#     else:
#         print(str(x)+"negative")


# list1 = [1,2,3,4]
# for x in list1:
#     print(x)


# list3 = [1,2,3,5,7]
# for p in list3:
#     print(p)
#
# list4 = [1,2,3,417,8]
# for c in list3:
#     print(c)

# num =[1,2,3,4,4,3,2,5]
# print(set(num))
#
# numbers = [x for x in range(10) if x%2==0]
# print(numbers)

# def add(a,b):
#     return a+b
# a=map(add,(1,2,3),(4,5,6))
# print(list(a))

# a= (1,2,3,4,5,6,7,8,9)
# x = slice(1,5)
# print(a[x])

# def palindrome():
#     str = input("Enter the string: ")
#     if str == str[::-1]:
#         return "It is Palindrome"
#     else:
#         return "Not palindrome"
#
# list1=[1,2,3,4,5]
# print(palindrome())
# import tkinter as tk
# from tkinter import *
# import random
# win = tk.Tk()
# win.geometry("750x750")
# win.title("PythonGeeks")
# num=random.randint(1,50)
# hint = StringVar()
# score = IntVar()
# final_score= IntVar()
# guess= IntVar()
# hint.set("Guess a number between 1 to 50 ")
# score.set(5)
# final_score.set(score.get())
# def fun():
#     x = guess.get()
#     final_score.set(score.get())
#     if score.get() > 0:
#
#         if x > 20 or x < 0:
#             hint.set("You just lost 1 Chance")
#             score.set(score.get() - 1)
#             final_score.set(score.get())
#
#         elif num == x:
#             hint.set("Congratulation YOU WON!!!")
#             score.set(score.get() - 1)
#             final_score.set(score.get())
#
#         elif num > x:
#             hint.set("Your guess was too low: Guess a number higher ")
#             score.set(score.get() - 1)
#             final_score.set(score.get())
#         elif num < x:
#             hint.set("Your guess was too High: Guess a number Lower ")
#             score.set(score.get() - 1)
#             final_score.set(score.get())
#     else:
#         hint.set("Game Over You Lost")
# Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
#
# Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7,
#                                                                                                 anchor=CENTER)
#
# Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)
#
# Label(win, text='I challenge you to guess the number ', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
#
# Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)
#
# Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5,
#                                                                                                             rely=0.5,                                                                                                   anchor=CENTER)


# import random
# import string
#
# total = string.ascii_letters + string.digits + string.punctuation
#
# length = 16
#
# password = "".join(random.sample(total, length))
#
# print(password)

# import tkinter as Tkinter
# from datetime import datetime

# counter = 0
# running = False
#
#
# def counter_label(label):
#     def count():
#         if running:
#             global counter
#             # To manage the intial delay.
#             if counter == 0:
#                 display = 'Ready!'
#             else:
#                 tt = datetime.utcfromtimestamp(counter)
#                 string = tt.strftime('%H:%M:%S')
#                 display = string
#
#             label['text'] = display
#
#             # label.after(arg1, arg2) delays by
#             # first argument given in milliseconds
#             # and then calls the function given as second argument.
#             # Generally like here we need to call the
#             # function in which it is present repeatedly.
#             # Delays by 1000ms=1 seconds and call count again.
#             label.after(1000, count)
#             counter += 1
#
#     # Triggering the start of the counter.
#     count()
#
#
# # start function of the stopwatch
# def Start(label):
#     global running
#     running = True
#     counter_label(label)
#     start['state'] = 'disabled'
#     stop['state'] = 'normal'
#     reset['state'] = 'normal'
#
#
# # Stop function of the stopwatch
# def Stop():
#     global running
#     start['state'] = 'normal'
#     stop['state'] = 'disabled'
#     reset['state'] = 'normal'
#     running = False
#
#
# # Reset function of the stopwatch
# def Reset(label):
#     global counter
#     counter = 0
#     # If reset is pressed after pressing stop.
#     if not running:
#         reset['state'] = 'disabled'
#         label['text'] = '00:00:00'
#     # If reset is pressed while the stopwatch is running.
#     else:
#         label['text'] = '00:00:00'
#
#
# root = Tkinter.Tk()
# root.title("Stopwatch")
#
# # Fixing the window size.
# root.minsize(width=250, height=70)
# label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
# label.pack()
# f = Tkinter.Frame(root)
# start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
# stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
# reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
# f.pack(anchor='center', pady=5)
# start.pack(side='left')
# stop.pack(side='left')
# reset.pack(side='left')
# root.mainloop()

# -*- coding: utf-8 -*-
# from tkinter import Tk, END, Entry, N, E, S, W, Button
# from tkinter import font
# from tkinter import Label
# from functools import partial
#
#
# def get_input(entry, argu):
#     entry.insert(END, argu)
#
#
# def backspace(entry):
#     input_len = len(entry.get())
#     entry.delete(input_len - 1)
#
#
# def clear(entry):
#     entry.delete(0, END)
#
#
# def calc(entry):
#     input_info = entry.get()
#     try:
#         output = str(eval(input_info.strip()))
#     except ZeroDivisionError:
#         popupmsg()
#         output = ""
#     clear(entry)
#     entry.insert(END, output)
#
#
# def popupmsg():
#     popup = Tk()
#     popup.resizable(0, 0)
#     popup.geometry("120x100")
#     popup.title("Alert")
#     label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
#     label.pack(side="top", fill="x", pady=10)
#     B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
#     B1.pack()
#
#
# def cal():
#     root = Tk()
#     root.title("Calc")
#     root.resizable(0, 0)
#
#     entry_font = font.Font(size=15)
#     entry = Entry(root, justify="right", font=entry_font)
#     entry.grid(row=0, column=0, columnspan=4,
#                sticky=N + W + S + E, padx=5, pady=5)
#
#     cal_button_bg = '#FF6600'
#     num_button_bg = '#4B4B4B'
#     other_button_bg = '#DDDDDD'
#     text_fg = '#FFFFFF'
#     button_active_bg = '#C0C0C0'
#
#     num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
#                          padx=10, pady=3, activebackground=button_active_bg)
#     cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
#                          padx=10, pady=3, activebackground=button_active_bg)
#
#     button7 = num_button(text='7', bg=num_button_bg,
#                          command=lambda: get_input(entry, '7'))
#     button7.grid(row=2, column=0, pady=5)
#
#     button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
#     button8.grid(row=2, column=1, pady=5)
#
#     button9 = num_button(text='9', command=lambda: get_input(entry, '9'))
#     button9.grid(row=2, column=2, pady=5)
#
#     button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
#     button10.grid(row=4, column=3, pady=5)
#
#     button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
#     button4.grid(row=3, column=0, pady=5)
#
#     button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
#     button5.grid(row=3, column=1, pady=5)
#
#     button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
#     button6.grid(row=3, column=2, pady=5)
#
#     button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
#     button11.grid(row=3, column=3, pady=5)
#
#     button1 = num_button(text='1', command=lambda: get_input(entry, '1'))
#     button1.grid(row=4, column=0, pady=5)
#
#     button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
#     button2.grid(row=4, column=1, pady=5)
#
#     button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
#     button3.grid(row=4, column=2, pady=5)
#
#     button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
#     button12.grid(row=2, column=3, pady=5)
#
#     button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
#     #button0.grid(row=5, column=0, columnspan=2, padx=3, pady=5, sticky=N + S + E + W)
#     button0.grid(row=5, column=0,  pady=5)
#
#     button13 = num_button(text='.', command=lambda: get_input(entry, '.'))
#     button13.grid(row=5, column=1, pady=5)
#
#     button14 = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
#                       command=lambda: get_input(entry, '/'))
#     button14.grid(row=1, column=3, pady=5)
#
#     button15 = Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
#                       command=lambda: backspace(entry), activebackground=button_active_bg)
#     button15.grid(row=1, column=0, columnspan=2,
#                   padx=3, pady=5, sticky=N + S + E + W)
#
#     button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
#                       command=lambda: clear(entry), activebackground=button_active_bg)
#     button16.grid(row=1, column=2, pady=5)
#
#     button17 = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
#                       command=lambda: calc(entry), activebackground=button_active_bg)
#     button17.grid(row=5, column=3, pady=5)
#
#     button18 = Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
#                       command=lambda: get_input(entry, '**'))
#     button18.grid(row=5, column=2, pady=5)
#     def quit():
#         exit['command'] = root.quit()
#     exit = Button(root, text='Quit', fg='white', bg='black', command=quit, height=1, width=7)
#     exit.grid(row=6, column=1)
#
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     cal()

# squares = [' ']*9
# players = 'XO'
# board = '''
#   0   1   2
#   {0} | {1} | {2}
#  -----------
# 3 {3} | {4} | {5} 5
#  -----------
#   {6} | {7} | {8}
#   6   7   8
# '''
# win_conditions = [
#     (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
#     (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
#     (0, 4, 8), (2, 4, 6)             # diagonals
# ]
#
# def check_win(player):
#     for a, b, c in win_conditions:
#         if {squares[a], squares[b], squares[c]} == {player}:
#             return True
#
# while True:
#     print(board.format(*squares))
#     if check_win(players[1]):
#         print(f'{players[1]} is the winner!')
#         break
#     if ' ' not in squares:
#         print('Cats game!')
#         break
#     move = input(f'{players[0]} to move [0-8] > ')
#     if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
#         print('Invalid move!')
#         continue
#     squares[int(move)], players = players[0], players[::-1]


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# p1 = Person("John", 36)
#
# class Emp:
#     def __init__(self, name, id):
#         self.name=name
#         self.id= id
#
#     def info(self):
#         return f"name is {self.name} and id {self.id}"
#
# n = Emp("pravin", 24)
#
# class Employee:
#     def __init__(self,emp_name, emp_id):
#         self.emp_name= emp_name
#         self.emp_id =emp_id
#
#     def AllInfo(self):
#         return f"Name is {self.emp_name} and id {self.emp_id}"
#
# E1 =Employee("XYZ",1)
# print(E1.AllInfo())

# decorators in python

# def greet(name):
#     print("Good morning")
#     name(4,2)
#     print("Good night")

# @greet
# def sayHi():
#     print("Hi")
# @greet
# def add(a,b):
#     print(a+b)

# data = [1,2,3,4,5]
# res= map(lambda x:x+1,data)
# print(list(res))
# for i in res:
#     print(i,end=" ")

# resfilter = filter(lambda x:x%2==0,data)
# print(list(resfilter))

# num = [x for x in range(20) if x%2==0]
# print(num)

# p1 = [1,2,3,4,5]
# for i in p1:
#     print(i - 1)

# def main():
#     return pass
#
# print(main())

# def Triangle(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print("")
#
# Triangle(5)

# def Number_Triangle(n):
#     row = n
#     count = 1
#     for i in range(0,row):
#         for j in range(0,i+1):
#             print(f"{count}",end=" ")
#             count+=1
#         print("")
#
# Number_Triangle(5)
# import time
# def countDown(sc):
#     for second in range(sc,0,-1):
#         print(second)
#         time.sleep(1)
#     print("Happy New Year")
# countDown(5)

# n = int(input("enter the no.:"))
# finalNum =""
# for i in range(1,n+1):
#     convert = str(i)
#     finalNum=finalNum+convert
# print(finalNum)
# print(type(finalNum))

# num = [1,2,3,4]
# num.clear()
#
# class Dog:
#     def __init__(self,name,breed):
#         self.name= name
#         self.breed= breed
#
# dog1 =Dog("Simba","abc")
# # print(isinstance(dog1,Dog))
#
# c=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             c=c+1
# print(c)
# a,b= 1,2
# _= a+b
# print(_)

# string= "abcd"
# for i in range(len(string)):
#     print(i,end="")

# x=y=5,10
# res=x==y
# print(res)

# def binaryRecursive(array,element,low,high):
#     mid = low + (high-low)//2
#     if high>= low:
#         if array[mid] == element:
#             return  mid
#         elif array[mid] < element:
#             return binaryRecursive(array,element,mid + 1,high)
#         else:
#             return binaryRecursive(array,element,low,mid-1)
#     else:
#         return -1
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 8
#
# result1 = binaryRecursive(array, x, 0, len(array)-1)
#
# if result1 != -1:
#     print(f"Element found at index {result1}")
# else:
#     print('ELement is not found')

# class Planet:
#     def __init__(self):
#         print('1')
#
#     def __init__(self):
#         print('2')
#
# p= Planet()
# a ='1'
# b = '2'
# print(a+b)

# def BinarySearch(array,element,low,high):
#    if high >= low:
#        mid = low + (high - low)//2
#
#        if array[mid] == element:
#            return mid
#        elif element > array[mid]:
#            return BinarySearch(array,element,mid+1,high)
#        else:
#            return BinarySearch(array,element,low,mid-1)
#    else:
#        return  -1
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 7
# result1 = BinarySearch(array, x, 0, len(array)-1)
#
# if result1 != -1:
#     print("Element is present at index " + str(result1))
# else:
#     print("Not found")

# def say(afternoon):
#     print("Good Morning")
#     afternoon()
#     print('good Night')
#
# @say
# def sayafternoon():
#     print('Good Afternoon')

# for i in range(0,6):
#     for j in range(0,i):
#         print("*",end="")
#     print()

# def fibo(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fibo(num-1)
# print(fibo(5))

# def getSmall(n1,n2):
#     if n1>n2:
#         print(n2)
#     elif n2>n1:
#         print(n1)
#     else:
#         print(None)
#
# getSmall(2,85)

# def Findmwdian(arr1,arr2):
#     median = len(arr1) // 2
#     newarr = arr1.append(arr2)
#     sortarr = newarr.sort()
#     if len(sortarr)%2==0:
#         return sortarr[median] + arr1[median-1]
#     else:
#         return arr1[median]
#
# num = [1,2,3,4,5]
#
# print(Findmwdian(num))

# tup = ("apple", "banana", "cherry")
# if "apple" in tup:
#     print(True)
# else:
# #     print(False)
# a = (1,2,3)
# b= (4,5)
# c = a+b
# d =(4,)
# print(type(d))


# fruits = ("apple", "banana", "cherry","strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)

# name = "asdasfjfkdbfds"
# dict1={}
# for i in name:
#
# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         nums1.sort()
#         nums2.sort()
#         merger_array=nums1+nums2
#         median = len(merger_array)//2
#
#         if len(merger_array)%2 == 0:
#             return merger_array[median]+ merger_array[median-1]
#         else:
#             return merger_array[median]
#
# a = Solution()

# def cookDist():
#     a = input("enter:")
#     size = int(a[0])
#     searchignElement = int(a[-1])
#     list1=[]
#     for i in range(size):
#         b = int(input())
#         list1.append(b)
#
#     if searchignElement in list1:
#         return"YES"
#     else:
#         return "NO"
#
# print(cookDist())
# def Noodle():
#     a = input()
#     num=a.split("  ")
#     c = num[0]
#     d =num[1]
#     return(int(c)* int(d),num)
# print(Noodle())

# a = map(int,input())
# print(a*2)

# num = [2,3,4,3,2]
# num1= sorted(num)
# for i in range(len(num)-1):
#     if num1[i] == num1[i+1]:
#         i = i+2
#     else:
#         print(num1[i])

# def findMAx(num):
#     userInput= 0
#     max_value = 0
#     for i in range(num):
#         userInput = int(input())
#         if max_value <= userInput:
#             max_value=  userInput
#     print(max_value)
#
#
# b = int(input())
# findMAx(b)

# def Running_comparison():
#     for i in range(int(input())):
#         n = int(input())
#         a = list(map(int, input().split()))
#         b = list(map(int, input().split()))
#
#         # Your code goes here
#         happy = 0
#         for i in range(n):
#             if a[i] * 2 >= b[i] and b[i] * 2 >= a[i]:
#                 happy += 1
#         print(happy)
#
# Running_comparison()

# num=[1,2,4,5]
# a = sorted(num)
# ans = "NO"
# for i in range(len(num)-1):
#     if num[i] == a[i]:
#         ans = "YES"
#     else:
#         ans ="NO"
#
# print(ans)

# n = int(input("Enter the rows"))
#
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()

# line = "pravin korde"
# a= line.split(" ")
# b = "-".join(a)
# print(b)
# import textwrap
#
# def wrap(string, max_width):
#     wrapper =textwrap.TextWrapper(width=max_width)
#     word_list = wrapper.wrap(text=string)
#     for i in word_list:
#         print(i)
#
#
# string="wqejfbfwjrflwbrf"
# max_width=4
# result = wrap(string, max_width)
# print(result)

# l1= [1,2,3]
# l2 = [4,5,6]
# l1_str=""
# l2_str=""
# for i in range(len(l1)):
#     b =str(l1[i])
#     c= str(l2[i])
#     l1_str+=b
#     l2_str+=c
# l1_int =int(l1_str)
# l2_int =int(l2_str)
# print(l1_int+l2_int)

# num = 121
# a = str(num)
# print(a[::-1])
# strs = ["flower","flow","flight"]
#
# prefix = ""
# a = strs[0]
# b = strs[1]
# noprefix = ""
# for i in range(len(a)):
#     if a[i] == b[i]:
#         prefix+=a[i]
#     else:
#         break
# print(prefix)

# def removeDuplicates(nums):
#     i = 0
#
#     for num in nums:
#       if i < 1 or num > nums[i - 1]:
#         nums[i] = num
#         i += 1
#
#     return i
# print(removeDuplicates([1,1,1,1,2,2,2,3,3,3,4]))

# num = [0,1,2,2,3,0,4,2]
# val=2
# for i in range(len(num)-1):
#     if num[i] == val:
#         num.remove(num[i])
# print(num)

# strs = ["flower","flow","flight","fl"]
# word =""
# prev =0
# next = 1
# l=0
# while True:
#     if len(strs[next]) <= len(strs[prev]):
#        word= strs[next]
#     next = next + 1
#     prev+=1
#     if len(strs):
#         break
# print(word)

# class Store:
#     def __init__(self):
#         self.map = [1,2,2,3,4,5,6]
#
#     def Print_list(self,value):
#         return value
#
# s = Store()
# c=s.Print_list([12])
# print(c)
# nums = [1,3,5,6]
# target = 7
# if target in nums:
#     print(nums.index(target))
# else:
#     nums.append(target)
#     nums.sort()
#     print(nums.index(target))



# def singlNumber(nums):
#     for i in nums:
#         a = nums.count(i)
#         if a != 2:
#             return i
#
# nums = [1]
# res =singlNumber(nums)
# print(res)

# s ="A man, a plan, a canal: Panama"
# words = s.split(" ")
# words.remove(",")
# print(words)
# new_s = ""
# for i in words:
#     new_s+=i
# x= new_s.replace(",","")
# if x==x[::-1]:
#     print(True)

# arr =[1,3,5,7,9]
# min_sum =0
# max_sum =0
# for i in range(len(arr)-1):
#     min_sum+= arr[i]
# for i in range(1,len(arr)):
#     max_sum+= arr[i]
# print(min_sum,max_sum)
# arr = [3,2,4,5,1,9]
# arr.sort()
# print(arr)
# median = len(arr)//2
# if len(arr)%2 !=0:
#     print(arr[median])
# else:
#     print(arr[median]+ arr[median-1]

# def largest_prime_factor(num):
#     res= 0
#     for i in range(1,num+1):
#         if num%i==0:
#             res=i
#     print(res)
# largest_prime_factor(23)
# t = int(input().strip())
# for a0 in range(t):
#     num = int(input().strip())
#     res = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             res=i
#         print(res)
# t = int(input("enter").strip())
# res =0
# for a0 in range(t):
#     n = int(input("num:").strip())
#
#     for i in range(1,n+1):
#         if n%1==0:
#             res= i
# print(res)


# def median(num1,num2):
#     num3 = num1 + num2
#     num3.sort()
#     median = len(num3) // 2
#     if len(num3) % 2 != 0:
#         return(num3[median])
#     else:
#         return ((num3[median] + num3[median - 1]) / 2)
#
# num1 =[1,3]
# num2 = [2,4]
# res =median(num1,num2)
# # print(res)
#
# def Repeat_string(s):
#     s = list(a)
#     c = []
#     for i in range(len(s)):
#         if s[i] not in c:
#             c.append(s[i])
#     res = "".join(c)
#     return res
# a = "pwwkew"
# res =Repeat_string(a)
# print(res)

# s = "   erojewr  erijer kjej eijfeip   "
# b = s.split(" ")
# c=[]
#
# for i in range(len(b)):
#     if len(b[i]) ==1:
#         if b[i]=='':
#             continue
#         else:
#             c.append(b[i])
# print(c)
# height = [4,3,2,1,4]
# c= set(height)
# b= list(c)
# b.sort()
# print(b[-2]*b[-2])

# def two_sum(num,target):
#     nums=num
#     nums.sort()
#     l=0
#     r=len(nums)-1
#     res =[]
#     while l<r:
#         if nums[l]+ nums[r]==target:
#             c=[nums[l],nums[r]]
#             res.append(num.index(nums[l]))
#             res.append(num.index(nums[r]))
#             return res
#         elif nums[l]+ nums[r]<target:
#             l+=1
#         else:
#             r-=1
# nums= [3,2,4]
# t=6
# res =two_sum(nums,t)
# print(res)
# divident =7
# divisor =-2
# d =abs(divident)
# dv =abs(divisor)
# res =0
# while d>= dv:
#     temp =dv
#     mul=1
#     while d>=temp:
#         d-=temp
#
# if (divident<0 and divisor>=0) or(divisor<0 and divident>=0):
#     res= -res
# print(res)

# def SearchDuplicates(nums):
#     hashamp = set()
#     for n in nums:
#         if n in hashamp:
#             return True
#         hashamp.add(n)
#     return  False
# nums = [1,2,3,22,22]
# res =SearchDuplicates(nums)
# print(res)

# def singleNumber(nums):
#     for i in nums:
#         a = nums.count(i)
#         if a == 1:
#             return i
#
# nums = [1,2,3,3,2,1,9]
# res =singleNumber(nums)
# print(res)

# def sum_of_arrary(n):
#     l = 0
#     r = len(n) - 1
#     target = 15
#     condition = True
#     while condition:
#         c = n[l:r]
#         s = sum(c)
#         if s == target:
#             return l + 1, r
#             break
#         elif s > target:
#             r -= 1
#         else:
#             l += 1
#
# n =[1,2,3,4,5,6,7,8,9,10]
# res=sum_of_arrary(n)
# print(res)

# def compareTriplte(a,b):
#     alice=0
#     bob=0
#     for i in range(len(a)):
#         if a[i] == b[i]:
#             continue
#         elif a[i]> b[i]:
#             alice+=1
#         else:
#             bob+=1
#     return [alice,bob]
# a=[17,28,30]
# b= [99,16,8]
# res =compareTriplte(a,b)
# print(res)

class Node:
    def __init__(self,value):
        self.value= value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length= 1

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next

    def append(self,value):
        new_node = Node(value)

        if self.length ==0:
            self.head =new_node
            self.tail =new_node
        else:
            self.tail.next =new_node
            self.tail= new_node
        self.length+=1
        return  True

    def pop(self):
        if self.length==0:
            return None

        temp =self.head
        pre= self.head
        while temp.next is not None:
            pre=temp
            temp = temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head =None
            self.tail= None
        return temp.value

    def get(self,index):
        temp = self.head
        for _ in range(index):
            temp= temp.next
        return temp

l =LinkedList(1)
l.append(4)
print(l.pop())
print(l.pop())
print(l.pop())
