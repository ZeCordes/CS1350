import re

'''
practice 1_a
'''

# Match years (exactly 4 digits)
text = "Born in 1995, graduated 2017, now it's 24"
pattern = r"\d{___}"  # Fill in the repetition

matches = re.findall(pattern, text)
print(f"Years found: {matches}")

'''
practice 1_b
'''
# Validate hex color codes (#RGB or #RRGGBB)
colors = ["#FFF", "#FFFFFF", "#12AB56", "#GGG", "#12"]
# Write pattern for 3 or 6 hex digits after #
# Hint: [0-9A-Fa-f]{3} or {6}

'''
practice 1_c
'''
# Extract and validate US Social Security Numbers
# Format: XXX-XX-XXXX where X is a digit
text = "SSN: 123-45-6789, Invalid: 12-345-6789, 123-4-5678"
# Write pattern using {n} for each section

'''
practice 2_a
'''
# Match repeated words like "very very" or "really really"
text = "It's very very important and really really cool"
pattern = r"(\w+) \1"  # Fill in to match repeated words

matches = re.findall(pattern, text)
print(f"Repeated words: {matches}")

'''
practice 2_b
'''
# Extract date components (MM/DD/YYYY)
dates = ["12/25/2024", "01/01/2025", "13/40/2024"]
# Write pattern with groups for month, day, year
# Validate and extract each component

'''
practice 2_c
'''
# Parse URLs: protocol://domain/path
urls = ["http://example.com/page", "https://site.org/path/to/file"]
# Create groups for protocol, domain, and path
# Print each component separately

'''
practice 3_a
'''
# Extract name and age from text
text = "My name is Alice and I am 25 years old"
pattern = r"name is (\w+) and I am (\d+)"

# Complete the code to print name and age separately
match = re.search(pattern, text)
if match:
    # Print the captured groups
    pass

'''
practice 3_b
'''
# Parse email addresses with named groups
emails = ["john.doe@company.com", "alice_smith@university.edu"]
# Write pattern with named groups for username and domain
# Pattern: (?P<user>...) @ (?P<domain>...)

'''
practice 3_c
'''
# Extract and validate time in HH:MM:SS format
times = ["12:30:45", "25:00:00", "10:65:30", "09:15:22"]
# Write pattern with groups for hours, minutes, seconds
# Validate each component (hours: 00-23, minutes/seconds: 00-59)

'''
practice 4_a
'''
text = "Hello there! Hi everyone. Hey you. Goodbye."
pattern = r"___"  # Fill in: Match Hello, Hi, or Hey

matches = re.findall(pattern, text)
print(f"Greetings: {matches}")

'''
practice 4_b
'''
# Validate file extensions for documents
files = ["report.doc", "image.jpg", "data.xlsx", "notes.txt"]
# Match .doc, .docx, .pdf, or .txt files
# Use alternation with proper grouping

'''
practice 4_c
'''
# Parse different date formats
dates = ["2024-01-15", "15/01/2024", "Jan 15, 2024", "January 15, 2024"]
# Write pattern to match:
# - YYYY-MM-DD
# - DD/MM/YYYY
# - Mon DD, YYYY
# Use alternation to handle all formats

'''
practice 5-a
'''
# Find a number and print its position
text = "The temperature is 72 degrees"
pattern = r"\d+"

match = re.search(pattern, text)
if match:
    # Print the number and where it was found
    # Use match.group() and match.span()
    pass

'''
practice 5_b
'''
# Extract URL components and their positions
url = "https://www.example.com/path/to/page"
pattern = r"(https?)://([^/]+)(.*)"

# Use the match object to extract:
# - Protocol (http or https)
# - Domain
# - Path
# - Position of each component

'''
practice 5_c
'''
# Build a function that returns match details as dictionary
def get_match_info(text, pattern):
    """
    Return dictionary with:
    - 'found': Boolean
    - 'match': The matched text
    - 'groups': All captured groups
    - 'position': (start, end) tuple
    - 'before': Text before match
    - 'after': Text after match
    """
    # Implement this function
    pass

# Test with: "Price: $19.99 (discounted)"
# Pattern: r"\$(\d+)\.(\d{2})"

'''
practice 6_a
'''
# Check if string starts with "Hello"
texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
pattern = r"Hello"

for text in texts:
    # Use re.match to check if text starts with Hello
    # Print whether it matches or not
    pass

'''
practice 6_b
'''
# Validate phone number format from start of string
# Format: (XXX) XXX-XXXX or XXX-XXX-XXXX
phones = ["(555) 123-4567", "555-123-4567", "Call 555-1234", "123-4567"]
# Write validation using re.match

'''
practice 6_c
'''
# Parse variable assignments (var = value)
assignments = ["x = 10", "name = 'John'", "flag = True", "= invalid", "no equals"]
# Write pattern to match and extract variable name and value
# Pattern should match from start: variable_name = value