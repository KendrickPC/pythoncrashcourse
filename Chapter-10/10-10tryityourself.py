# Must use python3

import collections
# The re module provides regular expression matching operations
import re

# Specific word search for a file
and_words_search = re.findall(r'and', open('huckleberry_finn.txt').read().lower())
total_and_words = collections.Counter(and_words_search).most_common(10)
print('\nPrinting "and" words in Huckleberry Finn novel:')
print(total_and_words)

# Count top ten words in Huckleberry Finn Novel
huckleberry_finn_word_search = re.findall(r'\w+', open('huckleberry_finn.txt').read().lower())
huckleberry_finn_most_common_words = collections.Counter(huckleberry_finn_word_search).most_common(10)
print('\nPrinting top ten words in Huckleberry Finn novel:')
print(huckleberry_finn_most_common_words)

# Count top ten words in Tom Sawyer Novel
tom_sawyer_word_search = re.findall(r'\w+', open('tom_sawyer.txt').read().lower())
tom_sawyer_most_common_words = collections.Counter(tom_sawyer_word_search).most_common(10)
print('\nPrinting top ten words in Tom Sawyer novel:')
print(tom_sawyer_most_common_words)

# Count top ten words in Great Expectations Novel
great_expectations_word_search = re.findall(r'\w+', open('great_expectations.txt').read().lower())
great_expectations_most_common_words = collections.Counter(great_expectations_word_search).most_common(10)
print('\nPrinting top ten words in Great Expectations novel:')
print(great_expectations_most_common_words)
