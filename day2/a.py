import sys

def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    print(program)

    # Initial replacements
    program[1] = 12
    program[2] = 2
    print(program)

    # Run the program
    position = 0
    while program[position] != '99':
        if program[position] == 1:
            program[program[position+3]] = program[program[position+1]] + program[program[position+2]]
            print(program)
        elif program[position] == 2:
            program[program[position+3]] = program[program[position+1]] * program[program[position+2]]
            print(program)
        elif program[position] == 99:
            print('Halting...')
            break
        else:
            print("Wrong code")
            sys.exit(1)
        position += 4

    print('Solution: ' + str(program[0]))

if __name__ == '__main__':
    main()
