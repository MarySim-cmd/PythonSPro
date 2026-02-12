import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# 1. ТЕСТЫ capitalize
def test_capitalize_positive():
    """Позитивные тесты для capitalize"""
    assert string_utils.capitalize("Тест") == "Тест"
    assert string_utils.capitalize("123") == "123"
    assert string_utils.capitalize("04 апреля 2025") == "04 апреля 2025"
    assert string_utils.capitalize("skypro") == "Skypro"


def test_capitalize_negative():
    """Негативные тесты для capitalize"""
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize(" ") == " "

    with pytest.raises((AttributeError, TypeError)):
        string_utils.capitalize(None)
    with pytest.raises((AttributeError, TypeError)):
        string_utils.capitalize([])


# 2. ТЕСТЫ trim
def test_trim_positive():
    """Позитивные тесты для trim"""
    assert string_utils.trim("   Тест") == "Тест"
    assert string_utils.trim("   123") == "123"
    assert string_utils.trim("   04 апреля 2025") == "04 апреля 2025"
    assert string_utils.trim("   skypro") == "skypro"


def test_trim_negative():
    """Негативные тесты для trim"""
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == ""
    assert string_utils.trim("   ") == ""

    with pytest.raises((AttributeError, TypeError)):
        string_utils.trim(None)
    with pytest.raises((AttributeError, TypeError)):
        string_utils.trim([])


# 3. ТЕСТЫ contains
def test_contains_positive():
    """Позитивные тесты для contains"""
    # True случаи
    assert string_utils.contains("Тест", "Т") is True
    assert string_utils.contains("123", "2") is True
    assert string_utils.contains("04 апреля 2025", "апреля") is True
    assert string_utils.contains("SkyPro", "S") is True
    # False случаи
    assert string_utils.contains("Тест", "X") is False
    assert string_utils.contains("123", "5") is False
    assert string_utils.contains("04 апреля 2025", "мая") is False


def test_contains_negative():
    """Негативные тесты для contains"""
    assert string_utils.contains("", "") is True
    assert string_utils.contains("test", "") is True
    assert string_utils.contains("", "a") is False
    assert string_utils.contains(" ", " ") is True

    with pytest.raises((TypeError, AttributeError)):
        string_utils.contains(None, "a")
    with pytest.raises((TypeError, AttributeError)):
        string_utils.contains("test", None)


# 4. ТЕСТЫ delete_symbol
def test_delete_symbol_positive():
    """Позитивные тесты для delete_symbol"""
    assert string_utils.delete_symbol("Тест", "Т") == "ест"
    assert string_utils.delete_symbol("123", "2") == "13"
    assert string_utils.delete_symbol("04 апреля 2025", "апреля") == "04  2025"
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_negative():
    """Негативные тесты для delete_symbol"""
    assert string_utils.delete_symbol("", "") == ""
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol("test", "") == "test"
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"
    assert string_utils.delete_symbol(" ", " ") == ""

    with pytest.raises((TypeError, AttributeError)):
        string_utils.delete_symbol(None, "a")
    with pytest.raises((TypeError, AttributeError)):
        string_utils.delete_symbol("test", None)