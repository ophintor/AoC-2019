import sys

def get_opscode(x):
    return x%100

def get_modes(x):
    modes = str(x)[:-2]
    lm=len(modes)
    if lm < 3:
        modes = '0'*(3-lm) + modes
    return modes

def calc_value(prog,mode,pos):
    if mode == '0':
        return prog[pos]
    elif mode == '1':
        return pos
    else:
        print('error')
        print(mode)
        sys.exit(1)

def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    input_instr = 1

    # Run the program
    position = 0
    opscode = get_opscode(program[position])
    modes = get_modes(program[position])

    while opscode != '99':
        opscode = get_opscode(program[position])
        modes = get_modes(program[position])
        if opscode == 1:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            p3=calc_value(program,modes[0],position+3)
            program[p3] = program[p1] + program[p2]
            position += 4
        elif opscode == 2:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            p3=calc_value(program,modes[0],position+3)
            program[p3] = program[p1] * program[p2]
            position += 4
        elif opscode == 3:
            program[program[position+1]] = input_instr
            position += 2
        elif opscode == 4:
            output = program[program[position+1]]
            print(output)
            position += 2
        elif opscode == 99:
            break
        else:
            print("Wrong code")
            sys.exit(1)


if __name__ == '__main__':
    main()
