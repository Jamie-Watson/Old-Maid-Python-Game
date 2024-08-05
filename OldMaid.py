# Family name: Watson
# Student number: 300356613
# Course: IT1 1120 
# Assignment Number 4 Game
# year 2023

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random




def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass




def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck



def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################



def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
    for i in range (len(deck)):
        if i%2==0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])
            
    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    no_pairs=[]
        
    #sort it by number
    l.sort()
    
    i=0
    stopping=len(l)-1

    #check to see if the card next to it has the same number and remove it
    while i<stopping:
        if l[i][0:-1]==l[i+1][0:-1]:
            l.pop(i)
            l.pop(i)
            stopping-=2

        else:
            i+=1

    no_pairs=l

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    for i in range(len(deck)):
        print(deck[i], end =" ")
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
    Precondition: n>=1
    '''
    flag = True
    wantedCard = int(input("Give me an integer between 1 and " +str(n)+": "))
    while flag:
        
        if wantedCard>=1 and n>=wantedCard:
            flag = False

        else:
            wantedCard = int(input("Invalid number. Please enter integer between 1 and " +str(n)+": "))
            
            
    return wantedCard

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)
    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:\n")
    print_deck(human)
    print("\n\nDo not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    #remove all duplicates
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)

    turn =1
    flag = True
    spacer="*"*20

    #until game ends
    while flag:
        print(spacer)

        #player turn
        if turn>0:
            print("Your Turn.\n")
            print("Your current deck of cards is:\n")
            print_deck(human)
            print("\n\nI have",len(dealer),"cards. If 1 stands for my first card and\n"+ str(len(dealer))+ " for my last card, which of my cards would you like?")
            cardNum=get_valid_input(len(dealer))

            #if statements for the right ending
            ending=""
            if cardNum%10==1:
                ending+="st"
            elif cardNum%10==2:
                ending+="nd"
            elif cardNum%10==3:
                ending+="rd"
            else:
                ending+="th"

            
            print("You asked for my "+str(cardNum)+ending+" card")
            print("Here it is. It is " +dealer[cardNum-1])
            print("With",dealer[cardNum-1],"added, your current deck of cards is:\n")

            #take dealers card
            human.append(dealer[cardNum-1])
            dealer.pop(cardNum-1)
            print_deck(human)
            
            print("\n\nAnd after discarding pairs and shuffling, your deck is:\n")
            remove_pairs(human)
            print_deck(human)
            print()
            wait_for_player()

            #change turns
            turn=turn*-1

        #computer turn
        else:
            print("My turn.\n")
            cardNum=random.randrange(1,len(human))

             #if statements for the right ending
            ending=""
            if cardNum%10==1:
                ending+="st"
            elif cardNum%10==2:
                ending+="nd"
            elif cardNum%10==3:
                ending+="rd"
            else:
                ending+="th"

            
            print("I took your "+str(cardNum)+ending+" card")

            #give card to dealer
            dealer.append(human[cardNum-1])
            human.pop(cardNum-1)
            remove_pairs(dealer)
            wait_for_player()

            #change turns
            turn=turn*-1

        #after each turn check to see if there are winners
        if len(human)==0 or len(dealer)==0:
            
            print(spacer)

            if len(human)==0:
                print("Ups. You do not have any more cards\nCongratulations! You, Human, win")
            else:
                print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
            flag=False
            
            
            
        
    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
	
	 

# main
play_game()
