# 1. Create a list of five numbers and append a new number to it. Print the updated list.
nums = [1, 2, 3, 4, 5]  
# print('nums: ', nums)
nums.append(6)  # Append
print('nums: ', nums)
print('-' * 20)


# 2. Extend a list [1, 2, 3] with another list [4, 5, 6]. Print the result.
list1 = [1, 2, 3]  # List 
# print('list1:', list)
list1.extend([4, 5, 6])  # Extend
print('list1:  ', list)
print('-' * 20)


# 3. Insert the string "Python" at index 2 in the list ["Java", "C++", "JavaScript", "Ruby"]. 
list2 = ["Java", "C++", "JavaScript", "Ruby"]
# print('list2: ', list2)
list2.insert(2,"Python") #insert
print('list2: ', list2)
print('-' * 20)


# 4. Remove the first occurrence of the number 10 from the list [10, 20, 30, 10, 40].
list3 = [10, 20, 30, 10, 40]
list3.remove(10) #remove
print('list3: ', list3)


# 5. Use the pop() method to remove the last element from [100, 200, 300, 400] and print the modified list.
list4 =  [100, 200, 300, 400] 
list4.pop() #Pop
print('list4: ', list4)
print('-' * 20)


# 6. Count how many times the number 5 appears in the list [5, 10, 5, 20, 5, 30].
list5 = [5, 10, 5, 20, 5, 30]
# print('list5: ', list5)
print(list5.count(5))  # Count
print('-' * 20)


# 7. Sort the list [9, 1, 8, 3, 5] in ascending and descending order.
list6 = [9, 1, 8, 3, 5]
list6.sort()
print('ascending: ', list6)
list6.sort(reverse=True)
print('descending : ', list6)


# 8. Reverse the list ['apple', 'banana', 'cherry'] using the reverse() method.
list7 = ["apple", "banana", "cherry"]
# print('list7: ', list7)
list7.reverse()
print('list7 reversed: ', list7)
print('-' * 20)


# 9 Create a copy of the list [1, 2, 3, 4, 5] and store it in another variable. Modify the copied list and print both lists
list8 = [1,2,3,4,5]
copied_list = list8.copy()
print('copied_list: ', copied_list)
copied_list.pop()
print('updated copy list: ', copied_list)
print("Original list:", list8)
print('-' * 20)


# 10 Clear all elements from a list [“hello”, “world”, “python”] using the clear() method.
list9 = ['hello', 'world', 'python']
list9.clear()
print('list9: ', list9)
print('-' * 20)


# 11. Create a tuple with 5 different fruits and print the third fruit.
tuple = ("apple", "banana", "cherry","mango","orange")  # Tuple
print('tuple(3): ', tuple[2])
print('-' * 20)


# Convert the tuple (10, 20, 30, 40, 50) into a list, remove the number 30, and convert it back into a tuple.
tuple2 = (10, 20, 30, 40, 50)
print('tuple2: ', tuple2)
list10 = list(tuple2)
print('list10: ', list10)
list10.remove(30)  # Remove
print('list10 updated: ', list10)
tuple2=list10
print('tuple2 updated: ', tuple2)
print('-' * 20)

# 16. Write a function that takes a list and returns a new list with all even numbers removed.
numbers = [1,2,3,4,5,6,7,8,9,10]           # List of numbers
def fun(numbers):                          # created a function that accepts array of numbers
    odd_array=[]                           
    for x in numbers[:]:                   # for each item in numbers 
        if x%2 !=0:                        # check if there is no zero in reminder if divided by 2
            # print("items: ",x)           # if there is no zero it means it is odd
            odd_array.append(x)            # now  finally push that into our new array
    print('odd_array: ', odd_array)        # here we go... 
    return 
fun(numbers)
print('-' * 20)


# 17. Create a function that accepts a list and returns a new list with elements sorted in descending order without using the sort() method
real = [5,10,2,3,9,20,16,7,8,9,10]           
def func(real):                         
    descending=[]
    print(real)
    ascending = set(real)
    print('ascending: ', ascending)
    converted_into_list = list(ascending)
    ascending= converted_into_list
    for nums in ascending:
        descending.append(nums)
    print('descending: ', descending[::-1])

    return 
func(real)
print('-' * 20)


# 18. Given a list of numbers, write a program to remove all duplicate elements and print the unique elements.
numbers = [5,10,2,3,9,20,16,7,8,9,10]
print('unique: ' , set(numbers))  # set() removes duplicates
print('-' * 20)


# 19. Given a tuple of names (“Alice”, “Bob”, “Charlie”, “Alice”, “David”), convert it into a list, remove duplicates, and convert it back to a tuple.
tuple19 = ('Alice', 'Bob', 'Charlie', 'Alice', 'David')
arr = list(tuple19)
print('Converted into a list: ', arr)
arr = tuple(set(arr)) 
print('Back to tuple: ', arr)


# 20. Create a program that takes a list of mixed data types (int, str, float) and separates integers into one list, strings into another, and floats into another
mixed_list = [42,9,"Me",99.92, "apple", 2.718, ]
numbers=[]
decimals=[]
strgs=[]
for item in mixed_list:
    if isinstance(item, int):
        numbers.append(item)
print('numbers: ', numbers)
for item in mixed_list:
    if isinstance(item, float):
        decimals.append(item)
print('decimals: ', decimals)
for item in mixed_list:
    if isinstance(item, str):
        strgs.append(item)
print('strgs: ', strgs)
