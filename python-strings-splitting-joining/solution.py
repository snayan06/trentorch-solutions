def word_count(text: str) -> int:
    """
    Return the number of words in `text`, where words are
    separated by any run of whitespace. Leading and trailing
    whitespace does not create extra words.
    """
    return len(text.split())


def reverse_word_order(text: str) -> str:
    """
    Split `text` on whitespace, reverse the order of the words
    (a list can be sliced with [::-1] like a string), and
    return them joined by single spaces.

    Example: reverse_word_order("  one  two three ") -> "three two one"
    """
    words = text.split()[::-1]
    return " ".join(words)


def last_field(line: str, sep: str) -> str:
    """
    Return the text after the LAST occurrence of `sep` in
    `line`. If `sep` does not occur, return `line` unchanged.
    Use rsplit() with a maxsplit of 1 and the index -1.

    Example: last_field("a/b/c.txt", "/") -> "c.txt"
    """
    words = line.rsplit(sep,1)
    return words[-1]

def count_nonblank_lines(text: str) -> int:
    """
    Return how many lines in `text` (as split by splitlines())
    contain at least one character that is not whitespace.
    """
    ans = 0
    for line in text.splitlines():
        if line.strip()!= "":
            ans+=1
    return ans



def make_csv_line(fields) -> str:
    """
    `fields` is a list of strings. Return one string in which
    the fields are joined by ",". Any field that contains a
    comma is first wrapped in double quotes.

    Example: make_csv_line(["a", "b,c", "d"]) -> 'a,"b,c",d'
    """
    processed = []
    for item in fields:
        if "," in item:
            value = '"' + item + '"'
            processed.append(value)
        else:
            processed.append(item)

    return ",".join(processed)
