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


def unit_type():

   while True:

        response = input("unit type: ")

        # check exit code
        if response == "xxx":
            return response

        if response in 'distance':
            return "distance"

        if response in 'mass':
            return "mass"

        if response in 'time':
            return "time"

        if response in 'volume':
            return "volume"

        else:
            print("Please enter a valid unit")


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
