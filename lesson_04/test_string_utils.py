import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ======================== capitalize ========================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_str", [
    ("test", "Test"),              # простой тест
    ("hello world", "Hello world"),  # строка с пробелом
    ("Тест", "Тест"),              # слово на кириллице с заглавной буквы
    ("123", "123"),                # цифры
    ("просто текст для теста", "Просто текст для теста"),  # строка с пробелами на кириллице
    ("Test", "Test"),          # слово на латинице с заглавной буквы
    (" test", " test"),        # строка с побелом в начале
])
def test_capitalize_positive(input_str, expected_str):
    assert string_utils.capitalize(input_str) == expected_str


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_str", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected_str):
    assert string_utils.capitalize(input_str) == expected_str


# =========================== trim ===========================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected_str", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),           # без пробелов
    ("     ", ""),                  # только пробелы → пустая строка
    ("  Тест", "Тест"),
    (" Текст с кучей пробелов между словами", "Текст с кучей пробелов между словами"),
])
def test_trim_positive(input_str, expected_str):
    assert string_utils.trim(input_str) == expected_str


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_str", [
    ("", ""),                       # пустая строка
    ("skypro ", "skypro "),         # пробел в конце
    ("sky pro", "sky pro"),         # с пробелом между словами
])
def test_trim_negative(input_str, expected_str):
    assert string_utils.trim(input_str) == expected_str


# ========================= contains =========================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("SkyPro", "y", True),
    ("Тест", "е", True),
    ("123", "2", True),
    ("04 апреля 2023", " ", True),  # пробел как символ
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "sky", False),       # в другом регистре
    ("", "a", False),               # пустая строка
    ("   ", "a", False),
    ("123", "a", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) is expected


# ======================= delete_symbol =======================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected_str", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),       # подстрока
    ("Тест", "е", "Тст"),
    ("Тест с пробелами", " ", "Тестспробелами"),
    ("aaa", "a", ""),               # удаление всех вхождений
    ("SkyPro", "U", "SkyPro"),      # символа нет — строка не меняется
])
def test_delete_symbol_positive(string, symbol, expected_str):
    assert string_utils.delete_symbol(string, symbol) == expected_str


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected_str", [
    ("", "a", ""),                  # пустая строка
    ("   ", " ", ""),               # строка из пробелов
    ("123", "4", "123"),
])
def test_delete_symbol_negative(string, symbol, expected_str):
    assert string_utils.delete_symbol(string, symbol) == expected_str
