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