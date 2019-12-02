import sys

def main():
    filename = 'input.txt'

    for noun in range(0,99):
        for verb in range(0,99):

            with open(filename) as f:
                program = [int(x) for x in f.readline().split(",")]

            program[1] = noun
            program[2] = verb

            # Run the program
            position = 0
            while program[position] != '99':
                if program[position] == 1:
                    program[program[position+3]] = program[program[position+1]] + program[program[position+2]]
                elif program[position] == 2:
                    program[program[position+3]] = program[program[position+1]] * program[program[position+2]]
                elif program[position] == 99:
                    break
                else:
                    print("Wrong code")
                    sys.exit(1)
                position += 4

            if program[0] == 19690720:
                print('Solution: ' + str(100 * noun + verb))
                sys.exit(0)

if __name__ == '__main__':
    main()
