# Mastering Python
![python](./img/pic1.png)

# Project

# Variables

## What are variables?
A reusable container for storing a value
 
A variable behaves as if it were the value it contains

## Variable Command
The following are examples of how variables can be displayed along with a text
 

```
If the variable is age and age = 21
Using string, print("You are " + str(age) + " years old")
By seperating the text and variabke in two separate arguement ("You are",age,"years old")
Using the f command, print(f"You are {age} years old")

```
![variable](./img/variables.jpg)

# TYPES OF DATA TYPES
There are four types of data types

## 1. Integers
Integers are whole numbers

age = 21

players = 2

quantity = 5

```
print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")
```

![Integer](./img/integers.jpg)

## 2. Float
They are numbers that contains decimal portions

gpa = 3.2

distance = 2.5

price = 10.99

```
print(f"Your gpa is {gpa}")
print(f"You ran a distance of {distance}km")
print(f"The price is ${price}")
```
![float](./img/float.jpg)

## 3. String
They are just a series of text or characters

name = "Bro"

food = "pizza"

email = "bro123@gmail.com"

```
print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")
```
![string](./img/string.jpg)

## 4. Float
This is a binary which is either true or false

online = True

for_sale = False

running = True
```
print(f"are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")
```
![boolean](./img/boolean.jpg)

## More on Variables

 
x = 1

y = 2

z = 3
```
print(x)

print(y)

print(z)
```

multiple assignment

x, y, z = 1, 2, 3
```
print(x)

print(y)

print(z)
```
set multiple variable to the same value

x = y = z = 0

```
print(x)

print(y)

print(z)
```
![mv](./img/mv1.jpg)
![mv](./img/mv2.jpg)

# List of numbers
# define a list of numbers
numbers = [1,2,3,4,5]

# Access and print individual elements
```
#print(numbers[1])

#print(numbers[2])

#print(numbers[3])

#print(numbers[0])

#print(numbers[2])

#print(numbers[3])

print(numbers[1])

print(numbers[2])

print(numbers[3])

print(numbers[-1])

print(numbers[-2])

print(numbers[-3])
```
![list](./img/list1.jpg)

# Modify an element
```
numbers[-1]=3
print(numbers)
```

# Add an element to the end
```
numbers.append(10)
print(numbers)
```

# remove an element from the list
```
numbers.pop()

print(numbers)

numbers.remove(1)

print(numbers)
```

# Get the length of the list
print("print the lenght of the list")

print(len(numbers))

![list](./img/list2.jpg)

# Iterate through the list
```
print("iterate through the list")
list_of_strings = ["1", "2", "3", "4", "5"]
list_of_numbers = [float(x) for x in list_of_strings]
print(list_of_numbers)
```
![list](./img/list3.jpg)
![list](./img/list4.jpg)

## Executing string using split

string_1 = "I am a boy"
#This is a string

string_2 = "2 3 4 5"                              #This is a string

#list_1 = ["I" "am" "a" "boy"]                      
#This is a list of strings

#list_2 = ["2" "3" "4" "5" "6"]                     
#This is a list of strings

```
print(string_1)

print(string_1.split())

print(string_2)

print(string_2.split())

```
![split](./img/split.jpg)

## Combination of 3 functions

Function to get numbers from the user.
def 

get_numbers():


input_string = input("Type here: ")


list_of_strings = input_string.split()

list_of_numbers = [float(num) for num in list_of_strings]

return list_of_numbers

list_of_numbers = get_numbers()

Function to calculate the sum of a list of numbers

def calculate_sum(any_list_of_number):
    total = (sum(any_list_of_number))
    return total

total = calculate_sum(list_of_numbers)

Function to display the sum to the user

def display_result(number):

```
    #print(number)
    print('The sum of {} is {}'.format(list_of_numbers, number))
```

display_result(total)

![comb](./img/comb1.jpg)

## Implementing Abstract

#function to get numbers from the user.
def get_numbers():

input_string = input("Type here: ")

list_of_strings = input_string.split()

list_of_numbers = [float(num) for num in list_of_strings]

return list_of_numbers


#Function to calculate the sum of a list of numbers

def calculate_sum(any_list_of_number):

total = (sum(any_list_of_number))

return total


#Function to display the sum to the user
def display_result(number):

    print('The sum of numbers in our list is {}'.format(number))

def main():

list_of_numbers = get_numbers()

total = calculate_sum(list_of_numbers)

display_result(total)

main()

![abstract](./img/impab.jpg)
