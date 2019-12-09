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

    final_image=[2] * (width * height)

    for l in range(layers):
        for p in range(height * width):
            index = p + (l * (height * width))
            if final_image[p] == 2:
                final_image[p] = pixels[index]

    line=0
    for y in range(height):
        for x in range(width):
            index = x + (width * line)
            if final_image[index]==1:
                print '*',
            else:
                print ' ',
        line += 1
        print('')

if __name__ == '__main__':
    main()
