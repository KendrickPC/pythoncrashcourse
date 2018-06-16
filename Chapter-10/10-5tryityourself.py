''' Must use python3 to execute this code. '''

# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a
# file that stores all the responses.

filename = 'programming_poll.txt'

poll_question = input("Why do you enjoy programming? ")

with open (filename, 'a') as file_object:
    file_object.write(poll_question + "\n")
