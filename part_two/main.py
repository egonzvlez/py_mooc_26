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
age: int = int(input("What is your age? "))
if age >= 13:
    print(f"Ok, you're {age} years old")
elif age >= 0 and age < 13:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")
