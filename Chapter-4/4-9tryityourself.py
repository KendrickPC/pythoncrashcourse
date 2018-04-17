# 4-3 Counting to Twenty:
count = [value for value in range(1,21)]
print(count)

# 4-4 One Million
count1million = [million for million in range(1, 1000001, 1)]
# print(count1million)

# 4-5 Summing a Million
print(min(count1million))
print(max(count1million))
print(sum(count1million))

# 4-6 Odd Numbers
oddNumbers = [odd + 1 for odd in range(0, 20, 2)]
print(oddNumbers)

# 4-7 Threes
listOfThrees = [threes + 0 for threes in range(3, 31, 3)]
print(listOfThrees)

# 4-8 Cubes
listOfCubes = [cubes ** 3 for cubes in range(1, 11, 1)]
print(listOfCubes)

# 4-9 List Comprehension Problem Solving Code Structure
listComprehensionOfCubes = [cubes ** 3 for cubes in range(1, 11, 1)]
print(listComprehensionOfCubes)