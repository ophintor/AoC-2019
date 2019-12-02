import math

def main():
    filename = 'input.txt'
    total = 0

    with open(filename) as f:
        lines = f.readlines()

    for mass in lines:
        print('mass ' + mass)
        fuel = int(math.floor(int(mass) / 3)-2)
        total_fuel = fuel
        print('fuel ' + str(fuel))

        while fuel > 0:
            fuel = int(math.floor(int(fuel) / 3)-2)
            print('fuel ' + str(fuel))
            if fuel > 0:
                total_fuel += fuel

        print('total fuel ' + str(total_fuel))
        print('---')
        total = (total + total_fuel)

    print('solution: ' + str(total))

if __name__ == '__main__':
    main()
