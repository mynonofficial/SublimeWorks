"""a for address b is for book"""
myDict={
"Cemile":6320459615,
"Kamile":5320459685,
"Halime":4320459645,
"Kerime":3320459685,
'Spartan':262045967,
}

for name, phones in myDict.items():
    print('The original Contact {} at {}'.format(name, phones))

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Kerime's phone number is = ",myDict["Kerime"])

if "Semile" in myDict:
	print("Yes, Semile is in adress book")
else:
	print("No, Semile is not in address book")

#for lines in myDict:
#	print(lines) #prints only one line
myDict['Semile'] = 9320459685
myDict['Fadime'] = 7320459685

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for name, phones in myDict.items():
    print('Contact {} at {}'.format(name, phones))

del myDict["Semile"]
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("In address book {} are found ".format(myDict))


print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#create anotfer sictionary and then update it
myDict2={"Serime":1120459685}
myDict.update(myDict2)

print("In address book {} are found ".format(myDict))