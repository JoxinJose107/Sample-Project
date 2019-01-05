
# ***** 2D Lists and Nested Loops*****

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0])
print("Printing the entire list: ")
for row in number_grid:
    print(row)

print("Nested for loops: ")
for row in number_grid:
    for col in row:
        print(col)