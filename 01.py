def number_arrange(m, n):
    """Return how many non-repeating n-digit numbers can be formed by selecting n
    non-repeating numbers from m non-repeating numbers."""
    return combination_number(m, n) * factorial(n)

def combination_number(m, n):
    """Choose n non-repeating numbers from m non-repeating numbers."""
    if m < n:
        return 0
    elif m == n:
        return 1
    else:
        return factorial(m) // (factorial(n) * factorial(m-n))


def factorial(n):
    """Returns the factorial of n."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

a = number_arrange(4, 3)
