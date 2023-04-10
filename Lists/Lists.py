# Lists
# covers crucial list concepts and operations on Python.

# declaring a list
mylist = ["banana", "cherry", "apple"]
print(mylist)

# a list can contain different types of elements
       # can contain 2 of the same elements
mylist2 = [5, True, "apple", "apple"]    
print(mylist2)

# accessing an element in a list
item = mylist[1]
print(item)
      
# negative indexing
item = mylist[-1] # last item
print(item)
item = mylist[-3] # first item
print(item)

# item = mylist[3] # index out of range
# item = mylist[-4] # index out of range

# iterating over the list
for i in mylist:
    print(i)
print() 

# checking if an item in the list
if "banana" in mylist:
    print("banana is in the list")
else:
    print("banana is not in the list")


# length of a list
print(len(mylist))

# inserting a new item to a list
mylist.append("lemon") # inserts the item at the end of the list
print(mylist)

mylist.insert(1, "grappe") # inserts the item on a specific index
print(mylist)

print(len(mylist))

# removing an item from the list
item = mylist.pop() # removes the last item
print(item)
print(mylist)

item = mylist.remove("grappe") # removes a specific item
print(mylist)

# reversing a list
mylist.reverse()
print(mylist)

# sorting a list alphabetically
mylist.sort()
print(mylist)

# sorting a list numerically
numlist = [3,7,5,4,1,2]
print(sorted(numlist)) 
print(numlist)
numlist.sort()
print(numlist)


# different methods of declaring lists
zerolist = [0] * 5 
print(zerolist)

# assambling 2 lists
stringlist = ["banana", "cherry", "apple"]
new_list = stringlist + zerolist
print(new_list)

# slicing a list
print(new_list[1:4]) # prints elements 1-2-3
print(new_list[1:]) # prints elements starting from 1
print(new_list[:4]) # prints elements until 3

# stepping a list
print(new_list[::2]) # list stepping by 2 & only even indices
print(new_list[::3]) # list stepping by 3
print(new_list[1::2]) # only odd indices
print(new_list[::-1]) # reverses the list


# assigning a list to another list
list_org = [0,1,2]
list_cop = list_org
list_cop.append(3)
print(list_cop)
print(list_org)

# copying a list
list_org = [0,1,2]
list_cop = list_org.copy()
list_cop.append(3)
print(list_cop)
print(list_org)


# list comprehends
num_list = [2,3,4,5]
sqrnum_list = [i*i for i in num_list]
print(sqrnum_list)
