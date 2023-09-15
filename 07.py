def multiplication_table():
    """Print 9 * 9 multiplication table."""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %-3d' %(j, i, i * j), end = '  ')
        print()
