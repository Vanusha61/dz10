import requests
from collections import Counter
import re

def get_text(url):
    response = requests.get(url)
    return response.text

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # читаем слова из файла
    with open(words_file) as file:
        words_to_count = [line.strip() for line in file if line.strip()]

    # один запрос к сайту
    text = get_text(url)

    # токенизация текста
    words = re.findall(r'\b\w+\b', text.lower())

    # считаем частоты
    word_counts = Counter(words)

    # формируем результат
    frequencies = {word: word_counts.get(word.lower(), 0) for word in words_to_count}

    print(frequencies)

if __name__ == "__main__":
    main()