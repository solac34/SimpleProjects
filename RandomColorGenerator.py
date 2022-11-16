import random


def rgb_gen(n):  # generate color with rgb
    if n == 1 or n == '1':
        return random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)
    return [(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)) for i in range(n)]


def hex_gen(n):  # generate color with hex
    if n == 1 or n == '1':
        return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for x in range(n)]

