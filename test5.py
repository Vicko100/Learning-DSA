from jovian.pythondsa import evaluate_test_case

def locate_card(cards, query):
  position = 0

  print('cards: ', cards)
  print('query: ', query)

  while position < len(cards):
    print('position: ', position)
    if cards[position] == query:
      return position 

    position += 1

    if position == len(cards):
      return -1
  return -1
      

test5 = ({
  'input': {
    'cards': [],
    'query': 0
  },
  'output': -1
})

locate_card(**test5['input'])

evaluate_test_case(locate_card, test5)












