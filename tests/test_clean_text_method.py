import pytest
from src.source import clean_text


@pytest.fixture
def test_basic_cleaning():
    sample = "This is a sample text with some punctuations! And, a link: http://example.com"
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == "this is a sample text with some punctuations and a link"

def test_empty_input():
    sample = ""
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == ""

def test_url_removal():
    sample = "Check out this link: http://example.com"
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == "check out this link"

def test_special_characters():
    sample = "Special characters !@#$%^&*()_+{}[]|;:,.<>?/`~"
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == "special characters"

def test_mixed_case():
    sample = "MiXeD CaSe TeXT"
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == "mixed case text"

def test_non_alphanumeric_chars():
    sample = "123!@#456"
    cleaned_sample = clean_text(sample)
    assert cleaned_sample == "123456"