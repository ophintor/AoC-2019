import sys

def sort_cards(deal, deck):

    if deal.count("deal with increment") > 0:
        new_deck = [-1 for x in range(len(deck))]
        increment = int(deal.split(' ')[-1:][0])
        # print("Dealing with increment " + str(increment))
        for index, card in enumerate(deck):
            position = (index * increment) % len(deck)
            while new_deck[position] != -1:
                position = (position + 1) % len(deck)
            new_deck[position] = card
    elif deal.count("deal into new stack") > 0:
        new_deck = []
        # print("Dealing into new stack")
        for index, card in enumerate(deck):
            new_deck.insert(0,card)
    elif deal.count("cut ") > 0:
        new_deck = []
        cut_point = int(deal.split(' ')[-1:][0])
        # print("Cutting " + str(cut_point))
        cut_1 = deck[cut_point:]
        cut_2 = deck[:cut_point]
        for item in cut_1:
            new_deck.append(item)
        for item in cut_2:
            new_deck.append(item)

    return new_deck


def find_patterns(solutions):
    for m in range(1,int(len(solutions)/10)):
        if  solutions[0]   == solutions[m]   == solutions[m*2]   == solutions[m*3]   == solutions[m*4] and \
            solutions[0+1] == solutions[m+1] == solutions[m*2+1] == solutions[m*3+1] == solutions[m*4+1]:
            return m
    return 0


def main():
    filename = 'input.txt'
    size = 2021
    solutions = []

    with open(filename) as f:
        deals = f.read().splitlines()

    solution_found = 0
    while not solution_found:
        deck = [int(x) for x in range(size)]
        for deal in deals:
            deck = sort_cards(deal, deck)

        # print(deck)
        solutions.append(deck.index(2020))
        print("Size: " + str(size) + ", Deck(2020): " + str(deck.index(2020)))
        size_pattern = find_patterns(solutions)

        if size_pattern > 0:
            solution_found = 1
            print("Pattern found, size " + str(size_pattern))
        else:
            size += 1


if __name__ == '__main__':
    main()
