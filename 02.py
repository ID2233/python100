def commission(p):
    """A company pays bonuses based on profits,
    Return the bonuses with defferent profilts P."""
    if p > 100:
        return (p - 100) * 0.01 + commission(100)
    elif p > 60:
        return (p - 60) * 0.015 + commission(60)
    elif p > 40:
        return (p - 40) * 0.03 + commission(40)
    elif p > 20:
        return (p - 20) * 0.05 + commission(20)
    elif p > 10:
        return (p - 10) * 0.075 + commission(10)
    else:
        return p * 0.1
    
#    if p <= 10:
#        return p * 0.1
#    elif p <= 20:
#        return (p - 10) * 0.075 + 10 * 0.1
#    elif p <= 40:
#        return (p - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
#    elif p <= 60:
#        return (p - 40) * 0.03 + (40 - 20) * 0.05 + + (20 - 10) * 0.075 + 10 * 0.1
#    elif p <= 100:
#        return (p - 60) * 0.015 + (60 - 40) * 0.03 + (40 - 20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1
#    else:
#        return (p - 100) * 0.01 + (100 - 60) * 0.015 + (60 - 40) * 0.03 + (40 -
#        20) * 0.05 + (20 - 10) * 0.075 + 10 * 0.1

