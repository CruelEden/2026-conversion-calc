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

        response = input("Unit type: ")

        # check exit code
        if response == "xxx":
            return response

        elif response in ['distance','d']:
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

        print(f"you picked {unit}")
        break

def mass():

    while True:

        print(f"you picked {unit}")
        break

def time():

    while True:

        print(f"you picked {unit}")
        break

def volume():

    while True:

        print(f"you picked {unit}")
        break

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