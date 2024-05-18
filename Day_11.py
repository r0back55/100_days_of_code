### Section 11 ###

############### Blackjack Project #####################



############### Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_in = input("Do you want to place a wager? Type 'yes' or 'no':  ")
# game_status = True

# # <---------------------------------------------------------------------------------
# # This is first round:
# user_card_1 = random.choice(cards)
# user_card_2 = random.choice(cards)
# user_total = user_card_1+user_card_2
# print(f"User's hand: {user_card_1} & {user_card_2} (total: {user_total})")

# dealer_card_1 = random.choice(cards)
# dealer_card_2 = random.choice(cards)
# dealer_total = dealer_card_1+dealer_card_2
# print(f"Dealers's hand: {dealer_card_1} & 'X' ") 

# # <---------------------------------------------------------------------------------
# # This is where loops start:
# if user_in == 'yes':
#     def next_card():
#         user_total = user_card_1+user_card_2
#         dealer_total = dealer_card_1+dealer_card_2
#         if user_total == 21 and (dealer_total != 21 or dealer_total > 21):
#             print("BlackJack! User won!")
#         elif user_total == 21 and dealer_total == 21:
#             print("This is 'push'. Try another time.")
#         elif user_total < 21 and dealer_total < 21:
#             user_continue = input("Do you want next card? Type 'yes' or 'no':  ")
#             if user_continue == 'yes':
#                 user_card_next = random.choice(cards)
#                 user_total += user_card_next
#                 print(f"New card is: {user_card_next}")
#                 print(f"User's total is now: {user_total}")
#                 if user_total == 21:
#                     print("BlackJack! User won!")
#                 elif user_total > 21:
#                     print(f"Dealer's second card was {dealer_card_2} (total: {dealer_total}).")
#                     print("Dealer won!")
#                 else:
#                     next_card()
#             else:
#                 if user_total > dealer_total:
#                     print(f"Dealer's second card was {dealer_card_2} (total: {dealer_total}).")
#                     print("User won!")
#                 else:
#                     print(f"Dealer's second card was {dealer_card_2} (total: {dealer_total}).")
#                     print("Dealer won!")

# next_card()


# <---------------------------------------------------------------------------------
# <---------------------------------------------------------------------------------
# This is ChatGPT:
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_in = input("Do you want to place a wager? Type 'yes' or 'no':  ")

if user_in.lower() == 'yes':
    # First round
    user_cards = [random.choice(cards), random.choice(cards)]
    user_total = sum(user_cards)
    print(f"User's hand: {user_cards[0]} & {user_cards[1]} (total: {user_total})")

    dealer_cards = [random.choice(cards), random.choice(cards)]
    dealer_total = sum(dealer_cards)
    print(f"Dealer's hand: {dealer_cards[0]} & 'X'")

    def user_turn():
        global user_total
        while user_total < 21:
            user_continue = input("Do you want the next card? Type 'yes' or 'no':  ")
            if user_continue.lower() == 'yes':
                new_card = random.choice(cards)
                user_cards.append(new_card)
                user_total = sum(user_cards)
                print(f"New card is: {new_card}")
                print(f"User's total is now: {user_total}")
                if user_total == 21:
                    print("BlackJack! User won!")
                    return True
                elif user_total > 21:
                    print(f"User busts! Dealer won!")
                    return False
            else:
                break
        return None

    def dealer_turn():
        global dealer_total
        while dealer_total < 17:
            new_card = random.choice(cards)
            dealer_cards.append(new_card)
            dealer_total = sum(dealer_cards)
        print(f"Dealer's cards were {dealer_cards} (total: {dealer_total})")
        return dealer_total


    user_result = user_turn()
    if user_result is not None:
        # The game already concluded in user's turn
        pass
    else:
        dealer_result = dealer_turn()
        if user_total <= 21:
            if dealer_total > 21 or user_total > dealer_total:
                print("User won!")
            elif user_total < dealer_total:
                print("Dealer won!")
            else:
                print("This is a 'push'. Try another time.")

else:
    print("Game aborted.")
