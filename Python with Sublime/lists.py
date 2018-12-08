thislist=["hello man",12548696,"We go out"]
print(type(thislist))
print(thislist[0])
print(thislist)
print("######Writing diff #######")
for items in thislist:
	print(items)

#lets see operations in a list
print("###### operations in the list #######")
#Change the second item:
thislist[1]=365489652
print(thislist)
#check if the item included
if "We dont go out" in thislist:
	print("Yes found")
else:
	thislist.append("Cherry")
	print(thislist)
#adding the list where we want
thislist.insert(0,"Apple")
print(thislist)

thislist.remove("hello man")
print(thislist)

# we can use pop() to remove as well
thislist.pop(2)
print(thislist)

#we can use del to delete all the list or some element

del thislist[0]
print(thislist)

#The clear() method empties the list:
thislist.clear()
print(thislist)

#Using the list() constructor to make a List:

thislist = list(("orange", "lemon", "cherry")) 
print(thislist)

"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""