# see if it's a valid number

def num_check(question):

    error = "please enter number that is more then zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
            if response == "xxx":
                return response

        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0, 20):
    amount = num_check("how much? ")

while True:
    if amount =="xxx":
        break
