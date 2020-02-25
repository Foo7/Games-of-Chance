import random

#Write your game of chance functions here

#---------------
# Heads or Tails

def coin_flip(guess, bet):
    
    if bet <= 0:
        print("Your bet should be above 0")
        return 0
    
    elif bet > money:
        print("You don´t have that much money, please select a lower amount")
        return 0
    
    elif ("Heads" == guess) or ("Tails" == guess):
        print("Let's play some Coin Flip!")
        print("You bet " + str(bet) + " USD on " + guess)

        num = random.randint(1, 2)

        if (num == 1 and "eads" in guess) or (num == 2 and "ails" in guess):
            print("It's " + guess + "! You Win " + str(bet * 2) + " USD :)")
            return (bet * 2)
    
        elif (num == 2 and guess == "Heads"):
            print("It's Tails! You Lose " + str(bet * 2) + " USD :(")
            return -(bet * 2)
    
        elif (num == 1 and guess == "Tails"):
            print("It's Heads! You Lose " + str(bet * 2) + " USD :(")
            return -(bet * 2)
    else:
        print("'" + str(guess) + "' is not a valid guess in Coin Flip, please select either 'Heads' or 'Tails'")
        return 0



#---------------
# Cho-Han

def cho_han(guess, bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0
    
    elif bet > money:
        print("You don´t have that much money, please select a lower amount")
        return 0
    
    elif ("Even" == guess) or ("Odd" == guess):
        print("Let's play some Cho-Han!")
        print("You bet " + str(bet) + " USD on " + guess)

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        print("The dices are rolling and... " + str(total) + "!")

        if (total % 2 == 0 and guess == "Even") or (total % 2 != 0 and guess == "Odd"):
            print("It's " + guess + "! You Win " + str(bet * 2) + " USD :)")
            return (bet * 2)

        elif (total % 2 == 0 and guess == "Odd"):
            print("It's Even! You Lose " + str(bet * 2) + " USD :(")
            return -(bet * 2)

        elif (total % 2 != 0 and guess == "Even"):
            print("It's Odd! You Lose " + str(bet * 2) + " USD :(")
            return -(bet * 2)
    
    else:
        print("'" + str(guess) + "' is not a valid guess in Cho-Han, please select either 'Even' or 'Odd'")
        return 0




#---------------
# Cards

def cardtranslate(card):
    if card >= 2 and card <= 10:
        return card
    elif card == 11:
        return "Jack"
    elif card == 12:
        return "Queen"
    elif card == 13:
        return "King"
    elif card == 14:
        return "Ace"

def cards(bet):
    if bet <= 0:
        print("Your bet should be above 0")
        return 0
    
    elif bet > money:
        print("You don´t have that much money, please select a lower amount")
        return 0
    
    print("Let's play some Cards!")
    print("You bet " + str(bet) + " USD. Higher card wins...")

    player = random.randint(2, 14)
    house = random.randint(2, 14)
    suit = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

    if player > house:
        print("You smirk as you draw a " + str(cardtranslate(player)) + " of " + str(random.choice(suit)) + ". House trembles and draws a " + str(cardtranslate(house)) + " of " + str(random.choice(suit)) + "! You win " + str(bet * 2) + " USD :)")
        return (bet * 2)
    
    elif player < house:
        print("You sweat as you draw a " + str(cardtranslate(player)) + " of " + str(random.choice(suit)) + ". House laughs at your pathetic card as it draws a " + str(cardtranslate(house)) + " of " + str(random.choice(suit)) + "! You lose " + str(bet * 2) + " USD :(")
        return -(bet * 2)
    
    elif player == house:
        print("You are unsure but draw a " + str(cardtranslate(player)) + " of " + str(random.choice(suit)) + ". House takes pity on you and draws a " + str(cardtranslate(house)) + " of " + str(random.choice(suit)) + "! It's a tie!")
        return 0



#---------------
# Roulette

def roulette(guess, bet):
    
    if bet <= 0:
        print("Your bet should be above 0")
        return 0
    
    elif bet > money:
        print("You don´t have that much money, please select a lower amount")
        return 0
    
    elif (type(guess) == str) and (guess not in ["Even", "Odd", "00"]):
        print("'" + str(guess) + "' is not a valid guess in Roulette, please select either 'Even', 'Odd', '00' or a number between 0 and 36")
        return 0
    
    elif ((guess in ["Even", "Odd", "00"])) or ((guess >= 0) and (guess <= 36)):
        print("Let's play some Roulette!")
        print("You bet " + str(bet) + " USD on " + str(guess))

        pocket = random.randint(0, 37)

        if pocket % 2 == 0 and pocket != 0 and pocket != 37 and guess == "Even": 
            print("Roulette stops rolling and it's... " + str(pocket) + ". You win " + str(bet * 2) + "$ USD :)")
            return (bet * 2)

        elif pocket % 2 != 0 and guess == "Odd":
            print("Roulette stops rolling and it's... " + str(pocket) + ". You win " + str(bet * 2) + "$ USD :)")
            return (bet * 2)

        elif pocket == 37 and guess == "00":
            print("Roulette stops rolling and it's... 00. You win " + str(bet * 35) + "$ USD :)")
            return (bet * 35)

        elif pocket == guess and guess != 37:
            print("Roulette stops rolling and it's... " + str(pocket) + ". You win " + str(bet * 35) + "$ USD :)")
            return (bet * 35)

        elif pocket != guess and pocket == 37:
            print("Roulette stops rolling and it's... 00. You loose " + str(bet * 2) + "$ USD :(")
            return -(bet * 2)

        elif pocket != guess:
            print("Roulette stops rolling and it's... " + str(pocket) + ". You loose " + str(bet * 2) + "$ USD :(")
            return -(bet * 2)
    
    else:
        print("'" + str(guess) + "' is not a valid guess in Roulette, please select either 'Even', 'Odd', '00' or a number between 0 and 36")
        return 0




#Call your game of chance functions here
money = 100
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You start with " + str(money) + "$ USD. Good Luck! :)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Heads or Tails

money += coin_flip("Heads", 10)

print("-----------------------------------------------------------")
print("You now have: " + str(money) + "$ USD")
print("-----------------------------------------------------------")


# Cho-Han
money += cho_han("Even", 10)

print("-----------------------------------------------------------")
print("You now have: " + str(money) + "$ USD")
print("-----------------------------------------------------------")

# Cards
money += cards(10)

print("-----------------------------------------------------------")
print("You now have: " + str(money) + "$ USD")
print("-----------------------------------------------------------")

# Roulette
money += roulette("Even", 10)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Your final score is: " + str(money) + "$ USD")
print("Thank you for playing! :)")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")





