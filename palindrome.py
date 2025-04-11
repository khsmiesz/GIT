#zadanie_palindrom

def is_it_palindrom(word):
    """
    Checks if argument is a palindrome by comparing letters in a word forward and backwards
    There is 1 string argument
    Return is True if the word is palindrome, False if not
    """
    forw=[]
    backw=[]
    for letter in word:
        forw += letter 
        backw=forw[::-1]
    return print(bool(backw==forw))
is_it_palindrom("baba")
is_it_palindrom("kajak")
is_it_palindrom("mamona")



