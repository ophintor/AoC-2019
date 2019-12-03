def main():
    filename = 'input.txt'

    with open(filename) as f:
        lines = f.read().splitlines()

    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')

    # Calculate matrix size
    # L, U, R, D
    max_1=[0,0,0,0]
    max_2=[0,0,0,0]
    matrix_size=[0,0,0,0]

    for instr in wire1:
        if instr[0]=='L':
            max_1[0] += int(instr[1:])
        elif instr[0]=='U':
            max_1[1] += int(instr[1:])
        elif instr[0]=='R':
            max_1[2] += int(instr[1:])
        elif instr[0]=='D':
            max_1[3] += int(instr[1:])

    for instr in wire2:
        if instr[0]=='L':
            max_2[0] += int(instr[1:])
        elif instr[0]=='U':
            max_2[1] += int(instr[1:])
        elif instr[0]=='R':
            max_2[2] += int(instr[1:])
        elif instr[0]=='D':
            max_2[3] += int(instr[1:])

    matrix_size = [max(value) for value in zip(max_1, max_2)]

    # calculate starting point and init matrix
    starting_point = [matrix_size[1], matrix_size[0]]
    x_size = (matrix_size[0]+matrix_size[2]+1)
    y_size = (matrix_size[1]+matrix_size[3]+1)
    matrix = [ [0] * (x_size) for _ in range(y_size) ]
    matrix[starting_point[0]][starting_point[1]]=-1

    # Write wire 1
    pos = list(starting_point)

    for instr in wire1:
        if instr[0]=='L':
            for i in range(int(instr[1:])):
                pos[1] -= 1
                matrix[pos[0]][pos[1]]=1
        elif instr[0]=='U':
            for i in range(int(instr[1:])):
                pos[0] -= 1
                matrix[pos[0]][pos[1]]=1
        elif instr[0]=='R':
            for i in range(int(instr[1:])):
                pos[1] += 1
                matrix[pos[0]][pos[1]]=1
        elif instr[0]=='D':
            for i in range(int(instr[1:])):
                pos[0] += 1
                matrix[pos[0]][pos[1]]=1

    # Write wire 2
    pos = list(starting_point)

    for instr in wire2:
        if instr[0]=='L':
            for i in range(int(instr[1:])):
                pos[1] -= 1
                if matrix[pos[0]][pos[1]] == 1:
                    matrix[pos[0]][pos[1]] = 2
        elif instr[0]=='U':
            for i in range(int(instr[1:])):
                pos[0] -= 1
                if matrix[pos[0]][pos[1]] == 1:
                    matrix[pos[0]][pos[1]] = 2
        elif instr[0]=='R':
            for i in range(int(instr[1:])):
                pos[1] += 1
                if matrix[pos[0]][pos[1]] == 1:
                    matrix[pos[0]][pos[1]] = 2
        elif instr[0]=='D':
            for i in range(int(instr[1:])):
                pos[0] += 1
                if matrix[pos[0]][pos[1]] == 1:
                    matrix[pos[0]][pos[1]] = 2

    # Find shorter way...
    crosses_list = []

    # Check wire 1
    pos = list(starting_point)
    print("Starting wire 1 at " + str(pos[0]) + ',' + str(pos[1]))
    count1 = 0
    for instr in wire1:
            if instr[0]=='L':
                for i in range(int(instr[1:])):
                    pos[1] -= 1
                    count1 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count1))
                        matrix[pos[0]][pos[1]] = count1
                        crosses_list.append([pos[0],pos[1]])
            elif instr[0]=='U':
                for i in range(int(instr[1:])):
                    pos[0] -= 1
                    count1 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count1))
                        matrix[pos[0]][pos[1]] = count1
                        crosses_list.append([pos[0],pos[1]])
            elif instr[0]=='R':
                for i in range(int(instr[1:])):
                    pos[1] += 1
                    count1 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count1))
                        matrix[pos[0]][pos[1]] = count1
                        crosses_list.append([pos[0],pos[1]])
            elif instr[0]=='D':
                for i in range(int(instr[1:])):
                    pos[0] += 1
                    count1 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count1))
                        matrix[pos[0]][pos[1]] = count1
                        crosses_list.append([pos[0],pos[1]])

    # Check wire 2
    pos = list(starting_point)
    print("Starting wire 2 at " + str(pos[0]) + ',' + str(pos[1]))
    count2 = 0
    for instr in wire2:
            if instr[0]=='L':
                for i in range(int(instr[1:])):
                    pos[1] -= 1
                    count2 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count2))
                        matrix[pos[0]][pos[1]] += count2
            elif instr[0]=='U':
                for i in range(int(instr[1:])):
                    pos[0] -= 1
                    count2 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count2))
                        matrix[pos[0]][pos[1]] += count2
            elif instr[0]=='R':
                for i in range(int(instr[1:])):
                    pos[1] += 1
                    count2 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count2))
                        matrix[pos[0]][pos[1]] += count2
            elif instr[0]=='D':
                for i in range(int(instr[1:])):
                    pos[0] += 1
                    count2 += 1
                    if matrix[pos[0]][pos[1]] > 1:
                        print('Found cross at ' + str(pos[0]) + ',' + str(pos[1]) + ' - ' + str(count2))
                        matrix[pos[0]][pos[1]] += count2

    solution = ''
    for coords in crosses_list:
        x = matrix[coords[0]][coords[1]]
        if not solution or x < solution:
            solution = x

    print('Solution: ' + str(solution))


if __name__ == '__main__':
    main()
