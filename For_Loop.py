#*****For Loops*******
#For loops are special loops in python which helps us to loop over different collection of items.

for letter in "Joxin":
    print(letter)


a="Ronaldo"
for letter in a:
    print(letter)



# Using array
array=["Cristiano Ronaldo","Gareth Bale","Luka Modric"]
for i in  array:
    print(i)


# Printing numbers:
for i in range(10):
    print(i)

# Printing numbers between a certain range
for i in range(3,10):
    print(i)

# Printing an array using range()

arr=["a","b","c"]
for i in range(len(arr)):
    print(arr[i])


for i in range(5):
    if i==0:
        print("First Iteration")
    else:
        print("Not first Iteration")