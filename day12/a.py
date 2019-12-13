import sys
from itertools import islice

def update_velocity(position, velocity):
    np=len(velocity)
    nc=len(velocity[0])
    for coords in range(nc):
        for moon1 in range(np):
            for moon2 in range(moon1+1,np):
                if position[moon1][coords] > position[moon2][coords]:
                    velocity[moon1][coords] -= 1
                    velocity[moon2][coords] += 1
                elif position[moon1][coords] < position[moon2][coords]:
                    velocity[moon1][coords] += 1
                    velocity[moon2][coords] -= 1
            position[moon1][coords] += velocity[moon1][coords]

    return position, velocity

def calculate_total_energy(position, velocity):
    energy = 0
    pot = []
    kin = []

    for x in position:
        pot.append(abs(x[0])+abs(x[1])+abs(x[2]))

    for x in velocity:
        kin.append(abs(x[0])+abs(x[1])+abs(x[2]))

    for x in range(len(pot)):
        energy += kin[x]*pot[x]

    return energy


def calculate_energy(position):
    steps = 1000
    velocity = [[ 0 for x in range(len(position[0]))] for y in range(len(position))]

    for _ in range(steps):
        # print(position, velocity)
        position, velocity = update_velocity(position, velocity)

    energy = calculate_total_energy(position, velocity)

    return energy

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
    positions = [io,europa,ganymede,callisto]

    energy = calculate_energy(positions)
    print (energy)

if __name__ == '__main__':
    main()
