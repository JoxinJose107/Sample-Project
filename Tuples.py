

#******Tuples**********

# Tuples is a kind of data structure which basically means it is a container which store values. Tuple is very similar to lists. We can store multiple peaces of information. List is created by [] brackets but tuple is created by () paranthesis.

# Tuples are immutable. Once created we cannot change or modify  the tuple.

coordinates=(4,5)
#coordinates[1]=10   *error: tuple cannot be modified once created.
print(coordinates[1])

# Practically tuples are used for the data that is never going to change.

# We can create the list of tuples:
coordinates1=[(4,5),(6,10),(3,3)]
print(coordinates1)