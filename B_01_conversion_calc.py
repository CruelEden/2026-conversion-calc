# store values
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

# displays instructions
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")
def instructions():
    statement_generator("instructions", "-")
    print('''
instructions go here.
- instruction 1
- instruction 2
- etc   
    ''')
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")
if want_instructions == "":
    instructions()

# Main





# need for later
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