from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе
    >>> encode('HELLO')
    '.... . .-.. .-.. ---'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('hello') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    KeyError: ...
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]
    return ' '.join(encoded_signs)


if __name__ == '__main__':
    print(encode('hello'))
