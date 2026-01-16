"""Problem 1
Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.
"""
# word: str = input("Please type in a word: ")
# word_len: int = len(word)

# if word_len >1:
#     print(f"There are {word_len} letters in the word {word}")
# print("Thank you!")


"""Problem 2
Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. 
Use the Python int function. You can assume the number given by the user is always greater than zero.
"""
# number: float = float(input("Please type in a number: "))
# int_number: int = int(number)
# dec_number: float = number - int_number
# print(f"Integer part: {int_number}")
# print(f"Decimal part: {dec_number}")


"""Problem 3
Please write a program which asks the user for their age.
The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.
"""
# age: int = int(input("How old are you? "))
# if age >= 18:
#     print("You are of age!")
# else:
#     print("You are not of age!")


"""Problem 4
Please write a program which asks for two integer numbers. 
The program should then print out whichever is greater. 
If the numbers are equal, the program should print a different message.
"""
# num_one: int = int(input("Please type in the first number: "))
# num_two: int = int(input("Please type in another number: "))
# if num_one > num_two:
#     print(f"The greater number was: {num_one}")
# elif num_one < num_two:
#     print(f"The greater number was: {num_two}")
# else:
#     print("The numbers are equal!")



"""Problem 5
Please write a program which asks for the names and ages of two persons.
The program should then print out the name of the elder.
"""
# print("Person 1: ")
# person_one_name:str = input("Name: ")
# person_one_age: int = int(input("Age: "))
# print("Person 2: ")
# person_two_name:str = input("Name: ")
# person_two_age: int = int(input("Age: "))
# #Comparison
# if person_one_age > person_two_age:
#     print(f"The elder is {person_one_name}")
# elif person_two_age > person_one_age:
#     print(f"The elder is {person_two_name}")
# else:
#     print(f"{person_one_name} and {person_two_name} are the same age")


"""Problem 6
Please write a program which asks the user for two words. 
The program should then print out whichever of the two comes alphabetically last.
You can assume all words will be typed in lowercase entirely.
"""
# word_one: str = input("Please type in the 1st word: ")
# word_two: str = input("Please type in the 2nd word: ")
# if word_one == word_two:
#     print("You gave the same word twice.")
# elif word_one > word_two:
#     print(f"{word_one} comes alphabetically last.")
# else:
#     print(f"{word_two} comes alphabetically last.")

"""Problem 7
Please write a program which asks for the user's age.
If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.
"""
# age: int = int(input("What is your age? "))
# if age >= 5:
#     print(f"Ok, you're {age} years old")
# elif age >= 0 and age < 5:
#     print("I suspect you can't write quite yet...")
# else:
#     print("That must be a mistake")



"""Problem 8
Please write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.
# """
# user_name: str = input("Please type in your name: ")
# if user_name == "Huey" or user_name == "Dewey" or user_name == "Louie":
#     print("I think you might be one of Donald Duck's nephews.")
# elif user_name == "Morty" or user_name == "Ferdie":
#     print("I think you might be one Mickey Mouse's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")


"""Problem 9
The table below outlines the grade boundaries on a certain university course. 
Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.
"""
# user_points: int = int(input("How many points [0-100]: "))
# if user_points < 0:
#     grade = "impossible!"
# elif user_points >= 0 and user_points <= 49:
#     grade = "fail"
# elif user_points >= 50 and user_points <= 59:
#     grade = "1"
# elif user_points >= 60 and user_points <= 69:
#     grade = "2"
# elif user_points >= 70 and user_points <=79:
#     grade = "3"
# elif user_points >= 80 and user_points <= 89:
#     grade = "4"
# elif user_points >= 90 and user_points <= 100:
#     grade = "5"
# else:
#     grade = "impossible!"
# print("Grade:", grade)


"""Problem 10
Please write a program which asks the user for an integer number.
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.
"""
# number: int = int(input("Number: "))
# if number % 3 == 0:
#     if number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)


"""Problem 11
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.
Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.
"""
# year: int = int(input("Please type in a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("That year is a leap year.")
#         else:
#             print("That year is not a leap year.")
#     else:
#         print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")


"""Problem 12
Please write a program which asks the user for three letters. 
The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
You may assume the letters will be either all uppercase, or all lowercase.
# """
# first_letter: str = input("1st letter: ")
# second_letter: str = input("2nd letter: ")
# third_letter: str = input("3rd letter: ")

