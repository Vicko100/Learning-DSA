def locate_card(card, query):
  # Create a position that would be used to compare the position of the query
  position = 0

  # Create a loop for repition (if )
  while True:
    
    if card[position] == query:
      return position 
    # This means the query is indeed the current card's position (0: the first card) 

    position += 1
    # This increments the position number if the above condition is not met(i.e the current card position is not equal to the query) 

    if position == len(card):
      return -1
    # This outputs -1 if the query is not in the pile of cards 

test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 4
  },
  'output': 4
}

    
result = locate_card(test['input']['cards'], test['input']['query'])

print(result)

print(result == test['output'])