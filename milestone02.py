import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7, 'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13 ,'Ace':14}

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank+" of " + self.suit
two_hearts=Card(suits[0],ranks[0])
three_clubs=Card(suits[1],ranks[1])
print(two_hearts.suit)
print(two_hearts.rank)
print(two_hearts)
print(three_clubs.value)
print(two_hearts.value)
print(two_hearts.value==three_clubs.value)
print(two_hearts.value<three_clubs.value)

class Deck():
    def __init__(self):
        self.all_cards= []
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return  self.all_cards.pop() #list
        
new_Deck=Deck()
new_Deck.all_cards
first_card=new_Deck.all_cards[0]
bottom_card=new_Deck.all_cards[-1]
print("hello")
print(first_card.rank)
print(first_card.value)
print(first_card)
for card_object in new_Deck.all_cards:
    print(card_object)
print(bottom_card)
new_Deck.shuffle()
print(new_Deck.all_cards[-1])
print(bottom_card)
mycard=new_Deck.deal_one()
print(mycard)

class Player():
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):   #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)      #list of a single card object

    def __str__(self):
        return f'player name " {self.name} " has {len(self.all_cards)} cards'
new_player = Player("Hamoud")
print(new_player)
new_player.add_cards(mycard)
print(new_player.all_cards[0])
new_player.add_cards([mycard,mycard,mycard,mycard,mycard,mycard])
new_player.remove_one()

player_one=Player("one")
player_two=Player("two")
new_Deck=Deck()
new_Deck.shuffle()
for x in range(26):  #26 is the number of Deck cards
    player_one.add_cards(new_Deck.deal_one())
    player_two.add_cards(new_Deck.deal_one())
print(len(player_one.all_cards))
print(player_one.all_cards[0])
game_on=True
round_num=0
while game_on:
    round_num+=1
    print(f'round is (round_num)')
    if len(player_one.all_cards) ==0 :
        print("player one out of cards so player2  wins")
        game_on=False
        break
    if len(player_two.all_cards) == 0:
        print("player two out of cards so player1 wins")
        game_on = False
        break
    #start a new round ,if  no one from the players then the game still on
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())   #remove cards from all cards and add it to player1 cards
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())



at_war=True
while at_war:
    if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        at_war = False
    elif player_one_cards[-1].value < player_two_cards[-1].value:
         player_two.add_cards(player_two_cards)
         player_two.add_cards(player_one_cards)
         at_war = False
    else:
        print("WAR!")
        if len(player_one.all_cards) < 3 :
            print("player 1 unable to play")
            print("player 2 wins")
            game_on=False
            Break

        elif len(player_two.all_cards) < 3:
            print("player 2 unable to play")
            print("player 1 wins")
            game_on = False
            Break
        else:
            for num in range(3):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())




