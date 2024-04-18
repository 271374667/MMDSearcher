class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


def color_text(text, foreground_color, background_color):
    return f"{foreground_color}{background_color}{text}{Color.END}"


def main():
    text = "Hello World"
    foreground_color = Color.BLUE
    background_color = Color.GREEN
    colored_text = color_text(text, foreground_color, background_color)
    print(f'{colored_text!r}')


if __name__ == "__main__":
    main()