# if (first_letter < second_letter and first_letter > third_letter) or (first_letter > second_letter and first_letter < third_letter):
#     print("The letter in the middle is", first_letter)
# elif (second_letter < first_letter and second_letter > third_letter) or (second_letter > first_letter and second_letter < third_letter):
#     print("The letter in the middle is", second_letter)
# else:
#     print("The letter in the middle is", third_letter)


"""Problem 13
Please write a program which calculates the correct amount of tax for a gift from a close relative. 
Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - 
you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.
"""
# Write your solution here
# gift_value: int = int(input("Value of gift: "))
# tax_low_limit: int = 0
# bracket: int = 0
# tax_percentage: float = 0

# if gift_value < 5000:
#     print("No tax!")
# elif gift_value >= 5000 and gift_value < 25000:
#     tax_low_limit += 100
#     bracket += 5000
#     tax_percentage += 0.08
# elif gift_value >= 25000 and gift_value < 55000:
#     tax_low_limit += 1700
#     bracket += 25000
#     tax_percentage += 0.10
# elif gift_value >= 55000 and gift_value < 200000:
#     tax_low_limit += 4700
#     bracket += 55000
#     tax_percentage += 0.12
# elif gift_value >= 200000 and gift_value < 1000000:
#     tax_low_limit += 22100
#     bracket += 200000
#     tax_percentage += 0.15
# else:
#     tax_low_limit += 142100
#     bracket += 1000000
#     tax_percentage += 0.17
# if gift_value != 0 and gift_value >5000:    
#     equation: float = (tax_low_limit + (gift_value - bracket) * tax_percentage)
#     print(f"Amount of tax: {equation}euros")  


"""Problem 14
Let's create a program along the lines of the example above.
This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no".
Then the program should print out "okay then" and finish. Please have a look at the example below.
"""
# while True:
#     print("hi")
#     cont: str = input("Shall we continue?")
#     if cont == "no":
#         print("okay then")
#         break


"""Problem 15
Please write a program which asks the user for integer numbers.
If the number is below zero, the program should print out the message "Invalid number".
If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
In either case, the program should then ask for another number.
If the user inputs the number zero, the program should stop asking for numbers and exit the loop.
"""
# import math
# while True:
#     number: int = int(input("Please type in a number: "))
#     if number < 0:
#         print("Invalid number")
#     elif number == 0:
#         print("Exiting...")
#         break
#     elif number > 0:
#         print(math.sqrt(number))

"""Problem 16
Please write a program which asks the user for a password. The program should then ask the user to type in the password again. 
If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.
"""
# password: str = input("Password:")
# while True:
#     repeat_password: str = input("Repeat password: ")
#     if password == repeat_password:
#         print("User account created!")
#         break
#     else:
#         print("They do not match!")


"""Problem 17
Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
The program should then print out the number of times the user tried different codes.
"""
# attempts: int = 0
# while True:
#     pin = int(input("PIN: "))
#     attempts += 1
    
#     if pin == 4321:
#         if attempts == 1:
#             print("Correct! It only took you one single attempt!")
#             break
#         else:
#             print(f"Correct! It took you {attempts} attempts")
#             break
#     else:
#         print("Wrong")


"""Problem 18
Please write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:
"""
# year: int = int(input("Year: "))
# start_year: int = year
# while True:
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 if year == start_year:
#                     year += 1
#                     continue

#                 else:
#                     print(f"The next leap year after {start_year} is {year}")
#                     break
#             else:
#                 year += 1
#         else:
#             if year == start_year:
#                 year += 1
#                 continue
#             else:
#                 print(f"The next leap year after {start_year} is {year}")
#                 break
#     else:
#         year += 1


"""Problem 19
Please write a program which keeps asking the user for words.
If the user types in end, the program should print out the story the words formed, and finish.
"""
# story: str = ""
# previous_word = ""
# while True:
#     word: str = input("Please type in a word: ")
#     if word == "end" or word == previous_word:
#         print(story)
#         break
#     else:
#         story += word + " "
#         previous_word = word


"""Problem 20
"""

print("Please type in integer numbers. Type in 0 to finish.")
number_count: int = 0
number_sum: int = 0
pos_num: int = 0
neg_num: int = 0
while True:
    number: int = int(input("Number: "))
    if number < 0:
        neg_num += 1
    elif number > 0:
        pos_num += 1

    if number == 0:
        print(f"Numbers typed in {number_count}")
        print(f"The sum of the numbers is {number_sum}")
        print(f"The mean of the numbers is {number_sum / number_count}")
        print(f"Positive numbers {pos_num}")
        print(f"Negative numbers {neg_num}")
        break
    else:
        number_count += 1
        number_sum += number
