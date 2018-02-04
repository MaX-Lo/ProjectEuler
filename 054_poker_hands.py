"""
Task:


Rank values:
1   High Card: Highest value card.
2   One Pair: Two cards of the same value.
3   Two Pairs: Two different pairs.
4   Three of a Kind: Three cards of the same value.
5   Straight: All cards are consecutive values.
6   Flush: All cards of the same suit.
7   Full House: Three of a kind and a pair.
8   Four of a Kind: Four cards of the same value.
9   Straight Flush: All cards are consecutive values of same suit.
10  Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

"""
import time


def main():
    start_time = time.time()

    data = read_file("054_poker.txt")
    print(data)

    print("time:", time.time() - start_time)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split(' '))
    return data_set


def highest_rank(hand):
    """
    get rank with according card from player 1 and 2
    if tie remove cards involved in that card, get rank again and compare once mor
    repeat until winner is definite

    :returns (rank, with which card)
    """


def is_one_pair(hand):
    """
    :param hand: player hand as "4S", "6S", "AS", "QS", "4D"
    :return: (2, card) (rank of one pair, card with which one pair is formed)
    """
    num_of_this_card = {}
    for card in hand:
        if card[0] in num_of_this_card[card[0]]:
            num_of_this_card[card[0]] += 1
        else:
            num_of_this_card[card[0]] += 1

    for card in num_of_this_card:
        if num_of_this_card[card] == 4:
            return 8, card, 
        if num_of_this_card[card] == 3:
            return 4

        if num_of_this_card[card] == 2:
            return 2, card


def is_full_house(hand):
    num_of_this_card = {}
    for card in hand:
        if card[0] in num_of_this_card[card[0]]:
            num_of_this_card[card[0]] += 1
        else:
            num_of_this_card[card[0]] += 1

    # full house
    if 3 in num_of_this_card.values() and 2 in num_of_this_card.values():
        first = None
        second = None
        for card in num_of_this_card:
            if num_of_this_card[card] == 3:
                first = card
        for card in num_of_this_card:
            if num_of_this_card[card] == 2:
                second = card

        if not first  or not second:
            print("Error while detecting a Full House")
        return 7, first, second
    else:
        return -1, '-1', '-1'


def compare_card(card1, card2):
    """
    :param card1:
    :param card2:
    :return: 1 if card1 is higher, 2 if card2 is higher, 0 if it's a tie
    """
    if card_to_int(card1) == card_to_int(card2):
        return 0
    elif card_to_int(card1) > card_to_int(card2):
        return 1
    else:
        return 2


def card_to_int(card):
    if not card.isalpha():
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == "A":
        return 14
    else:
        print("unknown card!", card)


if __name__ == '__main__':
    main()
