# 8-15. Printing Models: Put the functions for the example print_models.py
# in a separate file called printing_functions.py. Write an import statement
# at the top of print_models.py, and modify the file to use the imported
# functions.

from printing_functions import *

unprinted_designs = ['iphone x case', 'lungs', 'kidneys']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# If you are writing a function and notice the function is 
# doing too many different tasks, try to split the code into
# two functions.