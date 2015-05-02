small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """

    lst_of_words = title.split()
    new_title = ""

    for index, word in enumerate(lst_of_words):
        if index == 0 :
            new_title += " " + word.title()
        elif word.lower() in small_words:
            new_title += " " + word.lower()
        else:
            new_title += " " + word.title()

    return new_title.strip()

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()

print(book_title('the WORKS OF AleXANDer dumas'))

