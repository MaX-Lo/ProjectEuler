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

    wins = -3

    for example in data:
        hand1 = example[:5]
        hand2 = example[5:]
        rank1 = get_rank(hand1)
        rank2 = get_rank(hand2)
        if rank1 > rank2:
            wins += 1
        elif rank1 == rank2:
            if rank1 == 1:
                res = compare_highest_card_in_hands(hand1, hand2)
                if res == 1:
                    wins += 1
                elif res == 0:
                    print('same highest card', rank_to_string(rank1), ' - ', rank_to_string(rank2))
            elif rank1 == 2:
                res = compare_one_pairs(hand1, hand2)
                if res == 1:
                    wins += 1
                elif res == 0:
                    res = compare_highest_card_in_hands(hand1, hand2)
                    if res == 1:
                        wins += 1
                    elif res == 0:
                        print('same highest card', rank_to_string(rank1), ' - ', rank_to_string(rank2))
            else:
                print('same diff rank')

    print('wins', wins)
    print("time:", time.time() - start_time)


def read_file(filename):
    data_file = open(filename)
    data_set = []
    for line in data_file.readlines():
        data_set.append(line.strip().split(' '))
    return data_set


def get_rank(hand):
    """
    get rank with according card from player 1 and 2
    if tie remove cards involved in that card, get rank again and compare once mor
    repeat until winner is definite

    :returns (rank, with which card)
    """

    if is_royal_flush(hand):
        return 10
    elif is_straight_flush(hand):
        return 9
    elif is_four_of_a_kind(hand):
        return 8
    elif is_full_house(hand):
        return 7
    elif is_flush(hand):
        return 6
    elif is_straight(hand):
        return 5
    elif is_three_of_a_kind(hand):
        return 4
    elif is_two_pairs(hand):
        return 3
    elif is_one_pair(hand):
        return 2
    else:
        return 1


def is_royal_flush(hand):
    if not is_flush(hand):
        return False

    # check if Ass, King, Queen, ... are in the hand
    necessary_cards = {'A', 'K', 'Q', 'J', 'T'}
    for card in hand:
        if card[0] not in necessary_cards:
            return False
        else:
            necessary_cards.remove(card[0])

    return True


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand):
    card_counter = dict()
    for card in hand:
        if card[0] in card_counter:
            card_counter[card[0]] += 1
        else:
            card_counter[card[0]] = 1
    max_count = max(card_counter.values())
    return max_count == 4


def is_full_house(hand):
    card_counter = dict()
    for card in hand:
        if card[0] in card_counter:
            card_counter[card[0]] += 1
        else:
            card_counter[card[0]] = 1
    count = card_counter.values()
    if len(count) == 2:
        return True


def is_flush(hand):
    # check if all cards are of the same color
    hand_color = hand[0][1]
    for card in hand:
        if card[1] != hand_color:
            return False
    return True


def is_straight(hand):
    hand = [card_to_int(card[0]) for card in hand]
    hand.sort()
    last = hand[0] - 1
    for card in hand:
        if card == last + 1:
            last += 1
        else:
            return False


def is_three_of_a_kind(hand):
    card_counter = dict()
    for card in hand:
        if card[0] in card_counter:
            card_counter[card[0]] += 1
        else:
            card_counter[card[0]] = 1
    max_count = max(card_counter.values())
    return max_count == 3


def is_two_pairs(hand):
    card_counter = dict()
    for card in hand:
        if card[0] in card_counter:
            card_counter[card[0]] += 1
        else:
            card_counter[card[0]] = 1
    return len(card_counter) == 3


def is_one_pair(hand):
    card_counter = dict()
    for card in hand:
        if card[0] in card_counter:
            card_counter[card[0]] += 1
        else:
            card_counter[card[0]] = 1
    return len(card_counter) == 4


def compare_highest_card_in_hands(hand1, hand2):
    hand1_ints = [card_to_int(card[0]) for card in hand1]
    hand2_ints = [card_to_int(card[0]) for card in hand2]

    if max(hand1_ints) == max(hand2_ints):
        return 0
    elif max(hand1_ints) > max(hand2_ints):
        return 1
    else:
        return -1


def compare_one_pairs(hand1, hand2):
    hand1_ints = [card_to_int(card[0]) for card in hand1]
    hand2_ints = [card_to_int(card[0]) for card in hand2]

    pair1 = 0
    count1 = set()
    for card in hand1_ints:
        if card in count1:
            pair1 = card
        else:
            count1.add(card)
    pair2 = 0
    count2 = set()
    for card in hand2_ints:
        if card in count2:
            pair2 = card
        else:
            count2.add(card)

    if pair1 == pair2:
        return 0
    elif pair1 > pair2:
        return 1
    else:
        return -1

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


def rank_to_string(rank):
    if rank == 10:
        return 'royal flash'
    elif rank == 9:
        return 'straight flush'
    elif rank == 8:
        return 'four of a kind'
    elif rank == 7:
        return 'full house'
    elif rank == 6:
        return 'flush'
    elif rank == 5:
        return 'straight'
    elif rank == 4:
        return 'three of a kind'
    elif rank == 3:
        return 'two pairs'
    elif rank == 2:
        return 'one pair'
    else:
        return 'highest card'

if __name__ == '__main__':
    main()
