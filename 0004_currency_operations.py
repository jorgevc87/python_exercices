from fractions import Fraction
from decimal import Decimal # importar libreria de trabajo con decimales
import cmath

tax_rate = Decimal('7.25')/Decimal(1000) # cast string a Decimal

purchase_amount = Decimal('2.95')

print(f'${tax_rate * purchase_amount}') #Mostrar el decimal en la consola

# Fraction calculations
"""
When we´re doing calculations that have exact fractions values, we
can use the facttions module to create rational numbers

from fractions import fractions

"""

sugar_caps = Fraction('2.5')
scale_factors = Fraction(5/8)

sugar_caps * scale_factors

Fraction(25,16)

print(f"sugar_caps: ${sugar_caps}")
print(f"scale_factors: ${scale_factors}")
print(f"Fraction(25,16): ${Fraction(25,16)}")

# Aproximations
answer = (19/1555) * (19/1555)
print(f"answer: ${answer}")

complex_number = cmath.sqrt(-2)
print(f"complex_number: ${complex_number}")

total_seconds = 7385
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

print(f"total_seconds: {total_seconds}")
print(f"hours: {hours}")
print(f"remaining_seconds: {remaining_seconds}")




