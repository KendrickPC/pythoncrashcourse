# 9-13. OrderedDict Rewrite: Start with Exercise 6-4, where you used a
# standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the
# order in which key-value pairs were added to the dictionary.

# pep8 verified
from collections import OrderedDict

glossaryWord = OrderedDict()

glossaryWord['for loop'] = 'A control flow statement for specifying \
iteration, which allows code to be executed repeatedly.'
glossaryWord['lists'] = 'Lists are enclosed in square brackets [ ] and \
each item is separated by a comma. Lists are collections of items where \
each item in the list has an assigned index value.'
glossaryWord['dictionaries'] = 'A dictionary is an associative array (also \
known as hashes). Any key of the dictionary is associated (or mapped) to a \
value.'
glossaryWord['tuples'] = 'A tuple is a sequence of immutable Python objects.'
glossaryWord['attribute'] = 'An attribute is a specification that defines \
a property of an object, element, or file.'
glossaryWord['nested scope'] = 'The ability to refer to a variable in an \
enclosing definition.'
glossaryWord['object oriented'] = 'Programming typified by a data-centered \
(as opposed to a function-centered) approach to program design.'
glossaryWord['strings'] = 'One of the basic types in Python that store text.'
glossaryWord['mapping'] = 'A container object (such as dict) that supports \
arbitrary key lookups using __getitem__.'

for wordIndex, definition in glossaryWord.items():
    print("\n\t" + wordIndex.title() + ": " + definition)
