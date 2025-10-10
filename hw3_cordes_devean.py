import re
def format_receipt(items: list[str], prices: list[float], quantities: list[int]) -> str:
    """
    Create a formatted receipt using string methods.
    Args:
        items: List of item names
        prices: List of prices (floats)
        quantities: List of quantities (integers)
    
    Returns:
        str: Formatted receipt with aligned columns
    
    Format Requirements:
        - Item name: left-aligned, 20 characters
        - Quantity: center-aligned, 5 characters
        - Price: right-aligned, 8 characters with 2 decimal places
        - Total: right-aligned at bottom
        - Use dashes for separator lines
    
    Example:
        >>> items = ['Coffee', 'Sandwich', 'Cookie']
        >>> prices = [3.50, 8.99, 2.00]
        >>> quantities = [2, 1, 3]
        >>> print(format_receipt(items, prices, quantities))
        ========================================
        Item Qty Price
        ========================================
        Coffee 2 $ 7.00
        Sandwich 1 $ 8.99
        Cookie 3 $ 6.00
        ========================================
        TOTAL $ 21.99
        ========================================
    """
    receipt_str = '=' * 40 + '\n'
    receipt_str += 'Item Qty Price\n'
    receipt_str += '=' * 40 + '\n'
    receipt_str += '\n'.join(f'{item} {quantity} ${price:.2f}' for item, price, quantity in zip(items, prices, quantities)) + '\n'
    receipt_str += '=' * 40 + '\n'
    receipt_str += f'TOTAL ${sum(prices):.2f}\n'
    receipt_str += '=' * 40
    
    return receipt_str


def process_user_data(raw_data: dict[str, str]) -> dict[str, str]:
    """
        Clean and process user input data using string methods.
    Args:
        raw_data: Dictionary with messy user input
            - 'name': May have extra spaces, wrong capitalization
            - 'email': May have spaces, uppercase letters
            - 'phone': May have various formats
            - 'address': May have inconsistent formatting
    Returns:
        dict: Cleaned data with:
            - 'name': Properly capitalized, trimmed
            - 'email': Lowercase, no spaces
            - 'phone': Digits only
            - 'address': Title case, single spaces
            - 'username': Generated from name (first_last)
            - 'validation': Dict of validation results
    Example:
    input: {
        'name': ' john DOE ',
        'email': ' JOHN.DOE @EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street, apt 5'
    }
    output: {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'phone': '5551234567',
        'address': '123 Main Street, Apt 5',
        'username': 'john_doe',
        'validation': {
            'name': True,
            'email': True,
            'phone': True,
            'address': True
        }
    }
    """
    clean_data = {
        'validation': {}
    }
    name_pattern = r'^[a-zA-Z]+ [a-zA-Z]+$'
    email_pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]+$'
    # just check if phone has 10 digits when reduced
    address_pattern = r'^[a-zA-Z0-9\s.,]+$' # only letters, digits,
    
    clean_data['name'] = ' '.join(raw_data['name'].strip().title().split())
    clean_data['validation']['name'] = bool(re.match(name_pattern, clean_data['name']))
    
    clean_data['email'] = re.sub(r'\s', '', raw_data['email'].lower()) # remove ALL whitespace and make completely lowercase
    clean_data['validation']['email'] = bool(re.match(email_pattern, clean_data['email']))
    
    clean_data['phone'] = re.sub(r'\D', '', raw_data['phone']) # remove all non-digits
    clean_data['validation']['phone'] = len(clean_data['phone']) == 10
    
    clean_data['address'] = ' '.join(raw_data['address'].strip().title().split())
    clean_data['validation']['address'] = bool(re.match(address_pattern, clean_data['address']))
    
    clean_data['username'] = '_'.join(clean_data['name'].split()).lower()
    
    return clean_data


def analyze_text(text: str) -> dict:
    """
    Perform comprehensive text analysis using string methods.
    Args:
    text: Multi-line string of text
    Returns:
    dict: Analysis results containing:
    - 'total_chars': Total character count
    - 'total_words': Total word count
    - 'total_lines': Number of lines
    - 'avg_word_length': Average word length (rounded to 2 decimal)
    - 'most_common_word': Most frequently used word (case-insensitive)
    - 'longest_line': The longest line in the text
    - 'words_per_line': List of word counts per line
    - 'capitalized_sentences': Number of sentences starting with capital
    - 'questions': Number of sentences ending with '?'
    - 'exclamations': Number of sentences ending with '!'
    Example:
    >>> text = '''Hello world! How are you?
    ... This is a test. Another line here!'''
    >>> result = analyze_text(text)
    >>> result['total_words']
    11
    >>> result['questions']
    1
    """
    words = [word.lower() for word in re.findall(r'\w+', text)]
    analysis = {
        'total_chars': len(text), # including whitespace
        'total_words': len(words),
        'total_lines': text.count('\n') + 1
    } # initialize with easy to calculate
    analysis['avg_word_length'] = round(len(''.join(words)) / analysis['total_words'], 2) # num of chars in words / num of words
    analysis['most_common_word'] = max(words, key = lambda x: words.count(x))
    analysis['longest_line'] = max(text.split('\n'), key=len)
    analysis['words_per_line'] = [len(re.findall(r'\w+', line)) for line in text.split('\n')]
    
    analysis['capitalized_sentences'] = 0
    analysis['questions'] = 0
    analysis['exclamations'] = 0
    
    sentence_pattern = r'\w[^.!?]*[.!?]' # at least one 'word' char
    for sentence_match in re.finditer(sentence_pattern, text):
        sentence = sentence_match.group().strip()
        if sentence and sentence[0].isupper():
            analysis['capitalized_sentences'] += 1
        if sentence.endswith('?'):
            analysis['questions'] += 1
        elif sentence.endswith('!'):
            analysis['exclamations'] += 1
        
    return analysis


