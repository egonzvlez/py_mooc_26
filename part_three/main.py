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