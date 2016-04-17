__author__ = 'nikhil'

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

mul5 = multiplier_of(5)

print mul5(9)