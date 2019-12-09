import sys

def main():
    filename = 'input.txt'
    pixels = []
    width = 25
    height = 6


    with open(filename) as f:
        while True:
            c = f.read(1)
            if c == '\n':
                break
            pixels.append(int(c))

    layers = len(pixels) / (width * height)
    layers_zeros = [0] * (layers)
    layers_ones = [0] * (layers)
    layers_twos = [0] * (layers)

    for l in range(layers):
        for p in range(height * width):
            index = p + (l * (height * width))
            if pixels[index] == 0:
                layers_zeros[l] += 1
            elif pixels[index] == 1:
                layers_ones[l] += 1
            elif pixels[index] == 2:
                layers_twos[l] += 1

    min=0
    for i in range(len(layers_zeros)):
        if layers_zeros[i]<layers_zeros[min]:
            min=i

    solution = layers_ones[min]*layers_twos[min]
    print(solution)


if __name__ == '__main__':
    main()
