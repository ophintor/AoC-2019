import sys
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

    print("asteroids found: " + str(asteroids))
    return asteroids

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
                print (">>> checking " + str(x) + ',' + str(y))
                asteroids = get_number_of_asteroids(map,x,y)
                if asteroids > max_asteroids:
                    max_asteroids = asteroids
                    winner = [y, x]

    print(max_asteroids)
    print(winner)

if __name__ == '__main__':
    main()
