import sys
from itertools import permutations

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

def intcode(program, seq, input_instr):
    position = 0
    opscode = get_opscode(program[position])
    modes = get_modes(program[position])
    output = 0
    seq_applied = 0

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
            if not seq_applied:
                program[program[position+1]] = seq
                seq_applied = 1
            else:
                program[program[position+1]] = input_instr
            position += 2
        elif opscode == 4:
            output = program[program[position+1]]
            position += 2
        elif opscode == 5:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            if program[p1] != 0:
                position = program[p2]
            else:
                position += 3
        elif opscode == 6:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            if program[p1] == 0:
                position = program[p2]
            else:
                position += 3
        elif opscode == 7:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            p3=calc_value(program,modes[0],position+3)
            if program[p1] < program[p2]:
                program[p3] = 1
            else:
                program[p3] = 0
            position += 4
        elif opscode == 8:
            p1=calc_value(program,modes[2],position+1)
            p2=calc_value(program,modes[1],position+2)
            p3=calc_value(program,modes[0],position+3)
            if program[p1] == program[p2]:
                program[p3] = 1
            else:
                program[p3] = 0
            position += 4
        elif opscode == 99:
            break
        else:
            print("Wrong code")
            print(opscode)
            sys.exit(1)

    return output


def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    solution = 0
    for sequence in list(permutations(range(5), 5)):
        output=0
        for seq in sequence:
            p = list(program)
            input = output
            output = intcode(p, seq, input)
        if output > solution:
            solution = output

    print ('solution: '+ str(solution))

if __name__ == '__main__':
    main()
