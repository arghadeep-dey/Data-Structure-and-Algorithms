from array import array
import numpy as np
#Python Specific Data Structures

#String
'''
A string is a sequence of characters. 
In Python, strings are immutable, meaning that once they are created, 
they cannot be changed. Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). 
Triple quotes are often used for multi-line strings.(Like this one)
'''
#Creation
str1 = 'Hello'
str2 = "World"
str3 = '''T
his is a multi-line string.
It can span multiple lines.
'''

#Accessing characters
print(str1[0])  # Output: H
print(str1[-1]) # Output: o

#String Slicing
print(str1[1:4])  # Output: ell
print(str1[:3])   # Output: Hel
print(str1[2:])  # Output: llo
print(str1[::-1])  # Output: olleH

#Iteration
for char in str1:
    print(char) # Output: H e l l o (each character on a new line)

#Delete
del str1

#Update
str1 = 'Hi' # This creates a new string object and assigns it to str1

#Methods
print(len(str1))  # Output: 2
print(str1.upper())  # Output: HI
print(str1.lower())  # Output: hi
print(str1.replace('i', 'ello'))  # Output: Hello
print(str1.split('i'))  # Output: ['H', '']
print(str1.strip())  # Output: Hi (removes leading and trailing whitespace)

#Concatenation
str4 = str1 + ' there'  # Output: Hi there

#Formatting
name = 'Alice'
greeting = f'Hello, {name}!'  # Output: Hello, Alice!

#String Membership
print('H' in str1)  # Output: True
print('h' in str1)  # Output: False
#********************************************************************************************

#List
'''
A list is a collection of items that are ordered and changeable.
Lists are defined using square brackets [ ] and can contain elements of different data types.
'''
#Creation
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

#Accessing elements
print(list1[0])  # Output: 1
print(list1[-1]) # Output: 5

#List Slicing
print(list1[1:4])  # Output: [2, 3,4]
print(list1[:3])   # Output: [1, 2, 3]

#Iteration
for num in list1:
    print(num) # Output: 1 2 3 4 5 (each number on a new line)

#Delete
del list1[0]  # Deletes the first element of the list
del list1  # Deletes the entire list

#Update
list1 = [1, 2, 3, 4, 5]
list1[0] = 10  # Updates the first element to 10

#Methods
print(len(list1))  # Output: 5
list1.append(6)  # Output: [10, 2, 3, 4, 5, 6]
list1.insert(1, 15)  # Output: [10, 15, 2, 3, 4, 5, 6]
list1.remove(15)  # Output: [10, 2, 3, 4, 5, 6]
print(list1.pop())  # Output: 6 (removes and returns the last element)
print(list1)  # Output: [10, 2, 3, 4, 5]
list1.clear()  # Output: [] (removes all elements from the list)

#Concatenation
list3 = list1 + list2  # Output: [10, 2, 3, 4, 5, 'a', 'b', 'c']

#Repetition
list4 = list2 * 3  # Output: ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

#List Membership
print(10 in list1)  # Output: True
print(15 in list1)  # Output: False

#List Comprehension
#Loop
squared = [x**2 for x in list1]  # Output: [100, 4, 9, 16, 25] (creates a new list with the squares of the elements in list1)   

a = [i for i in range(10)]
print(a)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (creates a list of numbers from 0 to 9)

c = [(x, y) for x in range(3) for y in range(3)]
print(c)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] (creates a list of tuples representing all combinations of x and y from 0 to 2)        

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] (flattens a 2D list into a 1D list)

#Loops with Conditions
even_squares = [x**2 for x in list1 if x % 2 == 0]  # Output: [100, 4, 16] (creates a new list with the squares of the even elements in list1)

result = ['Even' if n % 2 == 0 else 'Odd' for n in a]  
print(result)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd'] (creates a new list with 'Even' for even numbers and 'Odd' for odd numbers in the list a)

result = ['Divisible by 2' if n % 2 == 0 else 'Divisible by 3' if n % 3 == 0 else 'Other' for n in a]  
print(result)  # Output: ['Divisible by 2', 'Divisible by 3', 'Divisible by 2', 'Divisible by 3', 'Divisible by 2', 'Other', 'Divisible by 2', 'Divisible by 3', 'Divisible by 2', 'Other'] (creates a new list with different strings based on the divisibility of the numbers in the list a)
#********************************************************************************************

