def is_palindrome(s):
    clean_str = ''.join(filter(str.isalnum, s.lower()))
    return clean_str == clean_str[::-1]