import random

# roll a (num_dice)d(num_faces) and return the result
# defaul is 1d6
# for example, to roll a 2d12: roll(2,12)
def roll(num_dice = 1, num_faces = 6):
    s = 0
    for _ in xrange(num_dice):
        s += random.randint(1, num_faces)
    return s

# rolls a 4d6 drop lowest for stat rolls
def roll_4d6_drop_lowest():
    rolls = [roll() for _ in xrange(4)]
    return sum(rolls) - min(rolls)

# roll stats using "4d6 drop lowest" method
def roll_stats():
    return sorted([roll_4d6_drop_lowest() for _ in xrange(6)])
