import random


def shuffle():
    # how many decks should i have? start with 1
    cards = []
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for i in suits:
        for j in values:
            cards.append((j, i))
    deck = random.sample(cards, k=len(cards))
    return deck


def draw(person, deck):
    person.append(deck[0])
    deck = deck[1:]
    return deck


# def dealer():
# this function should be called when there is no more drawing for the
# player

def counter(cards):
    count = []
    for i in range(len(cards)):
        if cards[i][0] == "King":
            count.append(10)
        elif cards[i][0] == "Queen":
            count.append(10)
        elif cards[i][0] == "Jack":
            count.append(10)
        else:
            count.append(int(cards[i][0]))
    return sum(count)
        

def game():
    deck = shuffle()
    player = []
    dealer = []
    for i in range(2):
        deck = draw(player, deck)
        deck = draw(dealer, deck)
    print("Player: ", player)
    print("Dealer: ", dealer)
    if counter(player) < 21:
        while input("Hit or stick? (h/s)") == 'h':
            deck = draw(player, deck)
            print("Player: ", player)
    print(counter(player))


if __name__ == '__main__':
    game()
