# Must use python3

# try:
#   print(5/0)
# except ZeroDivisionError:
#   print("\tYou can't divide by zero!")

# Using Exceptions to Prevent Crashes

print("Give me two numbers and let my AI divide it by two.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Check your math buddy.")
    else:
        print(answer)
