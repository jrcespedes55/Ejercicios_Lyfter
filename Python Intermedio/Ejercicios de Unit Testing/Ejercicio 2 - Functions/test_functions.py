from functions import string_backwards, list_sum, count_case_letters


# ---- Tests para string_backwards ----

def test_string_backwards_1():
    assert string_backwards("Hola") == "aloH"


def test_string_backwards_2():
    assert string_backwards("Pizza con piña") == "añip noc azziP"


def test_string_backwards_3():
    assert string_backwards("AnitalavalatinA") == "AnitalavalatinA"


# ---- Tests para list_sum ----

def test_list_sum_1():
    assert list_sum([4, 6, 2, 29]) == 41


def test_list_sum_2():
    assert list_sum([10, 20, 30, 40, 50]) == 150


def test_list_sum_3():
    assert list_sum([-5, 10, -3, 8]) == 10


# ---- Tests para count_case_letters ----

def test_count_case_letters_1():
    assert count_case_letters("Hola Mundo") == (2, 7)


def test_count_case_letters_2():
    assert count_case_letters("PYTHON") == (6, 0)


def test_count_case_letters_3():
    assert count_case_letters("hola mundo") == (0, 9)