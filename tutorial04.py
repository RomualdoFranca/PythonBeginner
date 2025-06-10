couses = ['History', 'Math', 'Phisics', 'CompSci'] # List

# prints out our entire list
print(couses)
# how many values are in the list
print(f"How many values are in the list: {len(couses)}")
#accessign values individually
print(f"Print a first element of the list: {couses[0]}")
#access last value of the list using negative index
print(couses[-1])
#access a range of value
#first index is the starting point and the second index is the stopping point
print(f"Access a range of value: {couses[0:2]}") #access at index zero and go to, but not including, index 2

#if we don't put the second index, we want to go all the way to the end of the list
print(f"No second index: {couses[2:]}")
#slicing
#add an item to our list
couses.append("Art")#add an item to the end of the list
print(couses)
#add an item to a specific location
#first argument: it takes the index where you want the to insert the value
#second argument: the value it's self
couses.insert(0,"Sociology")
print(couses)

#add a multiple values
couses_2 = ['Music', 'Pedagogy']
couses.extend(couses_2)
print(f"Add multiple values: {couses}")

#remove some values
couses.remove('Art') #remove an specific value
print(couses)
couses.pop()#remove the last value
print(couses)
#grabbed the value that was popped off of the list
#Ideia de implementação:
# recebe input de itens e guarda na lista
popped = couses.pop()
print(popped)

#sort our list
#reverse a list
couses.reverse()
print(f"Print out list in reverse: {couses}")
#sorted in  alphabetical order or ascendant order
couses.sort()
print(couses)
#reverse order altering the original list
couses.sort(reverse=True)
print(couses)
list_numbers = [9,3,6,12,15,0]
print(f"Original list: {list_numbers}")
#ordeded list altering the original
# list_numbers.sort()
# print(list_numbers)
#reverse order without altering the original list
sorted_numbers =  sorted(list_numbers)
print(f"Order copy {sorted_numbers}")
print(list_numbers)

