import sys

def main():
    filename = 'input.txt'
    pattern = [0,1,0,-1]
    num_phases = 100

    with open(filename) as f:
        signal = [int(x) for x in list(f.readline().strip())]

    for phase in range(num_phases):
        print ("Phase: " + str(phase))
        new_signal = []
        for i in range(len(signal)):
            phase_total = 0
            current_pattern = [x for x in pattern for _ in range(i+1)]
            if len(current_pattern)-1 < len(signal):
                current_pattern = current_pattern * ((len(signal) / len(pattern)) + 1)
            current_pattern.pop(0)
            for j in range(len(signal)):
                phase_total += signal[j] * current_pattern[j]

            new_signal.append(abs(phase_total)%10)

        signal = new_signal

    signal = [ str(x) for x in signal ]
    print (''.join(signal)[:8])

if __name__ == '__main__':
    main()
