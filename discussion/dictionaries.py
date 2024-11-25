#BASIC
#Ceate a dictionary with three key value pairs representing a student's information:name,age,and grade.Print each key on a new line.
student_info = {
    'name':"Rashida",
    'age':25,
    'grade': "B"
}
for key in student_info:
    print(key)    
#INTERMEDIATE.
#Write a function that takes a dictionary of people's names and their ages,{'Alice': 24, 'Bob': 19,'charlie': 30}.and
# returns a list of names of people who 21 or older.
def filter_adults(people):
    return[name for name, age in people.items()if age >= 21]
people_ages = {'Alice': 24 ,'Bob':19,'charlie': 30}
adults = filter_adults(people_ages)
print("people 21 or older", adults)
#Advanced 
#Given a dictionary representing items in a store with their prices,{'apple': 0.5,'banana': 0.3, 'orange': 0.7},
#write a program that takes a list of items bought ,['apple', 'orange', 'banana', 'banana'],and calculates the total cost .
items_bought = ['apple','orange','banana','banana']
prices = {'apple':0.5, 'banana':0.3,'orange':0.7}
total_cost =0
for item in items_bought:
    total_cost += prices[item]
print("Total cost:",total_cost)    
#CHALLENGE
#Write a program that counts the occurences of eeach word in a given sentence .Example:for the sentence "hello world hello"
#the output should be {'hello':2, 'world':1}
words= 'hello world hello'
def count_word_occurrences(sentence):
    word_counts = sentence.lower().split()
    word_counts= {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] =1  
sentence ='hello world hello'
word_counts=count_word_occurrences(sentence)
for word, count in word_counts.items():
    print(f"{word}: {count}")
