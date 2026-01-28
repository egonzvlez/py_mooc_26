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