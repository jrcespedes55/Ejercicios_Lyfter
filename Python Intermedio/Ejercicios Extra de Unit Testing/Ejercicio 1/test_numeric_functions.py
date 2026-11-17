import pytest

from numeric_functions import (
    sum_numbers,
    calculate_average,
    convert_temperature
)


class TestNumericFunctions:

    # ---- Tests para sum_numbers ----

    def test_sum_numbers_positive(self):
        assert sum_numbers(5, 10, 15, 20) == 50

    def test_sum_numbers_negative(self):
        assert sum_numbers(-5, -10, -15) == -30

    def test_sum_numbers_zeros(self):
        assert sum_numbers(0, 0, 0, 0) == 0


    # ---- Tests para calculate_average ----

    def test_calculate_average_positive(self):
        assert calculate_average(10, 20, 30, 40) == 25

    def test_calculate_average_negative(self):
        assert calculate_average(-5, -10, -15) == -10

    def test_calculate_average_zeros(self):
        assert calculate_average(0, 0, 0) == 0

    def test_calculate_average_without_arguments(self):
        with pytest.raises(ValueError):
            calculate_average()


    # ---- Tests para convert_temperature ----

    def test_convert_temperature_positive(self):
        assert convert_temperature(25, "C") == 77

        assert convert_temperature(100, "F") == pytest.approx(37.7777777778)

    def test_convert_temperature_negative(self):
        assert convert_temperature(-10, "C") == 14

        assert convert_temperature(-4, "F") == -20

    def test_convert_temperature_zero(self):
        assert convert_temperature(0, "C") == 32

        assert convert_temperature(0, "F") == pytest.approx(-17.7777777778)

    def test_convert_temperature_invalid_unit(self):
        with pytest.raises(ValueError):
            convert_temperature(25, "K")