import sys


def main():
    morse_code = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
        'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ',
        '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. ', ' ': '/ '
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        input_string = sys.argv[1]

        allowed_chars = set(morse_code.keys()) | set(
            " abcdefghijklmnopqrstuvwxyz")

        chars_check = (char in allowed_chars for char in input_string)
        assert all(chars_check), "the arguments are bad"

        morse_result = ""
        for char in input_string.upper():
            morse_result += morse_code[char]

        print(morse_result.rstrip())

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
