import pytest
from src.source import calculate_sample_stats

@pytest.mark.parametrize("sample, expected_result", [
    ("Hello world! Hello world! Hello world!", (38, 9, 35, 3)),
    ("", (0, 0, 0, 0)),

])
def test_stats_calculation(sample, expected_result):
    result = calculate_sample_stats(sample)
    assert result == expected_result