from random import choice 

class ParkingMeter:

    rands = (1, 2, 5, 10, 20, 50, 100, 200) # Rand denominations.
    due = [0, 10, 25, 50, 75] # Money due for time.
    unsettled = choice(due) # money owed for parking.
    time = ["15 min", "1 hour", "2 hours", "3 hours", "4+ hours"] # Time slotes.

    def meterFunction(money, owed):
        if (money >= owed):
            if (money != owed):
                change = (money - owed)
                index = 6
                print("Collect your change: R", (money - owed))
                while ((change > 0) and (index > - 1)):
                        if (ParkingMeter.rands[index] <= change):
                            print(">> R ", ParkingMeter.rands[index]) # Money given out in Rand deniminations.
                            change -= ParkingMeter.rands[index]
                        else:
                            index -= 1
            print("Collect ticket below. Enjoy your day.")
            return 0 # Money owed returned (R0).
        else:
            print("Money owed: R", (owed - money))
            return (owed - money) # Money owed returned.

if __name__ == "__main__":
    ParkingMeter.unsettled
    print("Money owed: R", ParkingMeter.unsettled)
    print("time -> ", ParkingMeter.time[ParkingMeter.due.index(ParkingMeter.unsettled)])
    while (ParkingMeter.unsettled):
        try: # Input checks.
            userIn = int(input("Enter an amount to input: R"))
            if (userIn in ParkingMeter.rands):
                ParkingMeter.unsettled = ParkingMeter.meterFunction(userIn, ParkingMeter.unsettled)
        except ValueError as e:
            print("Input a valid South African Rand.")
            continue

'''
    Above is my parking meter function.
    The Parking meter only accepts Rands and outputs Rands.
    Time is randomly chosen from a list of 5 available time slots.
    The time slots affect the amount of money owed for parking.
    Change is given out if the money (parameter 1) given is greater than money owed (parameter 2).
    Change is given out in Rands from largest Rand denomination due change to the smallest denomination due.
    The largest denomination due is deducted from the change due and this will run till the change is R0.
    No change is given if the money given is equal to the money owed.
    If the money given is less than the money owed, the programme will continue to run deducting the input\
    from the money owed.

    Jonathan Pieczara
'''
