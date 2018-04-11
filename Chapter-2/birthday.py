# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)

# TypeError: Can't convert 'int' object to str implicitly
# TypeError: cannot concatenate 'str' and 'int' objects

age = 25
message = "Happy " + str(age) + "rd Birthday!"
print(message)