""" def is_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd" """

def calculate_tip(bill, service):
    if service == "bad":
        tip_percentage = 0
        print ("You should tip nothing")
    elif service == "okay":
        tip_percentage = 0.15
        print ("You should tip 15%")
    elif service == "good":
        tip_percentage = 0.20
        print ("You should tip 20%")
    elif service == "great":
        tip_percentage = 0.25
        print ("You should tip 25%")
    else:
        raise ValueError("Invalid service rating")

    tip = bill * tip_percentage
    return tip
