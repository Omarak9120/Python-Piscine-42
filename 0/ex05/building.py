import sys


def info_text(text: str) -> dict:
    punctuations = ".,!?;:'\"()-[]}{<>@#$%^&*/\\|_=+"

    return {
        "upper": sum(1 for char in text if 'A' <= char <= 'Z'),
        "lower": sum(1 for char in text if 'a' <= char <= 'z'),
        "punctuation": sum(1 for char in text if char in punctuations),
        "spaces": sum(1 for char in text if char == ' ' or char == '\n'),
        "digits": sum(1 for char in text if '0' <= char <= '9')
    }


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one arg")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("text to count?\n")

        stats = info_text(text)

        print(f"The text contains {len(text)} characters:")
        print(f"{stats['upper']} upper letters")
        print(f"{stats['lower']} lower letters")
        print(f"{stats['punctuation']} punctuation marks")
        print(f"{stats['spaces']} spaces")
        print(f"{stats['digits']} digits")

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
