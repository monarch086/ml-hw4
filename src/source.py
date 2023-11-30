from num2words import num2words
import re
import string
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import nltk

nltk_words = set(words.words())


def clean_text(sample):
    sample = re.sub(f"[{string.punctuation}]", '', sample)
    sample = re.sub(r'http\S+', '', sample)
    sample = re.sub(r'[^a-zA-Z0-9\n]', ' ', sample)
    sample_words = sample.split()
    sample_words = [word.lower() for word in sample_words if word in nltk_words]
    sample = ' '.join(sample_words)
    return sample


def process_text(text):
    words = text.split()
    processed_words = []
    for word in words:
        try:
            processed_word = int(float(word)) if word.replace(".", "").replace(",", "").isdigit() else word
            processed_word = num2words(word) if word.isnumeric() else word
            processed_words.append(processed_word)
        except Exception as e:
            processed_words.append(word)
    tokens = word_tokenize(' '.join(processed_words))
    return ' '.join(tokens)


def calculate_sample_stats(sample):
    num_chars = len(sample)
    words = nltk.word_tokenize(sample)
    num_words = len(words)
    num_symbols = len([char for char in sample if char.isalnum() or char.isspace()])
    num_capital_letters = sum(1 for char in sample if char.isupper())

    return num_chars, num_words, num_symbols, num_capital_letters