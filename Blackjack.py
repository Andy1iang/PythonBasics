import random
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
suits_symbols = {'Diamonds': '♦', 'Hearts': '♥', 'Spades': '♠', 'Clubs': '♣'}
ranks = ('2 ', '3 ', '4 ', '5 ', '6 ', '7 ',
         '8 ', '9 ', '10', 'J ', 'Q ', 'K ', 'A ')
values = {'2 ': 2, '3 ': 3, '4 ': 4, '5 ': 5, '6 ': 6, '7 ': 7,
          '8 ': 8, '9 ': 9, '10': 10, 'J ': 10, 'Q ': 10, 'K ': 10, 'A ': 1}
blank = ['┌─────────┐', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│',
         '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '│░░░░░░░░░│', '└─────────┘']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.symbol = suits_symbols[suit]
        self.value = values[rank]
        self.face = ['┌─────────┐', f'│{rank}       │', '│         │',
                     '│         │', f'│    {suits_symbols[suit]}    │', '│         │',
                     '│         │', f'│       {rank}│', '└─────────┘']

    def __str__(self):
        return (f'Suit: {self.suit} \nRank: {self.rank}')


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        for i in range(0, random.randint(0, 10)):
            random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        return (f'There are {len(self.all_cards)} left in the deck')


class Player:
    def __init__(self):
        self.money = 100
        self.hand_value = 0
        self.hand_image = ['', '', '', '', '', '', '', '', '']

    def get_card(self, card):
        if card.rank == 'A ' and self.hand_value < 11:
            self.hand_value += 11
        else:
            self.hand_value += card.value
        for index, line in enumerate(card.face):
            self.hand_image[index] += line + '\t'

    def make_bet(self):
        bet = "Wrong"
        in_range = False
        while bet.isdigit() == False or in_range == False:
            bet = input('Please Place Your Bet\n')
            if not bet.isdigit():
                print('Please enter an integer')
            if bet.isdigit():
                if int(bet) > self.money and int(bet) > 0:
                    print('Insufficient Funds')
                elif int(bet) <= self.money and int(bet) > 0:
                    in_range = True
                    self.money -= int(bet)
        return int(bet)

    def print_hand(self):
        for line in self.hand_image:
            print(line)

    def __str__(self):
        return (f'Current Balance: {self.money}')

    def win(self, bet):
        self.money += bet*2

    def print_dealer_hand(self):
        for index, line in enumerate(self.hand_image):
            print(f'{blank[index]}\t{line[12::]}')

    def check_pop(self):
        if self.hand_value <= 21:
            return False
        elif self.hand_value > 21:
            return True


if __name__ == '__main__':
    game_on = True
    gamer = Player()
    dealer = Player()
    while game_on:
        print('\n'*100)
        # Set all variables to default at start of each game
        gamer.hand_value = 0
        gamer.hand_image = ['', '', '', '', '', '', '', '', '']
        dealer.hand_value = 0
        dealer.hand_image = ['', '', '', '', '', '', '', '', '']
        bet = None
        game_deck = Deck()
        game_deck.shuffle()

        # Shows current balance and takes bet
        print(gamer)
        bet = gamer.make_bet()
        print('\n'*100)

        # Deals a card for each player and shows the board
        dealer.get_card(game_deck.deal())
        gamer.get_card(game_deck.deal())
        dealer.get_card(game_deck.deal())
        gamer.get_card(game_deck.deal())
        dealer.print_dealer_hand()
        gamer.print_hand()
        print('\n'*20)

        # Asks player if they want one more card
        while not gamer.check_pop():
            hit_me = 'WRONG'
            while hit_me.lower() != 'y' and hit_me.lower() != 'n':
                hit_me = input('One More? (Y/N)')
            if hit_me.lower() == 'y':
                gamer.get_card(game_deck.deal())
                print('\n'*50)
                dealer.print_dealer_hand()
                gamer.print_hand()
                print('\n'*20)
            elif hit_me.lower() == 'n':
                break
        if gamer.hand_value > 21:
            print('\n'*50)
            dealer.print_hand()
            gamer.print_hand()
            print('BUST!')
            print('\n'*20)
            still_play = 'WRONG'
            while still_play.lower() != 'y' and still_play.lower() != 'n':
                still_play = input('Keep Playing? (Y/N)')
            if still_play.lower() == 'y':
                continue
            else:
                break
        print('\n'*50)
        dealer.print_hand()
        gamer.print_hand()
        print('\n'*20)
        while dealer.hand_value < gamer.hand_value:
            dealer.get_card(game_deck.deal())
            time.sleep(1.5)
            print('\n'*50)
            dealer.print_hand()
            gamer.print_hand()
            print('\n'*20)
        if dealer.hand_value > 21:
            print('Dealer Busts, Player Wins!')
            gamer.win(bet)
        elif dealer.hand_value == gamer.hand_value:
            print('Tie')
            gamer.win(bet/2)
        elif dealer.hand_value > gamer.hand_value:
            print('Player Loses!')
        still_play = 'WRONG'
        while still_play.lower() != 'y' and still_play.lower() != 'n':
            still_play = input('Keep Playing? (Y/N)')
            if still_play.lower() == 'y':
                continue
            else:
                game_on = False
                break