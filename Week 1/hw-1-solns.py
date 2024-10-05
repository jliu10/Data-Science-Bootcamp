"""
1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
2. Iterate through the following list of animals and print each one in all caps.

  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
"""

#### 1 #########################################################################

def count_vowels(word):
    vowels = 'a','e','i','o','u'
    count = 0
    word = word.lower()
    for c in word:
        if c in vowels:
            count += 1
    return count

#### 2 #########################################################################

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

#### 3 #########################################################################

for n in range(1,21):
    parity = "even"
    if n % 2 != 0:
        parity = "odd"
    print(str(n) + " is " + parity)
    
#### 4 #########################################################################
    
def sum_of_integers(a, b):
    return a + b