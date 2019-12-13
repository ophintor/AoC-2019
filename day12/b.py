import sys
from fractions import gcd
from itertools import combinations

def calculate_lcm(l):
    sol = 1
    for i in range(len(l)):
        sol = abs(sol * l[i]) // gcd(sol, l[i])
    print(sol)
    sys.exit(0)


def find_patterns(patterns_matrix, patterns_size):
    for s in range(len(patterns_size)):
        found = 0
        if patterns_size[s] < 2:
            for m in range(1,(len(patterns_matrix)/10)):
                if  patterns_matrix[0][s] == patterns_matrix[m][s] == patterns_matrix[m*2][s] == patterns_matrix[m*3][s] == patterns_matrix[m*4][s] and \
                    patterns_matrix[0+1][s] == patterns_matrix[m+1][s] == patterns_matrix[m*2+1][s] == patterns_matrix[m*3+1][s] == patterns_matrix[m*4+1][s]:
                    patterns_size[s]=m
                    found = 1
                if found:
                    break


def update_velocity2(position_0, position, velocity_0, velocity):
    nc=len(velocity[0])
    found = 0
    steps = 1
    moon_ids = [0,1,2,3]
    pairs = [ comb for comb in combinations(moon_ids, 2) ]
    patterns_matrix = []
    patterns_size = [ 0 ] * 24

    p = [item for sublist in position_0 for item in sublist]
    v = [item for sublist in velocity_0 for item in sublist]
    patterns_matrix.append(p + v)

    while not found:
        for coords in range(nc):
            for moons in pairs:
                moon1 = moons[0]
                moon2 = moons[1]
                if position[moon1][coords] > position[moon2][coords]:
                    velocity[moon1][coords] -= 1
                    velocity[moon2][coords] += 1
                elif position[moon1][coords] < position[moon2][coords]:
                    velocity[moon1][coords] += 1
                    velocity[moon2][coords] -= 1
            for moon in moon_ids:
                position[moon][coords] += velocity[moon][coords]

        p = [item for sublist in position for item in sublist]
        v = [item for sublist in velocity for item in sublist]
        patterns_matrix.append(p + v)
        steps += 1

        if steps % 10000 == 0:
            find_patterns(patterns_matrix, patterns_size)
            if all(i >= 2 for i in patterns_size):
                calculate_lcm(patterns_size)


def calculate_steps(position):
    velocity = [[ 0 for x in range(len(position[0]))] for y in range(len(position))]
    position_0 = [ x[:] for x in position]
    update_velocity2(position_0, position, velocity, velocity)


def main():
    filename = 'input.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    iostr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in lines[0])
    io = [int(i) for i in iostr.split()]
    europastr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in lines[1])
    europa = [int(i) for i in europastr.split()]
    ganymedestr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in lines[2])
    ganymede = [int(i) for i in ganymedestr.split()]
    callistostr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in lines[3])
    callisto = [int(i) for i in callistostr.split()]

    position = [io,europa,ganymede,callisto]
    calculate_steps(position)


if __name__ == '__main__':
    main()
