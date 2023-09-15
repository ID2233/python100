def print_order(x, y, z):
    """Output 3 numbers from small to large"""
    #def helper(l):
    #    """Output elements from small to large."""
    #    if len(l) == 1:
    #        return l

    #    if min(l) == l[0]:
    #        return [ l[0] ] + helper(l[1:])
    #    else:
    #        l.append(l[0])
    #        l.remove(l[0])
    #        return helper(l)

    #return helper([x, y, z])

    l = [x, y, z]
    l.sort()
    print(l)
