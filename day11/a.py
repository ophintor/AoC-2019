import sys, time
from os import system, name

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

def intcode(program,input_instr,position,offset):
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
            p1=calc_value(program,modes[2],position+1,offset)
            write_array(program,p1,input_instr)
            position += 2
        elif opscode == 4:
            p1=calc_value(program,modes[2],position+1,offset)
            while len(program) <= p1:
                program.append(0)
            output = program[p1]
            position += 2
            return output, position, offset
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
            return -1, position, offset
        else:
            print("Wrong code: " + str(opscode))
            sys.exit(1)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def paint(panel,x,y,facing,speed=0.1):
    clear()
    current = panel[x][y]

    if facing == 0:
        panel[x][y] = '^'
    elif facing == 1:
        panel[x][y] = '>'
    elif facing == 2:
        panel[x][y] = 'v'
    elif facing == 3:
        panel[x][y] = '<'

    print (len(panel[0]) * '- ')
    for i in range(len(panel)):
        print(' '.join(panel[i]))
    panel[x][y] = current
    print (len(panel[0]) * '- ')
    time.sleep(speed)

def robot(program):
    position = 0
    offset = 0
    finished = 0
    size = 70
    panel   = [[' ' for x in range(int(size*1.2))] for y in range(size)]
    painted = [[ 0  for x in range(int(size*1.2))] for y in range(size)]
    x,y = size/2,size/2
    facing = 0    # 0 up, 1 right, 2 down, 3 left

    while not finished:
        color = 0 if panel[x][y] == ' ' else 1
        color,position,offset = intcode(program,color,position,offset)
        direction,position,offset  = intcode(program,color,position,offset)
        panel[x][y] = ' ' if color == 0 else '#'
        painted[x][y] = 1

        if direction == -1:
            finished = 1
        else:
            if direction == 0:
                facing = (facing + 3) % 4
            elif direction == 1:
                facing = (facing + 1) % 4
            else:
                print("wrong direction")
                sys.exit(1)

            if facing == 0:
                x -= 1
            elif facing == 1:
                y += 1
            elif facing == 2:
                x += 1
            elif facing == 3:
                y -= 1

            paint(panel,x,y,facing)

    count=0
    for i in range(len(painted)):
        for j in range(len(painted[i])):
            count += painted[i][j]

    return count

def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    sol = robot(program)
    print (sol)

if __name__ == '__main__':
    main()
