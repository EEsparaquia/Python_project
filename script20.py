#! Python3

# Programming tutorial: 
# Module import Syntax


## Alternative 1
## Import just the library 
## You need in order to use
## The code:
import statistics as s
list_ex = [12,4,3,1,7,8,33,34,23,5]
x = s.variance(list_ex)
print(x)


## Alternative 2
## Import just the function 
## You need in order to simplify
## The code:
# from statistics import variance, mean
# list_ex = [12,4,3,1,7,8,33,34,23,5]
# x = variance(list_ex)
# y = mean(list_ex)
# print(x)
# print(y)


## Alternative 3
## Import just the function
## You need in order to simplify
## The code using alias:
# from statistics import variance as v
# list_ex = [12,4,3,1,7,8,33,34,23,5]
# x = v(list_ex)
# print(x)


## Alternative 4
## Import just the function s
## You need in order to simplify
## The code using alias:
# from statistics import variance as v, mean as m
# list_ex = [12,4,3,1,7,8,33,34,23,5]
# x = v(list_ex)
# y = m(list_ex)
# print(x)
# print(y)


## Alternative 5
## Import all the functions 
## Yof the library to use in
## The code:
# from statistics import *
# list_ex = [12,4,3,1,7,8,33,34,23,5]
# x = variance(list_ex)
# y = mean(list_ex)
# print(x)
# print(y)
