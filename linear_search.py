from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

def locate_card(cards, query):
  # Create a position variable that would be used to represent the index of the positions of cards
  position = 0

  print('cards: ', cards)
  print('query: ', query)

  # Create a loop for repition
  # We edited the loop so instead of using while True, we use this condition- this means as long as the list cards is not empty the loop will not be terminated(return -1) this is done to conter the error of test #6 which occurs as a result of an empty list cards

  while position < len(cards):
    print('position: ', position)
    if cards[position] == query:
      return position 
    # This means the query is indeed the current card's position (0: the first card) 

    position += 1
    # This increments the position number if the above condition is not met(i.e the current card position is not equal to the query) 

    if position == len(cards):
      return -1
    # This outputs -1 if the query is not in the pile of cards 
  return -1

test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 4
  },
  'output': 4
}

tests = []

#1. The number 'query' occurs somewhere in the middle of the list 'cards'
tests.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 7
  },
  'output': 3
})

#2. 'query' is the first element in cards
tests.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 13
  },
  'output': 0
})

#3. 'query' is the last element in cards
tests.append({
  'input': {
    'cards': [5, 3, 1, -3, -5],
    'query': -5
  },
  'output': 4
})

#4. The list 'cards' contain just one element, which is 'query'
tests.append({
  'input': {
    'cards': [13],
    'query': 13
  },
  'output': 0
})

'''5. The list 'cards' does not contain 'query':
The question does not state what to do when the list does not contain the query, so sometimes we have to ask the interviewer to restate the problem to crosscheck if we missed an instruction: we must also:
i. Read the problem statement carefully
ii. Look through the examples provided with the problem
iii. Make reasonable assumptions, state them and move forward.
iv. Ask the interviewer/platform for clarification

Here we assume -1 when the query is not available in the list cards
'''

tests.append({
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 12
  },
  'output': -1
})

#6. The list 'cards' is empty
tests.append({
  'input': {
    'cards': [],
    'query': 0
  },
  'output': -1
})

#7. The list 'cards' contains repeating numbers
tests.append({
  'input': {
    'cards': [8, 8, 8, 5, 5, 4, 2, 2, 1],
    'query': 4
  },
  'output': 5
})

#8. The number 'query' occurs at more than one positions in 'cards': we expect the function to return the position of query's first occurence
tests.append({
  'input': {
    'cards': [8, 8, 8, 5, 5, 4, 2, 2, 1],
    'query': 5
  },
  'output': 3
})

''' Come up with a correct solution for the problem, stating it in plain English (Algorithm)
The simplest solution to a problem is to check out all the possile outcomes. This is called 'brute force' solution
for this problem we can follow this simple algorithm:
1. Create a variable 'position' and assign it the value 0
2. Check if the number to pick is index number of 'position'(0)
3. We return the current value of position if step 2 is indeed true 
4. If not, we increment the value of 'position' by 1, we repeat steps 2 to 5 till we reach the last position  
5. If the query is not in cards, we return -1

This type of algorithm is called 'Linear Search'
'''
#Next we implement the algorithm see linear_search.py

# print(tests)
    
result = locate_card(test['input']['cards'], test['input']['query'])

print(result)

print(result == test['output'])

# evaluate_test_case(locate_card, test)
evaluate_test_cases(locate_card, tests)