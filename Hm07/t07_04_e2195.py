import sys
import re

def solve():
    first_line = sys.stdin.readline().split()
    if not first_line:
        return
    n, m = map(int, first_line)

    vocabulary = set()
    for _ in range(n):
        word = sys.stdin.readline().strip().lower()
        if word:
            vocabulary.add(word)

    text_lines = []
    for _ in range(m):
        text_lines.append(sys.stdin.readline())

    text_content = " ".join(text_lines)

    clean_text = re.sub(r'[.,:;\-\'\"!?]', ' ', text_content)
    words_in_text = clean_text.lower().split()

    used_words = set(words_in_text)

    if not used_words.issubset(vocabulary):
        print("Some words from the text are unknown.")
    elif not vocabulary.issubset(used_words):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == '__main__':
    solve()