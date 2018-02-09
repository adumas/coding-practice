# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons.
#
# Implement car and cdr.


def cons(a, b):
    return lambda f: f(a, b)


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


def test(fcn, input, expected):
    print "testing " + str(input)
    result = fcn(input)
    if result == expected:
        print "PASS"
    else:
        print "FAIL: " + str(result) + " [expected: " + str(expected) + "]"


test(lambda (a, b): car(cons(a, b)), [3, 4], 3)

test(lambda (a, b): cdr(cons(a, b)), [3, 4], 4)
