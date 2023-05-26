# InfinitePrecisioninPython
infinite precision math!

I want to do MATH with a lot more precision! At least hundreds of digits

Write a class that stores a number in (high) precision

Precision should expand as needed up to a class-wide hard-coded limit

v1 - integer, positives only
v2 - integer, handle negative numbers (you may want to design this before you implement v1)
Note that this is perhaps the hardest part of the project
v3 - fractional arithmetic ( 500.324523222 )

Implement:
initialize from string, long, copy
implement add, subtract, times, divide, mod, and comparison operators (<, etc)
can be separate methods, but then do the operator overloading
return string/long
(recommended)
implement a "state()" function that returns the internal state as a string for debug
implement ++ and --
Test cases
yup, lots
main() / driver
A simple calculator
read lines from user
M + N, M - N, etc -- output the result

# How to use:

feed a string, int or float into the highprecision() class that will serve as it's value.
Then perform any operator with that value and another high precision class and value.

ie.

a=highprecision(1)
b=highprecision(3)
print(a/b)
