""" Demonstrates how Python imports ignore _private vars 
try from another module with `from some_vars import *` and check if _a
is imported"""
a = 1
b = 2
_a = 42
