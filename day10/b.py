import sys
import math
from fractions import gcd

def get_number_of_asteroids(map,current_x,current_y):
    asteroids = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == '#' and (current_x != x or current_y != y):
                distance_x = abs(x - current_x)
                distance_y = abs(y - current_y)
                blocked = 0
                if distance_x == 0:
                    start_point = (current_y + 1) if y > current_y else (current_y - 1)
                    end_point   = y
                    direction   = 1 if y > current_y else -1
                    for step in range(start_point,end_point,direction):
                        if map[x][step] == '#':
                            blocked = 1
                            break
                    if not blocked:
                        asteroids += 1
                elif distance_y == 0:
                    start_point = (current_x + 1) if x > current_x else (current_x - 1)
                    end_point   = x
                    direction   = 1 if x > current_x else -1
                    for step in range(start_point,end_point,direction):
                        if map[step][y] == '#':
                            blocked = 1
                            break
                    if not blocked:
                        asteroids += 1
                elif distance_x != 0 and distance_y != 0:
                    common_div = gcd(distance_x,distance_y)
                    (step_x, step_y) = (distance_x / common_div, distance_y / common_div)
                    next_x = current_x
                    next_y = current_y
                    if common_div == 1:
                        asteroids += 1
                    else:
                        for step in range(common_div-1):
                            next_x = next_x + step_x if next_x < x else next_x - step_x
                            next_y = next_y + step_y if next_y < y else next_y - step_y
                            if map[next_x][next_y] == '#':
                                blocked = 1
                                break
                        if not blocked:
                            asteroids += 1

    return asteroids


def calculate_angles(map,current_x,current_y):
    angles = [ [1000.0] * (len(map[0])) for _ in range(len(map)) ]
    for x in range(len(angles)):
        for y in range(len(angles[0])):
            if (current_x == x) and (current_y == y):
                angles[x][y] = 666.0
            elif map[x][y] != '.':
                distance_x = abs(float(x - current_x))
                distance_y = abs(float(y - current_y))
                if (current_x >= x ) and (current_y > y):
                    angles[x][y] = float(360 - (distance_y * 45 / distance_x)) if distance_x >= distance_y else float(270 + (distance_x * 45 / distance_y))
                elif (current_x <= x ) and (current_y <= y):
                    angles[x][y] = float(180 - (distance_y * 45 / distance_x)) if distance_x >= distance_y else float(90 + (distance_x * 45 / distance_y))
                elif (current_x <= x ) and (current_y >= y):
                    angles[x][y] = float(180 + (distance_y * 45 / distance_x)) if distance_x > distance_y else float(270 - (distance_x * 45 / distance_y))
                elif (current_x > x ) and (current_y <= y):
                    angles[x][y] = float(distance_y * 45 / distance_x) if distance_x > distance_y else float(90 - (distance_x * 45 / distance_y))

    return angles

def find_minimum_and_closer(m, base, current_x, current_y):
    minimum = 360
    locations = []

    for x in range(len(m)):
        for y in range(len(m[0])):
            if base <= m[x][y] < minimum:
                minimum = m[x][y]

    if minimum == 360:
        closer_loc = [-1, -1]
    else:
        for x in range(len(m)):
            for y in range(len(m[0])):
                if m[x][y] == minimum:
                    locations.append([x,y])

        closer_loc = []
        for loc in locations:
            if not closer_loc or abs(loc[0] - current_x) < abs(closer_loc[0] - current_x):
                closer_loc = list(loc)

    return closer_loc[0], closer_loc[1], minimum

def vaporise(angles,current_x,current_y):
    base = 0
    vaporised = 0
    new_loop = 1
    all_destroyed = 0
    while not all_destroyed:
        (x,y,current_angle) = find_minimum_and_closer(angles, base, current_x, current_y)
        if x == -1 and y == -1:
            new_loop += 1
            if new_loop == 2:
                all_destroyed = 1
                print ("All destroyed!!")
                break
            base = 0
        else:
            new_loop = 0
            base = current_angle + 0.001
            print ("current angle: " + str(current_angle))
            print("Attempting to vaporise: " + str(x) + ',' + str(y))
            angles[x][y] = 1000.0
            vaporised += 1
            if vaporised == 200: (x200, y200) = (x, y)
            print("Vaporised (asteroide number " + str(vaporised) + ")")
            print('----')

    return (y200 * 100 + x200)

def main():
    filename = 'input.txt'

    with open(filename) as f:
        map = f.read().splitlines()

    for line in map:
        line.split("(?!^)")

    max_asteroids = 0

    for x in range(len(map)):
        for y in range(len(line)):
            if map[x][y] == '#':
                asteroids = get_number_of_asteroids(map,x,y)
                if asteroids > max_asteroids:
                    max_asteroids = asteroids
                    winner = [y, x]

    print(max_asteroids)
    print(winner)

    angles = calculate_angles(map,winner[1],winner[0])
    sol200 = vaporise(angles,winner[1],winner[0])

    print ("\nSolution for number 200: " + str(sol200))


if __name__ == '__main__':
    main()
