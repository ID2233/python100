def day_of_year(year, month, day):
    """Enter a date, a certain day of a certain month in a certain year,
    and return that this day is the day of the year."""

    # add an index, corresponding month order
    number_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year):
        number_of_days[2] = 29

    month_total = sum(number_of_days[1:month])
    return month_total + day

def leap_year(year):
    """Return True if it is a leay year, otherwise return False.
    Every year that is exactly divisible by four is a leap year,
    except for years that are exactly divisible by 100, but these
    centurial years are leap years if they are exactly divisible by 400. 
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
