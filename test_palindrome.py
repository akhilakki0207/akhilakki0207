# test_palindrome.py

from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
