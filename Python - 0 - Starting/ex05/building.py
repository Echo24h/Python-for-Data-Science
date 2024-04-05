import sys


def count_chars(text) -> dict:
    """
    Cette fonction compte les caractères dans une chaîne de texte donnée.

    Args:
        text (str): La chaîne de texte à analyser.

    Returns:
        dict: Un dictionnaire contenant le nombre de caractères majuscules,
        minuscules, de ponctuation, de chiffres et d'espaces.
    """
    dict = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }

    for char in text:
        if char.isupper():
            dict["upper"] += 1
        elif char.islower():
            dict["lower"] += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            dict["punctuation"] += 1
        elif char.isspace():
            dict["spaces"] += 1
        elif char.isdigit():
            dict["digits"] += 1

    return dict


def main():

    """
    Cette fonction est le point d'entrée du programme.

    Elle compte les caractères par type dans une chaîne de texte donnée
    et affiche le résultat.

    Args:
        None

    Returns:
        None
    """

    try:
        if len(sys.argv) == 1 or sys.argv[1] == "None":

            try:
                text = input("Please provide a string: \n")
            except KeyboardInterrupt:
                sys.exit(0)

        elif len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided")
        else:
            text = sys.argv[1]

        dict = count_chars(text)
        total_chars = sum(dict.values())
        print(f"The text contains {total_chars} characters:")
        print(str(dict["upper"]) + " upper letters")
        print(str(dict["lower"]) + " lower letters")
        print(str(dict["punctuation"]) + " punctuation marks")
        print(str(dict["spaces"]) + " spaces")
        print(str(dict["digits"]) + " digits")

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
