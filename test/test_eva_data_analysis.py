import pytest
import eva_data_analysis as eva

def test_text_to_duration_float():
    """
    Testing
    """
    assert eva.text_to_duration("10:20") == pytest.approx(10.3333333)

def test_text_to_duration_integer():
    """
    Testing
    """
    assert eva.text_to_duration("10:00") == 10

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
    ("Judith Resnik; Sally Ride;Buzz Aldrin;", 3),
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = eva.calculate_crew_size(input_value)
    assert actual_result == expected_result


