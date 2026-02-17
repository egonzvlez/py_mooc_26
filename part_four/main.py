"""Problem: 1
Please write a program which asks the user which editor they are using. 
The program should keep on asking until the user types in Visual Studio Code.
Please write a program which asks the user which editor they are using. 
The program should keep on asking until the user types in Visual Studio Code.
"""
# while True:
#     user_choice: str = input("Editor: ").lower()
#     if user_choice == "word" or user_choice == "notepad":
#         print("awful")
#     elif user_choice != "visual studio code":
#         print("not good")
#     else:
#         print("an excellent choice!")
#         break

"""Problem 2
Please write a function named line, which takes two arguments: an integer and a string. 
The function prints out a line of text, the length of which is specified by the first argument.
The character used to draw the line should be the first character in the second argument. 
If the second argument is an empty string, the line should consist of stars.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

"""Problem 3
Please write a function named box_of_hashes, which prints out a rectangle of hash characters. 
The function takes one argument, which specifies the height of the rectangle. 
The rectangle should be ten characters wide.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. 
Please don't change anything in your line function.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

# def box_of_hashes(height: int) ->None:
#     count: int = 0
#     while count < height:
#         line(10,"#")
#         count += 1

"""Problem 4
Please write a function named square_of_hashes, which draws a square of hash characters. 
The function takes one argument, which determines the length of the side of the square.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

# def square_of_hashes(length: int):
#     count: int = 0
#     while count < length:
#         line(length, "#")
#         count += 1

"""Problem 5
Please write a function named square, which prints out a square of characters, and takes two arguments. 
The first parameter specifies the length of the side of the square. 
The second parameter specifies the character used to draw the square.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

# def square(length: int, text: str) -> None:
#     count: int = 0
#     while count < length:
#         line(length, text)
#         count += 1

