# see if it's a valid number
from http.client import responses
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}


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


# Main Routine Goes Here
while True:
    amount = num_check("how much? ") or float(input("how much? "))
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





