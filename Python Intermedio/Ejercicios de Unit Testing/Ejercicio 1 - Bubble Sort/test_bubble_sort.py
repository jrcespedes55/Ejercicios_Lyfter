import pytest
from bubble_sort import bubble_sort


# ---- Tests para bubble_sort ----

def test_bubble_sort_small_list():
    my_list = [8, 6, 4, 7, 1]

    bubble_sort(my_list)

    assert my_list == [1, 4, 6, 7, 8]


def test_bubble_sort_large_list():
    my_list = list(range(150, 0, -1))

    bubble_sort(my_list)

    assert my_list == list(range(1, 151))


def test_bubble_sort_large_random_list_with_duplicates():
    my_list = [
        45, 12, 89, 3, 45, 67, 12, 99, 1, 34,
        56, 78, 3, 90, 23, 45, 67, 12, 8, 100,
        34, 56, 78, 2, 99, 1, 45, 67, 89, 3,
        15, 28, 42, 56, 78, 90, 12, 34, 67, 8,
        19, 23, 45, 89, 100, 2, 3, 56, 78, 12,
        91, 4, 37, 62, 18, 73, 29, 85, 11, 46,
        54, 7, 96, 32, 68, 14, 81, 25, 59, 40,
        5, 93, 21, 76, 38, 64, 17, 87, 30, 52,
        9, 98, 26, 71, 43, 60, 13, 84, 35, 50,
        6, 95, 22, 75, 39, 63, 16, 86, 31, 53,
        10, 97, 27, 72, 44, 61, 20, 82, 36, 49,
        24, 70, 41, 88, 33, 58, 94, 47, 66, 79
    ]

    expected_result = sorted(my_list)

    bubble_sort(my_list)

    assert my_list == expected_result


def test_bubble_sort_empty_list():
    my_list = []

    bubble_sort(my_list)

    assert my_list == []


@pytest.mark.parametrize("my_list", [
    "Hola mundo",
    {"name": "Python"},
    None
])
def test_bubble_sort_invalid_parameter(my_list):

    with pytest.raises(TypeError):
        bubble_sort(my_list)