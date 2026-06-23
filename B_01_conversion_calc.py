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

# Displays instructions
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


def num_check(question):
    error = "Please enter a number that is more than zero (or 'xxx' to exit)\n"
    while True:
        response = input(question).lower()  # Get input as text first

        # 1. Check for the exit code first
        if response == "xxx":
            return response

        # 2. If not exiting, try converting to a number
        try:
            response = float(response)

            # Check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def unit_type():
    while True:

        response = input("Unit type: ")

        # check exit code
        if response == "xxx":
            return response

        elif response in ['distance', 'd']:
            return "distance"

        elif response in ['mass', 'm']:
            return "mass"

        elif response in ['time', 't']:
            return "time"

        elif response in ['volume', 'v']:
            return "volume"

        else:
            print("Please enter a valid unit")

def distance():
    while True:

        amount = num_check("How much? ") or float(input("How much? "))
        if amount == "xxx":
            print("Exiting program. Goodbye!")
            break
        from_units = input("From unit? ")
        to_unit = input("To unit? ")

        # Multiply to get the standard value...
        multiply_by = distance_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = distance_dict[from_units]
        answer = standard / divide_by

        print(f"There are {answer} {to_unit} in {amount} {from_units} ")
        break

def mass():
    while True:

        amount = num_check("How much? ") or float(input("How much? "))
        if amount == "xxx":
            print("Exiting program. Goodbye!")
            break
        from_units = input("From unit? ")
        to_unit = input("To unit? ")

        # Multiply to get the standard value...
        multiply_by = mass_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = mass_dict[from_units]
        answer = standard / divide_by

        print(f"There are {answer} {to_unit} in {amount} {from_units} ")
        break

def time():
    while True:

        amount = num_check("How much? ") or float(input("How much? "))
        if amount == "xxx":
            print("Exiting program. Goodbye!")
            break
        from_units = input("From unit? ")
        to_unit = input("To unit? ")

        # Multiply to get the standard value...
        multiply_by = time_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = time_dict[from_units]
        answer = standard / divide_by

        print(f"There are {answer} {to_unit} in {amount} {from_units} ")
        break

def volume():
    while True:

        amount = num_check("How much? ") or float(input("How much? "))
        if amount == "xxx":
            print("Exiting program. Goodbye!")
            break
        from_units = input("From unit? ")
        to_unit = input("To unit? ")

        # Multiply to get the standard value...
        multiply_by = volume_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = volume_dict[from_units]
        answer = standard / divide_by

        print(f"There are {answer} {to_unit} in {amount} {from_units} ")
        break


# Main Routine Goes Here
while True:
    unit = unit_type()
    if unit == "xxx":
        break
    elif unit == "distance":
        dis_con = distance()
    elif unit == "mass":
        mas_con = mass()
    elif unit == "time":
        tim_con = time()
    elif unit == "volume":
        vol_con = volume()
