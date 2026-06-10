# Store values


distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001,
}


mass_dict = {
    "mg": 1000,
    "g": 1,
    "kg": .001,
    "t": .000001,
}


time_dict = {
    "ms": 3600 * 1000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "d": 1 / 24,
    "month": 1 / 168,
    "y": 1 / (24 * 365 + 6 + 9 / 60)  # it accounts for leap year
}


volume_dict = {
    "mL": 1000,
    "L": 1,
    "kL": .001,
    "ML": .000001,
}


# main
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