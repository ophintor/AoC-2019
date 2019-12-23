import sys

def sort_cards(deal, deck):

    if deal.count("deal with increment") > 0:
        new_deck = [-1 for x in range(len(deck))]
        increment = int(deal.split(' ')[-1:][0])
        print("Dealing with increment " + str(increment))
        for index, card in enumerate(deck):
            position = (index * increment) % len(deck)
            while new_deck[position] != -1:
                position = (position + 1) % len(deck)
            new_deck[position] = card
    elif deal.count("deal into new stack") > 0:
        new_deck = []
        print("Dealing into new stack")
        for index, card in enumerate(deck):
            new_deck.insert(0,card)
    elif deal.count("cut ") > 0:
        new_deck = []
        cut_point = int(deal.split(' ')[-1:][0])
        print("Cutting " + str(cut_point))
        cut_1 = deck[cut_point:]
        cut_2 = deck[:cut_point]
        for item in cut_1:
            new_deck.append(item)
        for item in cut_2:
            new_deck.append(item)


    return new_deck


def main():
    filename = 'input.txt'
    size = 10007

    deck = [int(x) for x in range(size)]

    with open(filename) as f:
        deals = f.read().splitlines()

    for deal in deals:
        deck = sort_cards(deal, deck)

    print("Solution: " + str(deck.index(2019)))



if __name__ == '__main__':
    main()
