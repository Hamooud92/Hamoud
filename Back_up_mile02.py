import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7, 'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13 ,'Ace':14}
playing=True


class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        #self.value=values[rank]
    def __str__(self):
        return self.rank+" of " + self.suit


class Deck():
    def __init__(self):
        #self.all_cards = []
        self.deck=[]  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                #created_card = Card(suit, rank)
                #self.all_cards.append(created_card)

    def __str__(self):
        deck_comp=''
        for card in  self.deck:
            deck_comp+='\n'+ card.__str__()
        return  "the deck has"+ deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        single_card=self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    def adjust_for_ace(self):
        while self.value > 21  and self.aces:
            self.value-=10
            self.aces-=1
zero=0
one=1
two=2
if zero:
    print('True')
class Chips():
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def take_bit(chips):
    while True:
        try:
            chips.bet=int(input("how many chips would u like to bet? "))
        except:
            print("sorry pls provide an integer")
        else:
            if chips.bet > chips.total:
                print("sorry,u don't have enough chips, you just have {}".format(chips.total))
            else:
                break
def hit(deck,hand):
    single_card=Deck.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input('hit or stand? Enter h or s')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("player stand")
            playing=False
        else:
            print("sorry i didn't understand that,please enter s or h only")
            continue
        break
def show_some(player,dealer):
    print("\n Dealer's hand" )
    print("first card hidden")
    print(dealer.cards[1])
    print("\n player's hand")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("\n Dealers's hand")
    for card in dealer.cards:
        print(card)
    print(f"value of dealer is : {dealer.value}")

    print("\n player's hand")
    for card in player.cards:
        print(card)
    print(f"value of player is : {player.value}")

def player_busts(player,dealer,chips):
    print("player busts ")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("player wins")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("player wins ,dealer bust ")
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print("dealer wins ")
    chips.lose_bet()
def push(player,dealer):
    print("Dealer and player tie!")

while True:
    print("welcome to black jack")
    deck=Deck()
    deck.shuffle()
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    player_hand=Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())


    player_chips=Chips()
    take_bit(player_chips)
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value >21 :
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <=21 :
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    print("\n  players total chips are at {}".format(player_chips.total))
    new_game=input("would u like to play another hand ? y/n")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thank u for playing")
        break




test_deck=Deck()
test_deck.shuffle()
print(test_deck)
test_player=Hand()
pulled_card=test_deck.deal_one()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
test_player.add_card(test_deck.deal_one())
test_player.value