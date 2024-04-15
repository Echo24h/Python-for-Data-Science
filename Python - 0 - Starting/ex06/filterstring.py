import sys
from ft_filter import ft_filter


def filter_words_by_length(S, N) -> list:
    """
    Filter words in a string by length.

    Args:
        S: A string.
        N: An integer.

    Returns:
        A list of words that have a length greater than N.
    """
    return ft_filter(lambda word: len(word) > N, S.split())


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"
        print(filter_words_by_length(sys.argv[1], int(sys.argv[2])))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        sys.exit(1)
