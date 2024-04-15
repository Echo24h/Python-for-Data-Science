import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def morse_encode(text: str) -> str:
    """
    Encode a string of text to Morse code.

    Args:
        text: A string of text.

    Returns:
        A string of Morse code.
    """
    string = ""
    for char in text:
        if char.upper() in NESTED_MORSE:
            string += NESTED_MORSE[char.upper()]
        else:
            raise AssertionError("the argument are bad")
    if len(string) > 0:
        string = string[:-1]
    return string


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        print(morse_encode(sys.argv[1]))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        sys.exit(1)
