distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

# Get amount and units (assume they are valid)
amount = float(input("How much? "))
from_units = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get the standard value...
multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

# Divide to get our desired value
divide_by = distance_dict[from_units]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_units} ")