#Tuple
'''
A tuple is a collection of items that are ordered and unchangeable.
Tuples are defined using parentheses ( ) and can contain elements of different data types.
'''

#Creation
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')

#Accessing elements
print(tuple1[0])  # Output: 1
print(tuple1[-1]) # Output: 5

#Tuple Slicing
print(tuple1[1:4])  # Output: (2, 3,4)
print(tuple1[:3])   # Output: (1, 2, 3)

#Iteration
for num in tuple1:
    print(num) # Output: 1 2 3 4 5 (each number on a new line)

#Delete
del tuple1  # Deletes the entire tuple

#Update
tuple1 = (1, 2, 3, 4, 5)
# tuple1[0] = 10  # This will raise a TypeError since tuples are immutable

#Methods
print(len(tuple1))  # Output: 5
print(tuple1.count(2))  # Output: 1 (counts the number of occurrences of 2 in the tuple)
print(tuple1.index(3))  # Output: 2 (returns the index of the first occurrence of 3 in the tuple)

#Concatenation
tuple3 = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 'a', 'b', 'c')

#Repetition
tuple4 = tuple2 * 3  # Output: ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

#Tuple Membership
print(1 in tuple1)  # Output: True
print(10 in tuple1)  # Output: False

#********************************************************************************************

#Dictionary
'''
A dictionary is a collection of key-value pairs that are unordered and changeable.
Dictionaries are defined using curly braces { } and each key-value pair is separated by a colon :.
'''

#Creation
dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}

#Accessing values
print(dict1['name'])  # Output: Alice
print(dict1.get('age'))  # Output: 30

#Iteration
for key in dict1:
    print(key)  # Output: name age city (each key on a new line)
for value in dict1.values():
    print(value)  # Output: Alice 30 New York (each value on a new line)
for key, value in dict1.items():
    print(f'{key}: {value}')  # Output: name: Alice age: 30 city: New York (each key-value pair on a new line)

#Delete
del dict1['age']  # Deletes the key 'age' and its associated value
del dict1  # Deletes the entire dictionary

#Update
dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict1['age'] = 31  # Updates the value associated with the key 'age' to 31
dict1['country'] = 'USA'  # Adds a new key-value pair to the dictionary

#Methods
print(len(dict1))  # Output: 4 (number of key-value pairs in the dictionary)
print(dict1.keys())  # Output: dict_keys(['name', 'age', 'city', 'country'])
print(dict1.values())  # Output: dict_values(['Alice', 31, 'New York', 'USA'])
print(dict1.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('country', 'USA')])
dict1.pop('city')  # Output: 'New York' (removes and returns the value associated with the key 'city')
print(dict1)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}  
dict1.clear()  # Output: {} (removes all key-value pairs from the dictionary)

#Dictionary Membership
print('name' in dict1)  # Output: True
print('age' in dict1)  # Output: True
print('city' in dict1)  # Output: False

#********************************************************************************************

#Set
'''
A set is a collection of unique items that are unordered and changeable.
Sets are defined using curly braces { } and can contain elements of different data types.
'''

#Creation
set1 = {1, 2, 3, 4, 5}
set2 = {'a', 'b', 'c'}  

#Accessing elements
# Sets do not support indexing, so you cannot access elements by index

#Iteration
for item in set1:
    print(item)  # Output: 1 2 3 4 5 (each item on a new line)

#Delete
del set1  # Deletes the entire set

#Update
set1 = {1, 2, 3, 4, 5}
set1.add(6)  # Output: {1, 2, 3, 4, 5, 6} (adds an element to the set)
set1.update({7, 8})  # Output: {1, 2, 3, 4, 5, 6, 7, 8} (adds multiple elements to the set)
set1.remove(2)  # Output: {1, 3, 4, 5, 6, 7, 8} (removes an element from the set)
set1.discard(10)  # Output: {1, 3, 4, 5, 6, 7, 8} (removes an element from the set if it exists, does nothing if it doesn't exist)  
set1.clear()  # Output: set() (removes all elements from the set)

