from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

'''
How binary_search can be applied to our problem:
1. Find the middle of the list
2. If it matches the query, return the middle number as the answer
3. If it is less than the query number, search the left side of the list
4. If it is greater than the query number, search the right side of the list.
5. If no more elements remain return -1.

Why we add the test_location function; this acts as a helper function to the main function:
We implemented this function to help fix the error we face when we run test 8(Test case #7), where we have multiple occurence of the query in the cards list and the reason for this function is to return the first occurence of the query in the list

Algorithm for this function:
1. Find the middle of the list
2. Check if the middle of the list is the query 
3. If yes we check if its the only occurence in the list
'''

def test_location(cards, query, mid):
  mid_card = cards[mid]
  print(f'mid_card: {mid_card}, mid: {mid}')
  if mid_card == query:
    if (mid-1) >= 0 and cards[mid-1] == query:
      return 'left'
    else:
      return 'found'
  elif mid_card < query:
    return 'left'
  else:
    return 'right'


def locate_cards(cards, query):
  lo, hi = 0, len(cards) - 1

  while lo <= hi:
    print(f'lo: {lo}, hi: {hi}')
    mid = (lo + hi) // 2 # mid represents the index of the card in the middle
    result = test_location(cards, query, mid)

    if result == 'found':
      return mid
    elif result == 'left':
      hi = mid - 1
    elif result == 'right':
      lo = mid + 1
  return -1

test = []

#1. The number 'query' occurs somewhere in the middle of the list 'cards'
test.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 7
  },
  'output': 3
})

#2. 'query' is the first element in cards
test.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 13
  },
  'output': 0
})

#3. 'query' is the last element in cards
test.append({
  'input': {
    'cards': [5, 3, 1, -3, -5],
    'query': -5
  },
  'output': 4
})

#4. The list 'cards' contain just one element, which is 'query'
test.append({
  'input': {
    'cards': [13],
    'query': 13
  },
  'output': 0
})

#5. The list 'cards' does not contain 'query'
test.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 12
  },
  'output': -1
})

#6. The list 'cards' is empty
test.append({
  'input': {
    'cards': [],
    'query': 0
  },
  'output': -1
})

#7. The list 'cards' contains repeating numbers
test.append({
  'input': {
    'cards': [8, 8, 8, 5, 5, 4, 2, 2, 1],
    'query': 4
  },
  'output': 5
})

#8. The number 'query' occurs at more than one positions in 'cards': we expect the function to return the position of query's first occurence
test.append({
  'input': {
    'cards': [8, 8, 8, 5, 5, 5, 2, 2, 1],
    'query': 5
  },
  'output': 3
})


# result = locate_cards(test['input']['cards'], test['input']['query'])
# print(result)
# checker = result == test
# print(checker)

# evaluate_test_cases(locate_cards, test)
evaluate_test_case(locate_cards, test[7])