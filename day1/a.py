import math

def main():
    filename = 'input.txt'
    total = 0

    with open(filename) as f:
        lines = f.readlines()

    for value in lines:
        value = int(math.floor(int(value) / 3)-2)
        total += value

    print('solution: ' + str(total))

if __name__ == '__main__':
    main()
