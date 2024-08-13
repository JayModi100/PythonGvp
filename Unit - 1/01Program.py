# A card is drawn at random from a deck of well-shuffled cards. Find the probability of it being neither a king nor a spade

#A card is drawn_card at random
drawn_card = 1

# Total number of cards
total_cards = 52  


# Number of kings 
kings = 4  

# Number of spades 
spades = 13  

# Number of king of spades
king_of_spades = 1  


# Calculate the number of card are reamining
remaining_card = total_cards - kings - spades + king_of_spades
                    
# Calculate the probability
probability = drawn_card*(remaining_card / total_cards)

# Print the result
print("The probability of drawing neither a king nor a spade is:{0:.2f}".format(probability))