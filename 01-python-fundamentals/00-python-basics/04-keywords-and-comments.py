# 04. Keywords and Comments in Python

# 1. Single-line comment: Starts with '#'

"""
2. Multi-line comment (Docstring):
Triple quotes are used for multi-line documentation
and explanations within functions or modules.
"""

import keyword

# Python reserved keywords cannot be used as variable names
print("Total Python Keywords:", len(keyword.kwlist))
print("List of Keywords:")
for i, kw in enumerate(keyword.kwlist, start=1):
    print(f"{kw:<12}", end="\n" if i % 5 == 0 else " ")
print()
