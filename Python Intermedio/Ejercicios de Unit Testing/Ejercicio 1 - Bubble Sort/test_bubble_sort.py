import pytest
from bubble_sort import bubble_sort

def test_bubble_sort_small_list():
    my_list = [6, 4, 1]

    bubble_sort(my_list)

    assert my_list == [1, 4, 6]

def test_bubble_sort_large_list():
    my_list = list(range(150, 0, -1))

    bubble_sort(my_list)

    assert my_list == list(range(1, 151))

def test_bubble_sort_empty_list():
    my_list = []

    bubble_sort(my_list)

    assert my_list == []

def test_bubble_sort_invalid_parameter():
    my_list = 123

    with pytest.raises(TypeError):
        bubble_sort(my_list)