def find_patterns(text):
    """
    Find basic patterns in text using regex.
    Args:
        text: String to search
    
    Returns:
        dict: Found patterns:
            - 'integers': List of all integers
            - 'decimals': List of all decimal numbers
            - 'words_with_digits': Words containing digits
            - 'capitalized_words': Words starting with capital letter
            - 'all_caps_words': Words in all capitals (min 2 chars)
            - 'repeated_chars': Words with repeated characters (aa, ll, etc.)
    
    Example:
        >>> text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
        >>> result = find_patterns(text)
        >>> result['integers']
        ['25']
        >>> result['decimals']
        ['3.14']
        >>> result['all_caps_words']
        ['HELLO']
        >>> result['words_with_digits']
        ['W0RLD']
    """
    
    patterns = {
        'integers': r'\b(?<!\.)\d+(?!\.)\b', # uses negative look ahead/behind to make sure its not part of a decimal
        'decimals': r'\b\d+.\d+\b',
        'words_with_digits': r'\b\w*\d\w*\b',
        'capitalized_words': r'\b[A-Z]\w*\b',
        'all_caps_words': r'\b[A-Z]{2,}\b', # only capture all caps if they are 2+ chars (so single letter words like'I' aren't grabbed)
        'repeated_chars': r'(.)\1'
    }
    
    result = {}
    for key, pattern in patterns.items():
        result[key] = re.findall(pattern, text)
    
    # remove entries that are just numbers (easier than figuring out complicated regex stuff)
    result['words_with_digits'] = [word for word in result['words_with_digits'] if not word.isdecimal()]
    
    return result


def validate_format(input_string, format_type):
    """
    Validate if input matches specified format using regex.
    
    Args:
        input_string: String to validate
        format_type: Type of format to check
    
    Returns:
        tuple: (is_valid: bool, extracted_parts: dict or None)
    
    Format types:
    - 'phone': (XXX) XXX-XXXX or XXX-XXX-XXXX
    - 'date': MM/DD/YYYY (validate month 01-12, day 01-31)
    - 'time': HH:MM AM/PM or HH:MM (24-hour)
    - 'email': basic email format (username@domain.extension)
    - 'url': http:// or https:// followed by domain
    - 'ssn': XXX-XX-XXXX (just format, not validity)
    
    For valid inputs, extract parts (area_code, month, hour, etc.)
    
    Example:
        >>> validate_format("(555) 123-4567", "phone")
        (True, {'area_code': '555', 'prefix': '123', 'line': '4567'})
        >>> validate_format("13/45/2024", "date")
        (False, None)
    """
    # Define patterns for each format type, use groups for parts
    patterns = {
        'phone': r'^\(?(\d{3})\)?[-\s](\d{3})-(\d{4})$',
        'date': r'^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/(\d{4})$',
        'time': r'^(0[1-9]|1[0-2]):([0-5][0-9])( AM| PM)?|([0-1][0-9]|2[0-3]):([0-5][0-9])$', # odd one
        'email': r'^([a-z0-9._%+-]+)@([a-z0-9.-]+)\.([a-z]+)$',
        'url': r'^https?://(?:www.)?(\w*\.[a-zA-Z]*)/?([\w/]*)?$',
        'ssn': r'^(\d{3})-(\d{2})-(\d{4})$'
    }
    extracted_parts = None

    if format_type not in patterns:
        raise ValueError("Invalid format_type specified.")

    match = re.match(patterns[format_type], input_string)
    is_valid = bool(match)

    if is_valid:
        if format_type == 'phone':
            extracted_parts = {
                'area_code': match.group(1),
                'prefix': match.group(2),
                'line': match.group(3)
            }
        elif format_type == 'date':
            extracted_parts = {
                'month': match.group(1),
                'day': match.group(2),
                'year': match.group(3)
            }
        elif format_type == 'time':
            if match.group(4): # 24-hour format
                extracted_parts = {
                    'hour': match.group(4),
                    'minute': match.group(5),
                    'period': '24-hour' 
                }
            else: # 12-hour format
                extracted_parts = {
                    'hour': match.group(1),
                    'minute': match.group(2),
                    'period': match.group(3).strip() if match.group(3) else None
                }
        elif format_type == 'email':
            extracted_parts = {
                'username': match.group(1),
                'domain': match.group(2),
                'extension': match.group(3)
            }
        elif format_type == 'url':
            extracted_parts = {
                'domain': match.group(1),
                'path': match.group(2) if match.group(2) else ''
            }
        elif format_type == 'ssn':
            extracted_parts = {
                'group1': match.group(1),
                'group2': match.group(2),
                'group3': match.group(3)
            }

    return is_valid, extracted_parts


