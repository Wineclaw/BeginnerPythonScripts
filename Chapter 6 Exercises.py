## Chapter 6 Exercises!

import sys

def day_name(x):
    """Returns a day name from x, assuming 0 is Sunday"""
    if x == 0:
        return "Sunday"
    elif x == 1:
        return "Monday"
    elif x == 2:
        return "Tuesday"
    elif x == 3:
        return "Wednesday"
    elif x == 4:
        return "Thursday"
    elif x == 5:
        return "Friday"
    elif x == 6:
        return "Saturday"


def day_num(x):
    """Returns a day name from x, assuming 0 is Sunday"""
    if x == "Sunday":
        return 0
    elif x == "Monday":
        return 1
    elif x == "Tuesday":
        return 2
    elif x == "Wednesday":
        return 3
    elif x == "Thursday":
        return 4
    elif x == "Friday":
        return 5
    elif x == "Saturday":
        return 6


def day_add(today, days_added):
    """Takes the current day, roday, and adds a number of days, days_added,
    and returns the day of the week of that future day."""
    future_day_num = (day_num(today) + days_added) % 7
    return day_name(future_day_num)


def days_in_month(month):
    """Returns the number of days in a month"""
    if month == "September" or month == "April" or month == "June" \
    or month == "November":
        return 30
    elif month == "February":
        return 28
    else:
        return 31


def to_secs(hours, minutes, secs):
    """Converts hours, minutes, and secs given into total seconds."""
    to_sec_result = (hours * 60 * 60) + (minutes * 60) + secs
    return int(to_sec_result)


def hours_in(seconds):
    """ Converts seconds to hours """
    hours = (seconds / 60) / 60
    return int(hours)

def minutes_in(seconds):
    """ Converts seconds to minutes """
    minutes = ((seconds / 60) % 60)
    return int(minutes)


def seconds_in(seconds):
    """ Returns the remainder of seconds if assigned to hours and minutes
    """
    seconds_left = (seconds % 60)
    return int(seconds_left)


def compare(a, b):
    """ Compares a and b and returns a value depending on ., ==, and < """
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def hypotenuse(x, y):
    """ Returns the length of the hypotenuse of a right triangle given 
    its legs """
    hypo = (x**2) + (y**2)
    return float(hypo ** 0.5)


def slope(x1, y1, x2, y2):
    """ Returns the slope of a line """
    slope = (y2 - y1) / (x2 - x1)
    return float(slope)


def intercept(x1, y1, x2, y2):    # call slope
    """ Returns the y-intercept of a line through points given """
    intercept = (y2) - ((slope(x1, y1, x2, y2)) * (x2))
    return float(intercept)


def is_even(x):
    """ Checks if a number x is even """
    if x % 2 == 0:
        return True
    else:
        return False


def is_odd(x):
    """ Checks if a number x is odd """
    if (is_even(x)) == True:
        return False
    else:
        return True


def is_factor(f, n): 
    """ Returns true is f is a factor of n """
    if n % f == 0:
        return True
    else: False

def is_multiple(x, y):
    """ Returns true if x is a multiple of y """
    if y == 0:
        return False
    elif x % y == 0: return True
    else: return False


def f2c(x):
    """ Returns Celsius from F """
    cel = (x - 32) * 0.5556
    return round(cel)

def c2f(x):
    """ Returns F from Celsius """
    far = (x * 1.8) + 32
    return round(far)


### TESTING - DO NOT REMOVE
def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
# insert tests here


test_suite()
### TESTING - DO NOT REMOVE