"""Problem 6:
Please write a function named triangle, which draws a triangle of hashes, and takes one argument.
The triangle should be as tall and as wide as the value of the argument.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. 
Please don't change anything in the line function.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

# def triangle(size: int) -> None:
#     count: int = 1
#     while count <= size:
#         line(count,"#")
#         count += 1

"""Problem 7:
Please write a function named shape, which takes four arguments.
The first two parameters specify a triangle, as above, and the character used to draw it. 
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.
The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.
"""
# def line(lenght: int, text: str) -> None:
#     if not text: # Check if text is an empty string
#         print("*" * lenght)
#     else:
#         print(text[0] * lenght)

# def shape(size: int, text: str, height: int, filler: str) -> None:
#     triangle_count: int = 1
#     while triangle_count <= size:
#         line(triangle_count,text)
#         triangle_count += 1

#     rectangle_count = 0
#     while rectangle_count < height:
#         line(size,filler)
#         rectangle_count += 1

"""Problem 8: (Incomplete)
Please write a function named spruce, which takes one argument. 
The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.
"""
# def spruce(size: int) -> None:
#     print("a spruce!")
#     count: int = 1
#     leafs: int = 1
#     while count <= size:
#         print("*" * leafs)
#         count += 1
#         leafs += 2

"""Problem 9:
Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.
"""
# def greatest_number(x: int, y: int, z: int) -> int:
#     greatest_value: int = 0
#     if x >= y and x>= z:
#         greatest_value = x
#     elif y>= x and y >= z:
#         greatest_value = y
#     else:
#         greatest_value = z
#     return greatest_value

"""Problem 10:
Please write a function named same_chars, which takes one string and two integers as arguments.
The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. 
Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
"""
# def same_chars(text: str, index_one: int, index_two: int) -> bool:
#     length_text = len(text)
#     if index_one >= length_text or index_two >= length_text:
#         return False
#     elif text[index_one] == text[index_two]:
#         return True
#     else:
#         return False

"""Problem 11:
Please write three functions: first_word, second_word and last_word. Each function takes a string argument.
As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.
In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. 
There will be no spaces in the beginning or at the end of the argument strings.
"""
# def first_word(text: str):
#     word = text.split(" ")
#     return word[0]

# def second_word(text: str):
#     word = text.split(" ")
#     return word[1]

# def last_word(text: str):
#     word = text.split(" ")
#     return word[-1]

"""Problem 12:
Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. 
Then the program should ask the user for an index and a new value, replace the value at the given index, and print the list again. 
This should be looped over until the user gives -1 for the index. You can assume all given index values will fall within your list.
"""
# starting_list = [1,2,3,4,5]
# while True:
#     index: int = int(input("Index: "))
#     if index == -1:
#         break
#     value: int = int(input("New value: "))

#     starting_list[index] = value
#     print(starting_list)

"""Problem 13:
Please write a program which first asks the user for the number of items to be added.
Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. 
Finally, the list is printed out.
"""
# total_items = int(input("How many items: "))
# some_list: list[int] = []
# for i in range(1,total_items + 1):
#     item = int(input(f"Item {i}: "))
#     some_list.append(item)
# print(some_list)

"""Problem 14
Please write a program which asks the user to choose between addition and removal.
Depending on the choice, the program adds an item to or removes an item from the end of a list.
The item that is added must always be one greater than the last item in the list. The first item to be added must be 1.
"""
# starting_list: list [int] = []
# count: int = 1

# while True:
#     print(f"The list is now: {starting_list}")
#     option: str = input("a(d)d, (r)emove or e(x)it: ")
#     if option == "d":
#         starting_list.append(count)
#         count += 1
#     elif option == "r":
#         starting_list.pop(-1)
#         count -= 1
#     elif option == "x":
#         break

"""Problem 15
Please write a program which asks the user for words. 
If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.
"""
# words: list[str] = []
# while True:
#     word: str = input("Word: ")
#     if word not in words:
#         words.append(word)
#     else:
#         break

# print(f"You typed in {len(words)} different words")

"""Problem 16
Please write a program which asks the user to type in values and adds them to a list.
After each addition, the list is printed out in two different ways:
    -in the order the items were added
    -ordered from smallest to greatest
