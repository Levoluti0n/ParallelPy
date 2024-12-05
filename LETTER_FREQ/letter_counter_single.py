import time
import json
import urllib.request


def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    for l in text:
        letter = l.lower()
        if letter.isalpha():
            frequency[letter] = frequency.get(letter, 0) + 1


def main():
    frequency = {}

    start = time.time()
    for i in range(1000, 1020):
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = time.time()

    print(json.dumps(frequency, indent=4))
    print(f"Done in {end-start:.4f}")


main()
