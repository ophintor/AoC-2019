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
                while len(program) <= p2:
                    program.append(0)
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
            return 99, position, offset
        else:
            print("Wrong code: " + str(opscode))
            sys.exit(1)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def paint(panel,x,y,score,speed):
    clear()
    print ("SCORE: " + str(score) + ' ' + str(x) + ',' + str(y))
    for i in range(len(panel)):
        print(' '.join(panel[i]))
    time.sleep(speed)

def arcade_game(program):
    position = 0
    offset = 0
    finished = 0
    size = 40
    score = 0
    joystick = -1
    screen = [[' ' for x in range(size)] for y in range(int(size*0.7))]
    previous = -1
    bar_pos = (0,0)

    program[0] = 2

    while not finished:
        x,position,offset = intcode(program,joystick,position,offset)

        if x == 99:
            finished = 1
            paint(screen,x,bar_pos[1],score,speed=0)
        else:
            y,position,offset = intcode(program,joystick,position,offset)

            if x == -1 and y == 0:
                score,position,offset = intcode(program,joystick,position,offset)
                paint(screen,x,bar_pos[1],score,speed=0)
            else:
                tile_id,position,offset = intcode(program,joystick,position,offset)

                if tile_id == 0:
                    screen[y][x] = ' '
                elif tile_id == 1:
                    screen[y][x] = '='
                elif tile_id == 2:
                    screen[y][x] = '#'
                elif tile_id == 3:
                    screen[y][x] = '_'
                    bar_pos=(x,y)
                elif tile_id == 4:
                    screen[y][x] = 'o'
                    paint(screen,x,bar_pos[1],score,speed=0.02)
                    if previous == -1:
                        joystick = 0
                    elif previous < x and bar_pos[0] <= x:
                        joystick = 1
                    elif previous > x and bar_pos[0] >= x:
                        joystick = -1
                    elif previous < x and bar_pos[0] > x:
                        joystick = -1
                    elif previous > x and bar_pos[0] < x:
                        joystick = 1
                    else:
                        joystick = 0
                    previous = x


def main():
    filename = 'input.txt'

    with open(filename) as f:
        program = [int(x) for x in f.readline().split(",")]

    arcade_game(program)

if __name__ == '__main__':
    main()
