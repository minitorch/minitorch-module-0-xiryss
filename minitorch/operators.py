"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$
def add(x: float, y: float) -> float:
    return x + y
def mul(x: float, y: float) -> float:
    return x * y
def eq(a: float, b: float) -> float:
    if (a == b):
        return 1
    return 0
def id(a: float) -> float:
    return a
def inv(a: float) -> float:
    return 1 / a
def lt(a: float, b: float) -> float:
    if (a < b):
        return 1
    return 0
def max(a: float, b: float) -> float:
    if(a>b):
        return a
    return b
def sigmoid(a: float) -> float:
    if (a >= 0):
        return 1 / (1 + math.exp(-a))
    else:
        return math.exp(a) / (1 + math.exp(a))
def is_close(a:float, b:float)->float:
    return abs(a-b) <1e-9
def relu(a: float) -> float:
    if(a>=0):
        return a
    return 0
def neg(a: float) -> float:
    return -a
def log_back(a:float, b:float) -> float:
    return b/a
def inv_back(a:float, b:float) -> float:
    return - b/(a*a)
def relu_back(a:float, b:float) -> float:
    if(a>=0):
        return b
    return 0
# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists
def log(a: float) -> float:
    return math.log(a)
def exp(a: float) -> float:
    return math.exp(a)
def map(func: Callable, b: Iterable) -> Iterable:
    iter_b = iter(b)
    res = []
    while True:
        try:
            res.append(func(next(iter_b)))
        except StopIteration:
            return res
def zipWith(func: Callable, a: Iterable[float], b: Iterable[float]) -> Iterable[float]:
    res = []
    iter_a = iter(a)
    iter_b = iter(b)
    res = []
    while True:
        try:
            res.append(func(next(iter_a), next(iter_b)))
        except StopIteration:
            return res
def reduce(func: Callable, ls: Iterable[float]) -> float:
    iter_ls = iter(ls)
    result = 0
    try:
        result = next(iter_ls)
    except StopIteration:
        return result
    for elem in iter_ls:
        result = func(result, elem)
    return result
def negList(ls:Iterable[float]) -> Iterable[float]:
    return map(neg, ls)
def addLists(a: Iterable[float], b: Iterable[float]) -> Iterable[float]:
    return zipWith(add, a, b)
def prod(ls: Iterable[float]) -> float:
    return reduce(mul, ls)
def sum(ls: Iterable[float]) -> float:
    return reduce(add, ls)

# TODO: Implement for Task 0.3.
