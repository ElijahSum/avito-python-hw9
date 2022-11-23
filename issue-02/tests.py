from morse import decode
import pytest


@pytest.mark.parametrize('morse_message, result',
                         [
                             ('... --- ...', 'SOS'),
                             ('.... . .-.. .-.. ---', 'HELLO'),
                             ('.--. -.-- - .... --- -.', 'PYTHON')
                         ])
def test_decode(morse_message, result):
    assert decode(morse_message) == result


if __name__ == '__main__':
    print(decode('... --- ...'))
