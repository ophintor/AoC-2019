import sys

def get_opscode(x):
    return x%100

def get_modes(x):
    modes = str(x)[:-2]
    lm=len(modes)
    if lm < 3:
        modes = '0'*(3-lm) + modes
    return modes

def calc_value(prog,mode,pos,offset):
    if mode == '0':
        return prog[pos]
    elif mode == '1':
        return pos
    elif mode == '2':
        return prog[pos] + offset
    else:
        print('error')
        print(mode)
        sys.exit(1)

def write_array(prog,pos,value):
    while len(prog)<=pos:
        prog.append(0)
    prog[pos] = value

def intcode(program, input_instr=''):
    # Run the program
    position = 0
    offset = 0
    opscode = get_opscode(program[position])

    while opscode != '99':
        opscode = get_opscode(program[position])
        modes = get_modes(program[position])

        if opscode == 1:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            p3=calc_value(program,modes[0],position+3,offset)
            value1 = 0 if len(program) <= p1 else program[p1]
            value2 = 0 if len(program) <= p2 else program[p2]
            write_array(program,p3,value1+value2)
            position += 4
        elif opscode == 2:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            p3=calc_value(program,modes[0],position+3,offset)
            value1 = 0 if len(program) <= p1 else program[p1]
            value2 = 0 if len(program) <= p2 else program[p2]
            write_array(program,p3,value1 * value2)
            position += 4
        elif opscode == 3:
            if input_instr:
                p1=calc_value(program,modes[2],position+1,offset)
                write_array(program,p1,input_instr)
            position += 2
        elif opscode == 4:
            p1=calc_value(program,modes[2],position+1,offset)
            while len(program) <= p1:
                program.append(0)
            output = program[p1]
            print("OUTPUT: " + str(output))
            position += 2
        elif opscode == 5:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            if program[p1] != 0:
                position = program[p2]
            else:
                position += 3
        elif opscode == 6:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            if program[p1] == 0:
                position = program[p2]
            else:
                position += 3
        elif opscode == 7:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            p3=calc_value(program,modes[0],position+3,offset)
            if program[p1] < program[p2]:
                write_array(program,p3,1)
            else:
                write_array(program,p3,0)
            position += 4
        elif opscode == 8:
            p1=calc_value(program,modes[2],position+1,offset)
            p2=calc_value(program,modes[1],position+2,offset)
            p3=calc_value(program,modes[0],position+3,offset)
            if program[p1] == program[p2]:
                write_array(program,p3,1)
            else:
                write_array(program,p3,0)
            position += 4
        elif opscode == 9:
            p1=calc_value(program,modes[2],position+1,offset)
            offset += program[p1]
            position += 2
        elif opscode == 99:
            break
        else:
            print("Wrong code")
            print(opscode)
            sys.exit(1)


def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    intcode(program,1)


if __name__ == '__main__':
    main()
