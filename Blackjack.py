import random
import os


def shuffle():
    cards = []
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    for i in suits:
        for j in values:
            cards.append((j, i))
    deck = random.sample(cards, k=len(cards))
    return deck


def play_again():
    if input("Do you want to play again? (Y/N) : ").lower() == "y":
        game()
    else:
        print("Bye!")
        exit()


def deal(player, dealer, deck):
    for i in range(2):
        deck = draw(player, deck)
        deck = draw(dealer, deck)


def draw(person, deck):
    person.append(deck[0])
    deck = deck[1:]
    return deck


def player_play(player, deck):
    while counter(player) <= 21:
        print("You're on: ", counter(player))
        if input("Hit or stick? (h/s)") == 'h':
            deck = draw(player, deck)
            print("\nyou've drawn {}, you're now on {}".format(player[-1], counter(player)))
            print("Player: ", player)
        else:
            break


def dealer_play(dealer, deck, player):
    if counter(player) <= 21:
        while counter(dealer) < 17:
            deck = draw(dealer, deck)
            print("\ndealer draws {}, dealers now on {}".format(dealer[-1], counter(dealer)))
    return dealer


def counter(cards):
    count = 0
    for i in range(len(cards)):
        if cards[i][0] == "King":
            count += 10
        elif cards[i][0] == "Queen":
            count += 10
        elif cards[i][0] == "Jack":
            count += 10
        elif cards[i][0] == "Ace":
            if count >= 11:
                count += 1
            else:
                count += 11
        else:
            count += int(cards[i][0])
    if count > 21:                      # Really need a better way of doing this
        a = []                          # this is bad for hard coding a -10
        for i in range(len(cards)):
            a.append(cards[i][0])
        if "Ace" in a:
            count += -10
    return count


def who_wins(player, dealer):
    if counter(dealer) > 21:
        print("Dealer went bust! You win")
    elif counter(player) > 21:
        print("oh no you're bust!, you got ", counter(player))
    elif counter(player) > counter(dealer):
        print("woo you won!")
        print("dealer got {} and you got {}".format(counter(dealer), counter(player)))
    elif counter(player) == counter(dealer):
        print("ahh its a draw..")
        print("dealer got {} and you got {}".format(counter(dealer), counter(player)))
    else:
        print("oh no dealer got {} and you got {}".format(counter(dealer), counter(player)))


def game():
    #os.system('CLS')               # Comment out for OS
    os.system('clear')              # top is windows, bottom is linux
    deck = shuffle()
    player = []
    dealer = []
    deal(player, dealer, deck)
    print("\nPlayer: ", player)
    print("Dealer: ", dealer)
    player_play(player, deck)
    dealer = dealer_play(dealer, deck, player)
    who_wins(player, dealer)
    play_again()


if __name__ == '__main__':
    game()