def extract_information(text: str):
    """
    Extract specific information from unstructured text.
    
    Args:
        text: Unstructured text containing various information
    
    Returns:
        dict: Extracted information:
            - 'prices': List of prices (formats: $X.XX, $X,XXX.XX)
            - 'percentages': List of percentages (X% or X.X%)
            - 'years': List of 4-digit years (1900-2099)
            - 'sentences': List of complete sentences (end with . ! or ?)
            - 'questions': List of questions (sentences ending with ?)
            - 'quoted_text': List of text in double quotes
    
    Example:
        >>> text = 'The price is $19.99 (20% off). "Great deal!" she said.'
        >>> result = extract_information(text)
        >>> result['prices']
        ['$19.99']
        >>> result['percentages']
        ['20%']
        >>> result['quoted_text']
        ['Great deal!']
    """
    # Your code here
    patterns = {
        'prices': r'\$(?:\d{1,3},)*\d{1,3}\.\d{2}',
        'percentages': r'\d{1,2}(?:\.\d{0,2})?%', # up to 2 digits after the decimal of a percent
        'years': r'(?:19|20)[0-9][0-9]',
        'sentences': r'\w[^.!?]*[.!?]',
        'questions': r'\w[^.!?]*\?',
        'quoted_text': r'"(.*)"'
    }
    
    result = {}
    for key, pattern in patterns.items():
        result[key] = re.findall(pattern, text)
    
    return result
    


# run examples for testing
if __name__ == '__main__':
    items = ['Coffee', 'Sandwich', 'Cookie']
    prices = [3.50, 8.99, 2.00]
    quantities = [2, 1, 3]
    print(format_receipt(items, prices, quantities))
    
    raw_data = {
        'name': ' john DOE ',
        'email': ' JOHN.DOE @EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street, apt 5'
    }
    processed_data = process_user_data(raw_data)
    print("\nProcessed User Data:")
    print(processed_data)
    
    bad_raw_data = {
        'name': '  jane doe123 ', # bad: has numbers
        'email': 'jane@ invalid', # bad: incomplete domain
        'phone': '123',           # bad: only 3 numbers
        'address': '123 main st.' # this one is fine
    }
    bad_processed_data = process_user_data(bad_raw_data)
    print("\nBad Processed User Data:")
    print(bad_processed_data)
    
    text = '''Hello world! How are you?
    ... This is a test. Another line here!
    Make hello the most common word'''
    analysis_result = analyze_text(text)
    print("\nText Analysis:")
    print(analysis_result)
    
    text_patterns = "I have 25 apples and 3.14 pies. HELLO W0RLD! The quick brown fox jumps over the lazy dog. Mississippi has repeated characters."
    patterns_result = find_patterns(text_patterns)
    print("\nPattern Finding:")
    print(patterns_result)
    
    print("\nValidation Examples:")
    print(validate_format("(555) 123-4567", "phone"))
    print(validate_format("555-123-4567", "phone"))
    print(validate_format("5551234567", "phone")) # Should be False
    print(validate_format("02/29/2024", "date"))
    print(validate_format("13/45/2024", "date")) # Should be False
    print(validate_format("10:30 AM", "time"))
    print(validate_format("22:15", "time"))
    print(validate_format("john.doe@example.com", "email"))
    print(validate_format("invalid-email", "email")) # Should be False
    print(validate_format("https://www.example.com/path/to/page", "url"))
    print(validate_format("http://example.com", "url"))
    print(validate_format("ftp://example.com", "url")) # Should be False
    print(validate_format("123-45-6789", "ssn"))
    print(validate_format("123456789", "ssn")) # Should be False
    
    infomercial_text = """This amazing product can be yours for just $19.99! That's 50% off the regular price.
But wait, there's more! If you order before 12/31/2024, we'll include a second one FREE.
Call now at (800) 123-4567. "Don't miss out!" exclaimed a happy customer.
Visit our website at https://www.buynow.com for details. This offer expires 01/15/2025.
Are you ready to change your life? Yes!
"""
    extracted_info = extract_information(infomercial_text)
    print("\nExtracted Information:")
    print(extracted_info)