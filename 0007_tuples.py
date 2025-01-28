"""
What's the best way to represent simple (x,y) and (r,g,b)
groups of values?

GETTING READY
In the String parsing with regular expressions recipe, we skipped over 
and interesting data structure.
"""

import re
from fractions import Fraction
from typing import NamedTuple

ingredient_pattern = re.compile(r'')
ingredient = "kumquat: 2 cups"
match = ingredient_pattern.match(ingredient)

match.groups()
('kumquat','2','cups')

my_data = ('Rice', Fraction(1/4), 'cups')

print(my_data)
print(type(my_data))

# Special case
one_tuple = ('item',)

print(f"len(one_tuple): {len(one_tuple)}")

# accessing items in a tuple
my_tuple = (12,3,True,"exercise")

print(f"my_tuple[1]: {my_tuple[1]}")
print(f"my_tuple[2]: {my_tuple[2]}")

t = ('kumquat','2','cups')

# Operations that we can perform
len(t) # 3
t.count('2') # 1
t.index('cups') # 2
t[2] # 'cups'

# Does a particular value exists in the tuple ?
'Rice' in t  # False

# NamedTuple
class Ingredient(NamedTuple):
    ingredient: str
    amount: str
    unit: str

item_2 = Ingredient('Kumquat', '2', 'cups')

#Another NamedTuple
class IngredientF (NamedTuple) :
    ingredient: str
    amount: Fraction
    unit: str

item_3 = IngredientF('Kumquat', Fraction(2), 'cups')

"""
With item_3, we can do mathematical operations because has
a numeric field.
"""

print(f"item_3-> {item_3.ingredient} double: {item_3.amount * 2}")














