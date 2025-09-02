# This example is taken from python in a nutshell - Chapter 17
# Page 825
# https://github.com/pynutshell/pynut4/blob/main/17_Testing_Debugging_and_Optimizing/inspect_example.py
# We start to inspect the class using a try except on each class
class A:
    def ff(self):
        pass

x = A()

# The function getmembers of the module inspect obtains the name of all the methods
# available on x in order to display them.
# try:
#     x.f()
# except AttributeError:
#     import sys, inspect
#     print(f"x is type {type(x)}, ({x!r})", file=sys.stderr)
#     print(f"methods in x:", file=sys.stderr, end='')
#     for n, v in inspect.getmembers(x, callable):
#         print(n, file=sys.stderr, end=' ')
#     print(file=sys.stderr)
#     raise

# NOTE: This example also shows an implementation of a helper function to use on any class
# import sys, inspect, logging

# Configuring logging to write to a file
# logging.basicConfig(filename='./logs/_app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def show_obj_methods(obj, name, show=sys.stderr.write):
#     show(f"{name} is type {type(obj)}({obj!r})\n")
#     show(f"{name}'s methods are: ")
#
#     # Logging
#     logging.info(f"{name} is type {type(obj)}({obj!r})")
#     logging.info(f"{name}'s methods are: ")
#
#     for n, v in inspect.getmembers(obj, callable):
#        show(f"Members loop {n} ")
#        logging.info(f"Members loop {n} ")
#     show('\n')
#
#
# # And then the example becomes just:
# try:
#     x.f()
# except AttributeError:
#     show_obj_methods(x, 'x')
#     raise