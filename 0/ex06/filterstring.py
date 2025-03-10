import sys
from ft_filter import ft_filter


def main():
    """
    Should wirte 2 arg
    string nad integer

    Returns a list of words that are longer than the integer.
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        string_arg = sys.argv[1]
        int_arg = sys.argv[2]

        assert int_arg.isdigit(), "the arguments are bad"

        min_length = int(int_arg)

        assert isinstance(string_arg, str), "the arguments are bad"
        words = string_arg.split()

        filtered_words = list(
            ft_filter(lambda word: len(word) > min_length, words)
        )
        print(filtered_words)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
