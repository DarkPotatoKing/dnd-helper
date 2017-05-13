import random

# roll a (num_dice)d(num_faces) and return the result
# defaul is 1d6
# for example, to roll a 2d12: roll(2,12)
def roll(num_dice = 1, num_faces = 6):
    s = 0
    for _ in xrange(num_dice):
        s += random.randint(1, num_faces)
    return s

# roll a d20
def d20():
    return roll(1,20)

# rolls a 4d6 drop lowest for stat rolls
def roll_4d6_drop_lowest():
    rolls = [roll() for _ in xrange(4)]
    return sum(rolls) - min(rolls)

# roll stats using "4d6 drop lowest" method
def roll_stats():
    return sorted([roll_4d6_drop_lowest() for _ in xrange(6)])

# calculate number of hits until unit dies
def calculate_hits_before_death(hp, ac, base_damage = 1, ac_mod = 0):
    num_hits = float()
    ave_damage = float()
    total_damage = float()

    for i in xrange(1, 20 + 1):
        if i == 1:
            total_damage += 0
        elif i == 20:
            total_damage += base_damage * 2
        elif i >= ac + ac_mod:
            total_damage += base_damage
        else:
            total_damage += 0

    ave_damage = total_damage / 20.0
    num_hits = hp / ave_damage

    return num_hits
