"""Problem 1
Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.
"""
# start_value: int = 2
# while start_value < 31:
#     print(start_value)
#     start_value += 2

"""Problem 2
Please write a program which asks the user for a number. 
The program then prints out all integer numbers greater than zero but smaller than the input
"""
# user_input: int = int(input("Upper limit: "))
# start: int = 1
# while start < user_input:
#     print(start)
#     start += 1

"""Problem 3
Please write a program which asks the user to type in an upper limit. 
The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1.
That is, the program prints out powers of two in order.
The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. 
No numbers greater than the limit should be printed.
"""
# num_limit: int = int(input("Upper limit: "))
# num_start: int = 1
# while num_start <= num_limit:
#     print(num_start)
#     num_start *= 2

"""Problem 4
Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
"""
# num_limit: int = int(input("Upper limit: "))
# num_base: int = int(input("Base: "))
# num_start: int = 1
# while num_start <= num_limit:
#     print(num_start)
#     num_start *= num_base

"""Problem 5
Please write a program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. 
The program should function as follows:
"""
# limit: int = int(input("Limit: "))
# start: int = 1
# total: int = 0
# while total < limit:
#     total += start
#     start += 1
# print(total)

"""Problem 6
Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed:
"""
# Write your solution here
# limit: int = int(input("Limit: "))
# start: int = 1
# total: int = 0
# count: str = ""
# while total < limit:
#     total += start
#     count += str(start) + " + "
#     start += 1
# print(f"The consecutive sum: {count[:-2]}= {total}")

"""Problem 7
Please write a program which asks the user for a string and an amount. 
The program then prints out the string as many times as specified by the amount. 
The printout should all be on one line, with no extra spaces or symbols added.
"""
# string_input: str = input("Please type in a string: ")
# int_input: int = int(input("Please type in an amount: "))
# print(string_input * int_input)

"""Problem 8
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters.
If the strings are of equal length, the program should print out "The strings are equally long".
"""
# str_one: str = input("Please type in string 1: ")
# str_two: str = input("Please type in string 2: ")
# if len(str_one) == len(str_two):
#     print("The strings are equally long")
# elif len(str_one) > len(str_two):
#     print(f"{str_one} is longer")
# else:
#     print(f"{str_two} is longer")

"""Problem 9
Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. 
Each character should be on a separate line.
"""
# str_input: str = input("Please type in a string: ")
# size: int = 0
# index: int = -1
# while size < len(str_input):
#     print(str_input[index])
#     index += -1
#     size += 1

"""Problem 10
Please write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character are the same or not.
See the examples below.
"""
# str_input: str = input("Please type in a string: ")
# if str_input[1] != str_input[-2]:
#     print("The second and the second to last characters are different")
# else:
#     print("The second and the second to last characters are", str_input[1])

"""Problem 11
Please write a program which prints out a line of hash characters, the width of which is chosen by the user.
"""
# width: int = int(input("Width: "))
# print("#" * width)

"""Problem 12
Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
"""
# width: int = int(input("Width: "))
# height: int = int(input("Height: "))
# counter = 0
# while counter < height:
#     print("#" * width)
#     counter += 1

"""Problem 13
Please write a program which asks the user for strings using a loop.
The program prints out each string underlined as shown in the examples below.
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.
"""
# while True:
#     user_str = input("Please type in a string: ")
#     if len(user_str) == 0:
#         break
#     else:
#         print(user_str)
#         print("-" * len(user_str))

"""Problem 14
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
"""
# user_str: str = input("Please type in a string: ")
# left = 20 - len(user_str)
# print("*" * left + user_str)

"""Problem 15
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters.
You may assume the input string will always fit inside the frame.
If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
"""
# user_str: str = input("Word: ")
# total_inner_width = 28
# spaces = total_inner_width - len(user_str)
# left_spaces = spaces // 2
# right_spaces = spaces - left_spaces 
# print("*" * 30)
# print(f"*{' ' * left_spaces}{user_str}{' ' * right_spaces}*")
# print("*" * 30)

"""Problem 16
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, from the shortest to the longest. 
Have a look at the example below.
"""
# user_str: str = input("Please type in a string: ")
# counter = 1
# while counter <= len(user_str):
#     print(user_str[0:counter])
#     counter += 1

"""Problem 17
Please write a program which asks the user to type in a string.
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.
"""
# user_str = input("Please type in a string: ")
# i = len(user_str) - 1
# while i >= 0:
#     print(user_str[i:])
#     i -= 1

"""Problem 18
Please write a program which asks the user to input a string. 
The program then prints out different messages if the string contains any of the vowels a, e or o.
You may assume the input will be in lowercase entirely. Have a look at the examples below.
"""
# while True:
#     user_str: str = input("Please type in a string: ")
#     if "a" in user_str:
#         print("a found")
#     if "a" not in user_str:
#         print("a not found")
#     if "e" in user_str:
#         print("e found")
#     if "e" not in user_str:
#         print("e not found")
#     if "o" in user_str:
#         print("o found")
#     if "o" not in user_str:
#         print("o not found")
#     break

"""Problem 19
Please write a program which asks the user to type in a string and a single character. 
The program then prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.
Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. 
In that case nothing should be printed out, and there should not be any indexing errors when executing the program.
"""
# user_str: str = input("Please type in a word: ")
# user_char: str = input("Please type in a character: ")
# start: int = user_str.find(user_char)
# if user_char in user_str:
#     if len(user_str[start:start + 3]) >= 3:
#         print(user_str[start:start + 3])

"""Problem 20"""
"""Problem 21"""

"""Problem 22
Please write a program which asks the user for a positive integer number. 
The program then prints out a list of multiplication operations until both operands reach the number given by the user. 
"""
user_str: str = input("")