from blackjack import calculate_score


def test_calculate_score():
    """Test the calculate score function"""
    assert calculate_score(['2', '3', '4']) is 9
    assert calculate_score(['A', 'A', '4']) is 16
    assert calculate_score(['J', '2', 'A']) is 13
    assert calculate_score(['4', 'A', 'A']) is 16


test_calculate_score()