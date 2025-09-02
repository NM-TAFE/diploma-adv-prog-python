# example 1
filename = __file__
import pdb; pdb.set_trace()
breakpoint()
print(f'path = {filename}')


# #example 2
# l & ll (list): Display the source code around the current line.
# p head: Print the value of head.
# p tail: Print the value of tail.
# n: Move to the next line in the current function.
# r (return): Continue execution until the current function returns.

# import os
#
# def get_path(file_name):
#     """Return file's path or empty string if no path."""
#     breakpoint()
#     head, tail = os.path.split(file_name)
#     import pdb; pdb.set_trace()
#
#     return head
#
#
# filename = __file__
# print(f'path = {get_path(filename)}')

# # example 3
# n: Step to the next line in the current scope.
# s: Step into the get_path function.
# p head, p tail: Print the current value of head and tail.
# c: Continue running the script until the next breakpoint or the end of the program.
# ll: Long listing of the current function, displaying the entire source code for context.
# q: Quit the debugger.

# import os
#
# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head
#
#q
# import pdb; pdb.set_trace()
# filename = __file__
# filename_path = get_path(filename)
# print(f'path = {filename_path}')

# # example 4
# u: up the stack
# d: down the stack
# c: Continue running the script until the next breakpoint or the end of the program.
# l & ll (list): Display the source code around the current line.
# w: check the stack
# b: set a breakpoint
# Use up & down
# def function_a(first_number, second_number):
#     result_of_addition = first_number + second_number
#     print(f"In function_a: first_number = {first_number}, second_number = {second_number}, result_of_addition = {result_of_addition}")
#     function_b(result_of_addition)

# def function_b(sum_result):
#     result_of_multiplication = sum_result * 2
#     breakpoint()
#     print(f"In function_b: sum_result = {sum_result}, result_of_multiplication = {result_of_multiplication}")
#     function_c(result_of_multiplication)

# def function_c(multiplied_result):
#     result_of_subtraction = multiplied_result - 3
#     print(f"In function_c: multiplied_result = {multiplied_result}, result_of_subtraction = {result_of_subtraction}")
#     function_d(result_of_subtraction)

# def function_d(subtracted_result):
#     result_of_division = subtracted_result / 2
#     print(f"In function_d: subtracted_result = {subtracted_result}, result_of_division = {result_of_division}")
#     # Start debugger here
#     # breakpoint()  # Start debugger here
#     print("Inside function_d")

if __name__ == "__main__":
    number_one = 5
    number_two = 10
    function_a(number_one, number_two)
