
#****Working with Lists in Python*******
# Lists are essentially a strucure that we can use inside python that can store and manage large amount of data.
# Lists can have strings, numbers and boolean.

football=["Cristiano Ronaldo","Lionel Messi","Zlatan Ibrahimovic","Wayne Rooney","Paul Pogba"]
print(football[0])

# We can use -ve indexing if we want to access the items from the back of the list.

print(football[-1])  

# Index position of the item at the beginning of the list is 0 and the index position of the item at the back of the list is -1.

# To access items after a specific index
print(football[1:]) # Items indexed from 1 and after will be printed.

# To access items within a range from the list.
print(football[1:3]) # Item indexed at 3 wont be printed.

# To modify values inside the list
football[1]="Juan Mata"
print("The modified list is: \n"+str(football))


# List Functions
# 1) extend() function append a list with another list.

#kit_number=[7,8,9,10,6]
#football.extend(kit_number)
print(football)

# 2) append() function is used to add another item to the end of the list.

football.append("Rashford")
print(football)

# 3) insert() function is used to insert an item into the middle of the list. It takes two parameters: i) the index value ii) the item to be inserted
football.insert(1,"Gareth Bale")
print(football)

# 4) remove() function is used to remove an item from the list.

football.remove("Rashford")
print(football)

# 5) clear() function is used to empty the entire list
   #football.clear()
   #print(football)

# 6) pop() function removes the list element from the list

football.pop()
print(football)

## To check whether an element is present in the list, use index() function. it returns the index value of the item else returns error saying "item not in list"

# 7) count() function returns the count of an element in the list.
print(football.count("Cristiano Ronaldo"))

# 8) sort() function is used to sort the items in the list in ascending order
football.sort()
print(football) # The same applies for the numbers also

# 9) reverse() function reverses the order of the list.

football.reverse()
print(football)

# 10) copy() function copies the items of one list into another
# football2=football.copy()
# print(football2)