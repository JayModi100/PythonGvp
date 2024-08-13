# To read a card as input and output if the card is lucky or not

cardDetail=input("Enter Any Suit with Card : ").lower()
cardDetail=cardDetail.strip()

suit,card=cardDetail.split()
if(suit=='diamond' or (suit=='spade' and card=='ace') or card=='king'):
  print("Card is Lucky")
else:
  print("Please,try next time")




