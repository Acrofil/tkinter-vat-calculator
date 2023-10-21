from project import calculate_vat_included, calculate_vat_excluded
import pytest

def test_calculate_vat_included_right_output():
    result = calculate_vat_included(100, 20)
    
    assert result[0] == 83.33
    assert result[1] == 16.67
    
def test_calculate_vat_included_wrong_output():
    result = calculate_vat_included(100, 20)
    
    assert result[0] == 83.3
    assert result[1] == 16.53


def test_calculate_vat_excluded_right_output():
    result = calculate_vat_excluded(100, 20)
    
    assert result[0] == 120
    assert result[1] == 20
    
def test_calculate_vat_excluded_wrong_output():
    result = calculate_vat_excluded(100, 20)
    
    assert result[0] == 110
    assert result[1] == 20