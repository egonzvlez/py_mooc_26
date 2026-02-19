"""Problem 1:
Please write a function named longest(strings: list), which takes a list of strings as its argument.
The function finds and returns the longest string in the list. 
You may assume there is always a single longest string in the list.
"""
# def longest(strings: list[str]) -> str:
#     size: int = 0
#     longest_string: str = ""

#     for string in strings:
#         length = len(string)
#         if length >= size:
#             size = length
#             longest_string = string

#     return longest_string


"""Problme 2:
Please write a function named count_matching_elements(my_matrix: list, element: int), 
which takes a two-dimensional array of integers and a single integer value as its arguments. 
The function then counts how many elements within the matrix match the argument value.
"""
# def count_matching_elements(my_matrix: list[list[int]], element: int) -> int:
#     count: int = 0
#     for row in my_matrix:
#         for num in row:
#             if num == element:
#                 count += 1

#     return count

"""Problem 3:
Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. 
The array consists of integer values, which represent the following situations:

    0: empty square
    1: player 1 game piece
    2: player 2 game piece

The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board.
Also, the size of the game board is not limited.
The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
If both players have the same number of pieces on the board, the function should return the value 0.
"""
# def who_won(game_board: list[list[int]]) -> int:
#     ones: int = 0
#     twos: int = 0

#     for i in game_board:
#         for j in i:
#             if j == 1:
#                 ones += 1
#             elif j == 2:
#                 twos += 1

#     if ones > twos:
#         return 1
#     elif twos > ones:
#         return 2
#     else:
#         return 0

"""Problem 4:
Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid,
and an integer referring to a single row, as its arguments.Rows are indexed from 0.
The function should return True or False, depending on whether the row is filled in correctly, 
that is, whether it contains each of the numbers 1 to 9 at most once.
"""
# def row_correct(sudoku: list[list[int]], row_no: int) -> bool:
#     row: list[int] = sudoku[row_no]
#     valid_numbers:list [int] = []
#     for num in row:
#         if num == 0:
#             continue
#         elif num not in valid_numbers:
#             valid_numbers.append(num)
#         else:
#             return False
#     return True

"""Problem 5:
Please write a function named column_correct(sudoku: list, column_no: int), which takes a two-dimensional array representing a sudoku grid,
and an integer referring to a single column, as its arguments. Columns are indexed from 0.
The function should return True or False, depending on whether the column is filled in correctly, 
that is, whether it contains each of the numbers 1 to 9 at most once.
"""
# def column_correct(sudoku: list[list[int]], column_no: int ) -> bool:
#     valid_numbers:list [int] = []
#     for row in sudoku:
#         element = row[column_no]
#         if element == 0:
#             continue
#         elif element not in valid_numbers:
#             valid_numbers.append(element)
#         else:
#             return False
#     return True

"""Problem 6:
Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, 
and two integers referring to the row and column indexes of a single square, as its arguments. 
Rows and columns are indexed from 0.

The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly.
That is, whether the block contains each of the numbers 1 to 9 at most once.

Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check,
and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). 
Such restrictions on indexes should not be implemented here.
"""
# def block_correct(sudoku:list[list[int]], row_no: int, column_no: int) -> bool:
#     # Holds seen values in 3x3 box
#     valid_num: list[int]= []

#     for i in range(row_no, row_no + 3):
#         for j in range(column_no, column_no + 3):
#             element = sudoku[i][j]
#             if element == 0: # empty square, ignore
#                 continue
#             elif element not in valid_num: # if value is not in seen values, it gets added to keep track
#                 valid_num.append(element)
#             else: # value in seen values, invalid sudoku box
#                 return False
#     return True

# # sudoku = [
# #   [9, 0, 0, 0, 8, 0, 3, 0, 0],
# #   [2, 0, 0, 2, 5, 0, 7, 0, 0],
# #   [0, 2, 0, 3, 0, 0, 0, 0, 4],
# #   [2, 9, 4, 0, 0, 0, 0, 0, 0],
# #   [0, 0, 0, 7, 3, 0, 5, 6, 0],
# #   [7, 0, 5, 0, 6, 0, 4, 0, 0],
# #   [0, 0, 7, 8, 0, 3, 9, 0, 0],
# #   [0, 0, 1, 0, 0, 0, 0, 0, 3],
# #   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# # ]
# # print(block_correct(sudoku, 0, 0))

"""Problem 7:
Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument.
The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. 
Copy the functions from the exercises above into your Python code file for this exercise.

The function should check each of the nine rows, columns and 3 by 3 blocks in the grid.
If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. 
These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).
"""
# # Still working on it
# def sudoki_grid_correct(sudoku: list[list[int]]) -> bool:
#     grids: list[tuple[int,int]] = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

#     for i in range(0,9):
#         if row_correct(sudoku,i):
#             if column_correct(sudoku, i):
#                 row_no = i[0]
#                 column_no = i[1]
#                 if block_correct(sudoku,row_no,column_no):
                
#         else:
#             return False
        
#     return True