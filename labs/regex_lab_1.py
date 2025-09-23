import re

def practice_1a():
    # Find the word "dog" in the text
    text = "The dog barked at the mailman"
    pattern = r"dog"  # Fill in the pattern

    result = re.search(pattern, text)
    if result:
        print("Found the dog!")

def practice_1b():
    # Find "2024" in the text and print its position
    text = "The year 2024 will be exciting"
    # Write code to:
    # 1. Search for "2024"
    # 2. Print where it starts in the text
    # 3. Print the matched text

# Create a function that checks if a word exists in text
def word_exists(text, word):
    return bool(re.search(word, text))
        

# Test your function
def practice_1c():
    print(word_exists("Hello world", "world"))  # Should print True
    print(word_exists("Hello world", "python")) # Should print False
    
def practice_2a():
    # Match any vowel (a, e, i, o, u) in the text
    text = "Hello World"
    pattern = r"[aeiou]"  # Fill in the vowels

    matches = re.findall(pattern, text.lower())
    print(f"Vowels found: {matches}")

def practice_2b():
    # Find all hexadecimal digits (0-9, A-F, a-f)
    text = "Color code: #FF5A2B"
    # Write pattern to match hex digits
    # Hint: Use multiple ranges in one character class
    pattern = r'[0-9A-Fa-f]'
    
    digits = re.findall(pattern, text)
    print(digits)
    
def practice_2c():
    # Extract all non-alphabetic characters from text
    text = "Hello, World! 123"
    # Write code to find all characters that are NOT letters
    # Print them as a list
    pattern = r"[^A-Za-z]"
    print(re.findall(pattern, text))
    
def practice_3a():
    # Count how many digits are in the text
    text = "I have 2 cats and 3 dogs"
    pattern = r"\d"  # Fill in shorthand for digit

    matches = re.findall(pattern, text)
    print(f"Number of digits: {len(matches)}")  
    
def practice_3b():
    # Extract all "words" (continuous word characters)
    text = "user@email.com has user_id=12345"
    # Use \w+ to find all word chunks
    # Expected: ['user', 'email', 'com', 'has', 'user_id', '12345']
    pattern = r'\w+'
    print(re.findall(pattern, text))
    
def practice_3c():
    # Clean text by removing all non-word characters except spaces
    text = "Hello! How are you? I'm fine... Thanks!"
    # Use re.sub with \W pattern
    # syntax: re.sub(pattern, repl, string, count=0, flags=0)
    # usage: replace parts of a string that match a specific regular expression patter
    # Keep only words and spaces
    pattern = r'[^\w\s]'
    cleaned = re.sub(pattern, '', text)
    print(cleaned)
    
def practice_4a():
    # Check if string starts with "Python"
    texts = ["Python is fun", "I love Python", "Python"]
    pattern = r"____"  # Fill in pattern to match strings starting with Python

    for text in texts:
        if re.search(pattern, text):
            print(f"'{text}' starts with Python")
            
def practice_4b():
    # Validate that a string contains ONLY digits
    test_strings = ["12345", "123abc", "456"]
    # Write pattern to match strings that are entirely digits
    # Use ^ and $ anchors with \d+
    
def practice_4c():
    # Find all three-letter words ending in 'at'
    text = "The cat sat on the mat with a bat"
    # Use dot metacharacter and word boundaries
    # Word boundary: \b, can be at the beginning and end
    # Expected: ['cat', 'sat', 'mat', 'bat']
    
def practice_5a():
    # Find all words (one or more letters)
    text = "Hello 123 world 456"
    pattern = r"[a-zA-Z]___"  # Fill in the quantifier

    matches = re.findall(pattern, text)
    print(f"Words: {matches}")
    
def practice_5b():
    # Match phone numbers with optional area code
    # Format: (555) 123-4567 or 123-4567
    phones = ["(555) 123-4567", "123-4567", "555-1234"]
    # Write pattern using ? for optional area code
    # For a group of characters to be optional inside an re pattern
    # use () to group the set of characters
    
def practice_5c():
    # Extract content between quotes (non-greedy)
    text = 'He said "hello" and she said "goodbye" quickly'
    # Write pattern to extract text between quotes
    # Use non-greedy matching
    # Expected: ['hello', 'goodbye']


if __name__ == '__main__':
    practice_1a()
    practice_1b()
    practice_1c()
    practice_2a()
    practice_2b()
    practice_2c()
    practice_3a()
    practice_3b()
    practice_3c()
    practice_4a()
    practice_4b()
    practice_4c()
    practice_5a()
    practice_5b()
    practice_5c()