#BASIC
#Create a list of 5 fruits and print each fruit on a new line using a for loop.
list =['orange','mango','apple','banana']
for fruit in list:
    print(fruit)

# INTERMEDIATE
# Write a function that takes a list of numbers and returns a new list with each number squared.
# Example:[1,2,3,]should become[1,4,9].
numbers=[1,2,3,4]
squared_numbers=[num** 2 for num in numbers]
print(numbers)
print(squared_numbers)
# ADVANCED
# Write a pythn program that takes two lists. list1 =[1,2,3] and list2 =[4,5,6],and combines them into 
# a single list , combined = [1,4,2,5,3,6].
list1=[1,2,3]
list2=[4,5,6]
list3= list1 + list2
print(list3)
# CHALLENGE.
# Given a list of numbers,[3,1,4,1,5,9,2].Write a program to find and print the two largest numbers in the list without
# using the max()function.
numbers = [3,1,4,1,5,9,2]
largest =second_largest =float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num 
    elif num > second_largest:
        second_largest =num  
print("The largest number is:",)
print("The second largest number is",)          
 
 