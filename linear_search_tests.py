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
7. The list 'cards' contains repeating numbers
8. The number 'query' occurs at more than one positions in 'cards'
9. The numbers in 'cards' can contain negative numbers 

'''

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_cards(cards, query)
print(result)

result == output

# locate_cards(**test['input']) == test['output']

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

'''5. The list 'cards' does not contain 'query':
The question does not state what to do when the list does not contain the query, so sometimes we have to ask the interviewer to restate the problem to crosscheck if we missed an instruction: we must also:
i. Read the problem statement carefully
ii. Look through the examples provided with the problem
iii. Make reasonable assumptions, state them and move forward.
iv. Ask the interviewer/platform for clarification

Here we assume -1 when the query is not available in the list cards
'''

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

print(test)