def is_even(x): # determines if a number is even
    if x % 2 == 0:
        return True
    else:
        return False
    
def is_int(x): # takes input and returns true if it is an integer
    if x - int(x) == 0:
        return True
    else:
        return False
    
def digit_sum(n): # takes a positive integer and returns the sum of all digits
    p = 0
    while n != 0:
        p += n % 10
        n = n // 10
    return p

def factorial(x): # calculate factorial by multipling all numbers in a range from 1 through x (must be positive integer)
    total = 1
    for n in range(1,x+1):
        total = total * n
    return total
    
    
def is_prime(x): #determines if number x is prime number
    if x < 2:
        return False
    elif x == 2 or x ==3:
        return True
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
                break
        return True
    
def reverse(text): #takes a string as input and returns it in reverse order
    new_text = ""
    for i in range(len(text), 0, -1):
        new_text += text[i-1]
    return new_text

def anti_vowel(text): #removes vowels from string
    result = ""
    
    for l in text:
        if l not in "aeiouAEIOU":
            result += l
    return result

# takes a string as input and finds the scrabble score for the string
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    word_score = 0
    for l in word:
        word_score += score[l]
    return word_score

#takes two strings, text and word, as input. It return the text with the word you chose replaced with asterisks.
def censor(text, word): 
    text = text.replace(word, "*" * len(word))
    return text

#takes two arguments, list and item, that returns the number of times the item occurs in the list
def count(sequence, item):
    total = 0
    for i in sequence:
        if i is item:
            total += 1
    return total

# take a list of numbers and removes all odd numbers and returns remaining even numbers 
def purify(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

# takes list of integers and returns product of all items
def product(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total

# takes a list as input and removes items that are the same
def remove_duplicates(seq):
    new_seq = []
    for i in seq:
        if i not in new_seq:
            new_seq.append(i)
    return new_seq

# takes a list of integers and returns median value in list
def median(seq): 
    seq.sort() 
    #n = len(seq)
    if len(seq) % 2 == 0: #determine if even number of items in list
        med = (len(seq) / 2)
        return (seq[med] + (seq[med - 1])) / 2.0
    else:
        med = (len(seq) / 2)
        return seq[med]
    
    
    