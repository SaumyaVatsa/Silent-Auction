from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids={}
bidding_finished = False

def find_highest_bid(bidding_record):
  highest_bid =0
  winner = ''
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The Winner is {winner} with a bid of ${highest_bid}.")
      

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if cont == "no":
    bidding_finished = True
    find_highest_bid(bids)
  elif cont == "yes":
    clear()
