def is_palindrome(input_str):
    clean_str = ''.join(filter(str.isalnum, input_str.lower()))
    return clean_str == clean_str[::-1]