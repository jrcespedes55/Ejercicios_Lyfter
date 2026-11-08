from functions import (string_backwards, list_sum, count_case_letters, sort_words_alphabetically, get_prime_numbers)


# ---- Tests para string_backwards ----

def test_string_backwards_basic():
    assert string_backwards("Hola") == "aloH"


def test_string_backwards_with_spaces():
    assert string_backwards("Pizza con piña") == "añip noc azziP"


def test_string_backwards_with_numbers():
    assert string_backwards("Python 123") == "321 nohtyP"


# ---- Tests para list_sum ----

def test_list_sum_basic():
    assert list_sum([4, 6, 2, 29]) == 41


def test_list_sum_with_multiple_numbers():
    assert list_sum([10, 20, 30, 40, 50]) == 150


def test_list_sum_with_negative_numbers():
    assert list_sum([-5, 10, -3, 8]) == 10


# ---- Tests para count_case_letters ----

def test_count_case_letters_mixed():
    assert count_case_letters("Hola Mundo") == (2, 7)


def test_count_case_letters_uppercase():
    assert count_case_letters("PYTHON") == (6, 0)


def test_count_case_letters_lowercase():
    assert count_case_letters("hola mundo") == (0, 9)


# ---- Tests para sort_words_alphabetically ----

def test_sort_words_alphabetically_basic():
    assert sort_words_alphabetically(
        "python-variable-funcion"
    ) == "funcion-python-variable"


def test_sort_words_alphabetically_different_words():
    assert sort_words_alphabetically(
        "zoey-yesenia-xinia-alba"
    ) == "alba-xinia-yesenia-zoey"


def test_sort_words_alphabetically_another_order():
    assert sort_words_alphabetically(
        "monitor-computadora-python"
    ) == "computadora-monitor-python"


# ---- Tests para get_prime_numbers ----

def test_get_prime_numbers_basic():
    assert get_prime_numbers(
        [1, 4, 6, 7, 13, 9, 67]
    ) == [7, 13, 67]


def test_get_prime_numbers_all_primes():
    assert get_prime_numbers(
        [2, 3, 5, 7, 11]
    ) == [2, 3, 5, 7, 11]


def test_get_prime_numbers_no_primes():
    assert get_prime_numbers(
        [1, 4, 6, 8, 9, 10]
    ) == []