#Set Membership
print(1 in set1)  # Output: True
print(10 in set1)  # Output: False  

#********************************************************************************************

#Array
'''
An array is a collection of items that are ordered and changeable.
In Python, the built-in list type can be used as an array, but it is not as efficient as arrays in other programming languages.
For more efficient array operations, we can use the array module or the NumPy library.
'''

#Using the array module
arr1 = array('i', [1, 2, 3, 4, 5])  # Creates an array of integers
print(arr1[0])  # Output: 1
arr1.append(6)  # Output: array('i', [1, 2, 3, 4, 5, 6]) (adds an element
arr1.insert(1,4) # Output: array('i', [1, 4, 2, 3, 4, 5, 6]) (inserts an element at a specific index)
arr1.remove(2)  # Output: array('i', [1, 4, 3, 4, 5, 6]) (removes an element from the array)
arr1.pop()  # Output: 6 (removes and returns the last element)
arr1.pop(1)  # Output: 4 (removes and returns the element at index 1)
print(arr1)  # Output: array('i', [1, 3, 4, 5]) (prints the array)
arr2 = array.array('i', arr1[1:3])  # Output: array('i', [3, 4]) (slices the array from index 1 to index 3)
print(arr1.index(4))  # Output: 3 (returns the index of the first occurrence of 4 in the array)
arr2.reverse()  # Output: array('i', [4, 3]) (reverses the array)


#Using the NumPy library
arr2 = np.array([1, 2, 3, 4, 5])  # Creates a NumPy array
print(arr2[0])  # Output: 1
arr2 = np.append(arr2, 6)  # Output: array([1, 2, 3, 4, 5, 6]) (adds an element to the array)
arr2 = np.delete(arr2, 1)  # Output: array([1, 3, 4, 5, 6]) (removes an element from the array)     
arr2 = np.insert(arr2, 1, 4)  # Output: array([1, 4, 3, 4, 5, 6]) (inserts an element at a specific index)
print(arr2)  # Output: array([1, 4, 3, 4, 5, 6]) (prints the array)
arr3 = arr2[1:3]  # Output: array([4, 3]) (slices the array from index 1 to index 3)
print(np.where(arr2 == 4))  # Output: (array([1, 3]),) (returns the indices of all occurrences of 4 in the array)
arr2 = np.flip(arr2)  # Output: array([6, 5, 4, 3, 4, 1]) (reverses the array)

#********************************************************************************************
#FUN BEGINS HERE

#Linked List
'''
A linked list is a linear data structure where each element (called a node) contains a value and a reference (or link) to the next node in the sequence.
In Python, we can define a linked list using a class for the nodes and a class for the linked list itself.
'''

#Creating a Node class and a LinkedList class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val)  # Output: prints the value of each node in the linked list
            current_node = current_node.next

#Creating a linked list and appending values
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()  # Output: 1 2 3 (each value on a new line)
#Structure of linkedlist node: (1,index of 2) -> (2,index of 3) -> (3,None)

#Removing a node from the linked list
def remove_node(linked_list, val):
    current_node = linked_list.head
    prev_node = None

    while current_node:
        if current_node.val == val:
            if prev_node:
                prev_node.next = current_node.next  # Bypass the current node
            else:
                linked_list.head = current_node.next  # Update head if the node to remove is the head
            return
        prev_node = current_node
        current_node = current_node.next
remove_node(linked_list, 2)
linked_list.print_list()  # Output: 1 3 (each value on a new line)
#Before removal: (1,index of 2) -> (2,index of 3) -> (3,None)
#After removal: (1,index of 3) -> (3,None)

#Removing a node from the linked list without access to the head
def remove_node_no_head(node):
    if node is None or node.next is None:
        return  # Cannot remove the node if it's the last node or if it's None

    next_node = node.next
    node.val = next_node.val  # Copy the value of the next node to the current node
    node.next = next_node.next  # Bypass the next node
#Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
# Before removal: (1,index of 2) -> (2,index of 3) -> (3,None)
remove_node_no_head(linked_list.head.next)  # Removing the node with value 2
linked_list.print_list()  # Output: 1 3 (each value on a new line)
# After removal: (1,index of 3) -> (3,None)


