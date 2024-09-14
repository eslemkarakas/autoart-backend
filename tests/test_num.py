import polars as pl
from info.cases.num import get_basic_stats  # Replace 'your_module' with the actual module name

def test_get_basic_stats():
    # Create a sample Polars series
    series = pl.Series([1, 2, 3, 4, 5])

    # Expected values
    expected_stats = {
        'min': 1,
        'max': 5,
        'std': series.std(),
        'mean': 3.0,
        'median': 3.0
    }

    # Call the function
    result = get_basic_stats(series)

    # Assert that the result matches the expected values
    assert result['min'] == expected_stats['min'], f"Expected min {expected_stats['min']}, got {result['min']}"
    assert result['max'] == expected_stats['max'], f"Expected max {expected_stats['max']}, got {result['max']}"
    assert result['std'] == expected_stats['std'], f"Expected std {expected_stats['std']}, got {result['std']}"
    assert result['mean'] == expected_stats['mean'], f"Expected mean {expected_stats['mean']}, got {result['mean']}"
    assert result['median'] == expected_stats['median'], f"Expected median {expected_stats['median']}, got {result['median']}"