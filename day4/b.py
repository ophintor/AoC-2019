def adyacents_in_it(n):
    dig0=int(str(n)[0])
    dig1=int(str(n)[1])
    dig2=int(str(n)[2])
    dig3=int(str(n)[3])
    dig4=int(str(n)[4])
    dig5=int(str(n)[5])

    if ((dig0 == dig1) and (dig1 != dig2)) or \
        ((dig1 == dig2) and (dig1 != dig0) and (dig2 != dig3)) or \
        ((dig2 == dig3) and (dig2 != dig1) and (dig3 != dig4)) or \
        ((dig3 == dig4) and (dig3 != dig2) and (dig4 != dig5)) or \
        ((dig4 == dig5) and (dig4 != dig3)):
        return 1
    else:
        return 0

def increase_if_decreases(n):
    dig0=int(str(n)[0])
    dig1=int(str(n)[1])
    dig2=int(str(n)[2])
    dig3=int(str(n)[3])
    dig4=int(str(n)[4])
    dig5=int(str(n)[5])

    if (dig0 > dig1):
        dig1 = dig0
        dig2 = dig0
        dig3 = dig0
        dig4 = dig0
        dig5 = dig0
    elif (dig1 > dig2):
        dig2 = dig1
        dig3 = dig1
        dig4 = dig1
        dig5 = dig1
    elif (dig2 > dig3):
        dig3 = dig2
        dig4 = dig2
        dig5 = dig2
    elif (dig3 > dig4):
        dig4 = dig3
        dig5 = dig3
    elif (dig4 > dig5):
        dig5 = dig4

    new_number = (dig0 * 100000) + (dig1 * 10000) + (dig2 * 1000) + (dig3 * 100) + (dig4 * 10) + dig5
    return new_number

def main():
    count = 0
    start = 240298
    end = 784956
    number = start

    while number <= end:
        number=increase_if_decreases(number)
        if number <= end and adyacents_in_it(number):
            print ('Found: ' + str(number))
            number += 1
            count += 1
        else:
            number += 1

    print("Solution: " + str(count))

if __name__ == '__main__':
    main()
