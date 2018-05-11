# 8-16. Imports: Using a program you wrote that has one function in it,
# store that function in a separate file. Import the function into your
# main program file, and call the function using each of these approaches:

from make_great_magician import show_magicians, make_great

magicians = ['Ken Dog', 'Kenneth', 'Ken']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)