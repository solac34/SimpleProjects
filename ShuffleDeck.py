import random


def shuffle(size, count, decksize):
    # finding possible errors
    if type(size) != int:  # if size is not an integer
        raise Exception('Size must be an int type')
    if type(count) != int:  # if count is not an integer
        raise Exception('Count must be an int type')
    if type(decksize) != int:  # if decks is not an integer
        raise Exception('Decksize must be an int type')
    if decksize < 1:
        raise Exception('At least one(1) deck is needed to shuffle.')
    if size * count > 52 * decksize or size * count < 0:  # if user requested a shuffle that is not possible with decksize
        raise Exception(f"Size*Count*decksize must be between 1 & 52*{decksize}")

    deck = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A', '12A', '13A', '1B', '2B', '3B', '4B',
            '5B', '6B', '7B', '8B', '9B', '10B', '11B', '12B', '13B', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C',
            '9C', '10C', '11C', '12C', '13C', '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D',
            '13D']

    current_deck = 1  # to control deck operations
    while current_deck < decksize:  # until the current deck reaches decksize,add  deck list on deck list.
        op_no = 0  # to control how many elements added to deck.
        for item in deck:
            if op_no < 52:  # each deck has 52 cardsTo stop infinite loop, when it reaches 52, iterate to next deck.
                deck.append(item)
            else:
                break
            op_no += 1

        current_deck += 1

    current_step = 1
    hands = list()
    while current_step <= count:  # to create new hand. each step equals a hand
        size_step = 0
        current_hand = list()

        while size_step < size:  # to create hand elements.each step equals a card
            current_hand.append(deck[random.randint(0, len(deck) - 1)])  # add random card from deck
            deck.remove(current_hand[size_step])  # delete the card just added to stop multiple cards from a deck
            size_step += 1

        hands.append(current_hand)  # add hand to deliver list
        current_step += 1
    return hands


def builtin_shuffle(name):  # builtin deck setups like poker-pisti etc.
    # error catching
    if type(name) != str:
        raise Exception('Only string-type names are available.')

    if name.lower() == 'pisti2':  # builtin pisti shuffle
        pisti2_hand = shuffle(4, 13, 1)
        starter_hand = pisti2_hand[random.randint(0, 12)]
        pisti2_hand.remove(starter_hand)
        game_hands = pisti2_hand
        return starter_hand, game_hands