The program exits when the user types in 0.
"""
# normal_list: list[int] = []
# formatted_list: list[int] = []
# while True:
#     item: int = int(input("New Item: "))
#     if item == 0:
#         print("Bye!")
#         break
#     else:
#         normal_list.append(item)
#         formatted_list.append(item)
#         print(f"The list now: {normal_list}")
#         print(f"The list in order: {sorted(formatted_list)}")

"""Problem 17
Please write a function named length which takes a list as its argument and returns the length of the list.
"""
# def length(some_list: list[int]) -> int:
#     return len(some_list)

"""Problem 18:
Please write a function named mean, which takes a list of integers as an argument. The function returns the arithmetic mean of the values in the list.
"""
# def mean(numbers: list[int]) -> int:
#     return sum(numbers) / len(numbers)

"""Problem 19:
Please write a function named range_of_list, which takes a list of integers as an argument.
The function returns the difference between the smallest and the largest value in the list.
"""
# def range_of_list(numbers: list[int]) -> int:
#     numbers.sort()
#     return numbers[-1] - numbers[0]

"""Problem 20:
Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. After each character there should be a star (*) printed on its own line.
"""
# some_string: str = input("Please type in a string: ")
# for char in some_string:
#     print(char)
#     print("*")

"""Problem 21:
Please write a program which asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.
"""
# number: int = int(input("Please enter a positive number: "))
# for i in range(-number,number + 1):
#     if i == 0:
#         continue
#     else:
#         print(i)

"""Problem 22:
Please write a function named list_of_stars, which takes a list of integers as its argument. The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.
"""
# def list_of_stars(number_stars: list[int]) -> None:
#     for i in number_stars:
#         print("*" * i)

"""Problem 23
Please write a function named anagrams, which takes two strings as arguments. The function returns True if the strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters.
"""
# def anagrams(string_one: str, string_two: str) -> bool:
#     if len(string_one) != len(string_two):
#         return False
#     else:
#         for i in string_one:
#             if i in string_two:
#                 continue
#             else:
#                 return False
#         return True

"""Problem 24:
Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards.
"""
# def palindromes(word: str) -> bool:
#     word_backwards = word[::-1]
#     if word_backwards == word:
#         print(f"{word} is a palindrome!")
#         return True
#     else:
#         print("that wasn't a palindrome")
#         return False
    
# found_palindrome = False
# while not found_palindrome:
#     word: str = input("Please type in a palindrome: ")
#     if palindromes(word):
#         found_palindrome = True
#     else:
#         continue

"""Problem 25:
Please write a function named sum_of_positives, which takes a list of integers as its argument. The function returns the sum of the positive values in the list.
"""
# def sum_of_positives(numbers: list[int]) -> int:
#     total = 0
#     for i in numbers:
#         if i < 0:
#             continue
#         else:
#             total += i
#     return total

"""Problem 26:
Please write a function named even_numbers, which takes a list of integers as an argument. The function returns a new list containing the even numbers from the original list.
"""
# def even_numbers(numbers: list[int]) -> list[int]:
#     even_nums: list[int] = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_nums.append(num)
#     return even_nums

"""Problem 27:
Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains the sums of the items at each index in the two original lists. You may assume both lists have the same number of items
"""
# def list_sum(list_one:list[int], list_two: list[int]) -> list[int]:
#     sum_list: list[int] = []
#     for i in range(len(list_one)):
#         total = list_one[i] + list_two[i]
#         sum_list.append(total)
#     return sum_list

"""Problem 28:
Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
"""
# def distinct_numbers(list_one:list[int]) -> list[int]:
#     new_list: list[int] = []
#     for i in list_one:
#         if i not in new_list:
#             new_list.append(i)
#     return sorted(new_list)

"""Problem 29:
Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.
"""
# def length_of_longest(some_list: list[str]) -> int:
#     longest_string = 0
#     for string in some_list:
#         length = len(string)
#         if length > longest_string:
#             longest_string = length
#     return longest_string

"""Problem 30:
Please write a function named shortest, which takes a list of strings as its argument. 
The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests).
You may assume there will be no empty strings in the list.
"""
# def shortest(some_list: list[str]) -> str:
#     shortest_str: float = float("inf")
#     shortest_string: str = ""
#     for i in some_list:
#         length = len(i)
#         if length < shortest_str:
#             shortest_str = length
#             shortest_string = i
#     return shortest_string

"""Problem 31:
def all_the_longest(some_list: list[str]) -> list[str]:
    long_strings: list[str] = []
    size_of_string: int = 0

    # get the length of longest string
    for i in some_list:
        length = len(i)
        if length > size_of_string:
            size_of_string = length

    for i in some_list:
        if len(i) >= size_of_string:
            long_strings.append(i)

    return long_strings
"""

"""Problem 32:
Please write a function named formatted, which takes a list of floating point numbers as its argument. 
The function returns a new list, which contains each element of the original list in string format, rounded to two decimal points.
The order of the items in the list should remain unchanged.
"""
# def formatted(some_list: list[float]) -> list[str]:
#     formatted_list: list[str] = []
#     for i in some_list:
#         formatted_list.append(f"{i:.2f}")
#     return formatted_list

"""Problem 33:
Please write a function named everything_reversed, which takes a list of strings as its argument. 
The function returns a new list with all of the items on the original list reversed.
Also the order of items should be reversed on the new list.
"""
# def everything_reversed(some_list: list[str]) -> list[str]:
#     new_list: list[str] = []
#     copy_list: list[str] = some_list[::-1]
#     for i in copy_list:
#         word = i[::-1]
#         new_list.append(word)
#     return new_list

"""Why wont this work"""
