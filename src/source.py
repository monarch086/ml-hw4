"""Module providing a functions for text processing"""
import re
import string
from num2words import num2words
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk_words = set(words.words())

def clean_text(sample):
    """
    Cleans and normalizes the input text.

    This function performs several operations to clean and normalize the input text:
    1. Removes punctuation using a translation table.
    2. Removes any remaining punctuation using regular expressions.
    3. Removes URLs that start with 'http' using regular expressions.
    4. Replaces non-alphanumeric characters with spaces, preserving digits and letters.
    5. Splits the text into words, converts each word to lowercase, and then rejoins
       them into a single string.

    Parameters:
    sample (str): A string representing the text to be cleaned.

    Returns:
    str: The cleaned and normalized text.
    """
    sample = sample.translate(str.maketrans('', '', string.punctuation))
    sample = re.sub(f"[{string.punctuation}]", '', sample)
    sample = re.sub(r'http\S+', '', sample)
    sample = re.sub(r'[^a-zA-Z0-9\n]', ' ', sample)
    sample_words = sample.split()
    sample_words = [word.lower() for word in sample_words]
    sample = ' '.join(sample_words)
    return sample

def lemmatize_text(text):
    """
    Converts the input text into its lemmatized form.

    This function tokenizes the input text into words and then applies lemmatization 
    to each word. Lemmatization is the process of reducing words to their base or root form. 
    For example, the word 'running' would be lemmatized to 'run'.

    Parameters:
    text (str): A string representing the text to be lemmatized.

    Returns:
    str: The lemmatized text where each word has been reduced to its base form.
    """
    lemmatizer = WordNetLemmatizer()
    tokenized_words = word_tokenize(str(text))
    lemmatized_text = ' '.join(lemmatizer.lemmatize(word) for word in tokenized_words)
    return lemmatized_text

def _convert_to_int_if_numeric(word):
    try:
        return int(float(word))
    except ValueError:
        return word

def process_text(text):
    """
    Processes the input text by lemmatizing, filtering, and tokenizing.

    This function performs several steps to process the input text:
    1. Lemmatizes the text to convert words to their base form.
    2. Splits the lemmatized text into words.
    3. Converts numbers to words (if applicable) and filters out words not in a predefined set 
       (nltk_words_set).
    4. Tokenizes the resulting text into individual words and rejoins them into a single string.

    Parameters:
    text (str): A string representing the text to be processed.

    Returns:
    str: The processed text as a string, with lemmatization, number conversion, filtering, and 
    tokenization applied.
    """
    lemmatized_text = lemmatize_text(text)
    lemmatized_words = lemmatized_text.split()
    processed_words = []

    for word in lemmatized_words:
        try:
            processed_word = _convert_to_int_if_numeric(word)
            processed_word = num2words(word) if word.isnumeric() else word
            processed_words.append(processed_word)
        except Exception:
            processed_words.append(word)

    processed_words = [word for word in processed_words if word in nltk_words]
    tokens = word_tokenize(' '.join(processed_words))
    return ' '.join(tokens)

def calculate_sample_stats(sample):
    """
    Calculates sample statistics.

    Parameters:
    sample (str): The sample text for which to calculate statistics.

    Returns:
    tuple: A tuple containing the number of characters, words, symbols, and capital letters 
    in the sample.
    """
    num_chars = len(sample)
    tokenized_words = nltk.word_tokenize(sample)
    num_words = len(tokenized_words)
    num_symbols = len([char for char in sample if char.isalnum() or char.isspace()])
    num_capital_letters = sum(1 for char in sample if char.isupper())

    return num_chars, num_words, num_symbols, num_capital_letters
