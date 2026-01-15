
"""
Problem 1:
Please write a program which estimates a user's typical food expenditure.
The program asks the user how many times a week they eat at the student cafeteria.
Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
Based on this information the program calculates the user's typical food expenditure both weekly and daily.
"""

# times_at_cafeteria: int = int(input("How many time a week do you eat at the student cafeteria? "))
# lunch_price: float = float(input("The price of a typical student lunch? "))
# grocerie_weekly: float = float(input("How much money do you spend on groceries in a week? "))

# daily_spending: float = ((times_at_cafeteria * lunch_price) + grocerie_weekly) / 7
# weekly_spending: float = (times_at_cafeteria * lunch_price) + grocerie_weekly
# print("Average food expenditure: ")
# print(f"Daily: {daily_spending} euros")
# print(f"Weekly: {weekly_spending} euros")


""" (Incomplete)
Problem 2:
Please write a program which asks for the number of students on a course and the desired group size. 
The program will then print out the number of groups formed from the students on the course. 
If the division is not even, one of the groups may have fewer members than specified.
"""

# total_students: int = int(input("How many students on the course? "))
# group_size: int = int(input("Desired group size? "))
# number_of_groups: int = total_students // group_size
# print(f"Number of groups formed: {number_of_groups}")


"""
Problem 3:
Please write a program which asks the user for an integer number. 
The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
"""

# orwell_num: int = int(input("Please type in a number: "))
# if orwell_num == 1984:
#     print("Orwell")


"""
Problem 4:
Please write a program which asks the user for an integer number. 
If the number is less than zero, the program should print out the number multiplied by -1. 
Otherwise the program prints out the number as is. 
Please have a look at the examples of expected behaviour below.
"""

# user_input: int = int(input("Please type in a number: "))
# if user_input < 0:
#     print(f"The absolute value of this number is {user_input * -1}")
# else:
#     print(f"The absolute value of this number is {user_input}")

"""Problem 5:
Please write a program which asks for the user's name. 
If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. 
The price of a single portion is 5.90.
"""

# user_name: str = input("Please tell me your name:")
# cost_per_portion: float = 5.90

# if user_name == "Jerry":
#     print("Next please!")
# else:
#     portions: int = int(input("How many portions of soup: "))
#     total_cost = portions * cost_per_portion
#     print(f"The total cost is {total_cost}")
#     print("Next please!")

"""
Problem 6:
Please write a program which asks the user for an integer number. 
The program should then print out the magnitude of the number according to the following examples.
"""

user_number: int = int(input("Please type in a number:"))

if user_number < 1000:
    print("This number is smaller than 1000")
if user_number < 100:
    print("This number is smaller than 100")
if user_number < 10:
    print("This number is smaller than 10")

print("Thank you!")