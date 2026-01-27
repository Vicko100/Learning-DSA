'''
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them flat down in a sequence on a table. She challenges Bob to pick out a card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

'''

# Create a signature function to help visualize the function and parameters
def locate_cards(cards, query):
  pass

# TEST CASES/ EDGE CASES

'''
1. The number 'query' occurs somewhere in the middle of the list 'cards'
2. 'query' is the first element in cards
3. 'query' is the last element in cards
4. The list 'cards' contain just one element, which is 'query'
5. The list 'cards' does not contain 'query'
6. The list 'cards' is empty

'''

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_cards(cards, query)
print(result)

result == output

test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 7
  },
  'output': 3
}

locate_cards(**test['input']) == test['output']