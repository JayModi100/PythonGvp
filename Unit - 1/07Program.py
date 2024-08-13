# # To read a card as input and output if the card is lucky or not

# cardDetail=input("Enter Any Suit with Card : ").lower()
# cardDetail=cardDetail.strip()

# suit,card=cardDetail.split()
# if(suit=='diamond' or (suit=='spade' and card=='ace') or card=='king'):
#   print("Card is Lucky")
# else:
#   print("Please,try next time")


suitDetail = input("Enter Suit Detail : ").upper()
cardDetail = input("Enter Card Detail : ").upper()

print(suitDetail," ",cardDetail)
luckySuit = ["DIAMOND","SPADES"]
luckyCard = ["JACK","ACE","7","10"]

if ((suitDetail in luckySuit) and (cardDetail in luckyCard)):
    print("You are lucky")
else:
    print("You are not")

