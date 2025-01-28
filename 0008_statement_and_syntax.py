import math
# another way to define imports
from math import (
    sin,cos,tan,sqrt,log,frexp
)

example_value1 = (63/25) * (17/15*math.sqrt(5))/(7+5*math.sqrt(5))
example_value2 = (63/25) * (17/15*math.sqrt(5))/(7+5*math.sqrt(5))

print(f"example_value1: {example_value1}")
print(f"example_value2: {example_value2}")
print(f"example_value1==example_value2 -> {example_value1==example_value2}")

message_text = (
    f'the internal representation '
    #f'is {mantissa_whole:d}'
)


messgae_example = "This a example of *formatted* text"

print(f"messgae_example: {messgae_example}")


"""
If.... Elif....

if weather == Weather.RAIN and plan == Plan:GO_OUT:
    bring("unbrella")
else
    bring("sunglasses")

It may not be inmediately obvious, but we've ommited a number of possible 
alternatives. The weather and plan variables have four different combi_
nations of values. One of the conditions is stated explicitedly, the other
three are asumed:

"""
die_1 = 1
die_2 = 2


dice = die_1 + die_2

if dice in (2,3,12):
    print("game.craps()")
elif dice in (7, 11):
    print("game.winner()")
elif dice in (4,5,6,8,9,10):
    print(f"game.point({dice})")
else:
    raise Exception("Design problem")

"""
This extra "else" gives us a way to positively identify when a logic problem
is found.
"""











