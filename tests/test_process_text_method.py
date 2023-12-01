import pytest
from src.source import process_text


@pytest.fixture
def nltk_words_mock(monkeypatch):
    fake_nltk_words = set(["one", "two", "three", "four", "five", "and"])
    monkeypatch.setattr("src.source.nltk_words", fake_nltk_words)

def test_process_text_with_numbers(nltk_words_mock):
    text = "one convert 1 123 and 2 45.67 3 four to words 5"
    result = process_text(text)
    expected_result = "one one and two three four five"
    assert result == expected_result

def test_process_text_without_numbers():
    text = "this buuuuuugwoooord is a sample text without numbers"
    result = process_text(text)
    assert result == "this is a sample text without number"


def test_process_text_with_nltk_words_filtering(nltk_words_mock):
    text = "one two three four five"
    result = process_text(text)
    expected_result = "one two three four five"
    assert result == expected_result
