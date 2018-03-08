#!/usr/bin/env python3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '.': operator.floordiv,
}

ans = ""

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def percent(base, perc, order): #order is True if base comes before percent
    perc = num(perc[0:-1])
    perc = perc/100
    base = num(base)
    arg1 = base
    arg2 = base*perc
    return (arg1, arg2) if order else (arg2, arg1)

def calculate(myarg):
    global ans
    stack = list()
    for token in myarg.split():
        if token == ":ans":
            if ans == "":
                raise Exception("Cannot use answer without previous calculation")
            stack.append(ans)
        elif token not in operators.keys():
            if token == "s":
                count = 0
                for c in range(0, len(stack)):
                    b = stack.pop()
                    count += num(b)
                stack.append(str(count))
            else:
                stack.append(token)
        else:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            if arg1[-1] == "%":
                arg1, arg2 = percent(arg2, arg1, False)
            elif arg2[-1] == "%":
                arg1, arg2 = percent(arg1, arg2, True)
            else:
                arg1 = num(arg1)
                arg2 = num(arg2)
            result = str(function(arg1, arg2)) #We want just strings on the stack. Keeps 
            stack.append(result)
    logger.debug(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    ans = stack.pop()
    return num(ans)

def main():
    global ans
    ans = ""
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()