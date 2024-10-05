# Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios
#  de semana 6 (exceptuando el 1 y 2).

import pytest
import HW_tests_ww6 as ww6


# Unit Test prime numbers.
def test_returns_prime_numbers_from_given_list():
    # Arrange:
    numbers_list = [1, 2, 4, 6, 7, 13, 9, 67, 87, 37, 47, 97, 21]
    # Act:
    result = ww6.prime_number(numbers_list)
    # Assert:
    assert result == [2, 7, 13, 67, 37, 47, 97]


# Unit Test Str separado por guiones.
def test_returns_string_words_sorted_alphabetically_from_given_str():
    # Arrange:
    string_to_sort = 'esto-es-un-string-de-palabras-separdas-por-guiones'
    # Act:
    result = ww6.order_str(string_to_sort)
    # Assert:
    assert result == 'de-es-esto-guiones-palabras-por-separdas-string-un'


# Unit Test cuenta mayúsculas y minúsculas de un string.
def test_returns_amount_of_upper_and_lower_case_letters():
    # Arrange:
    string_to_count = 'Funcion que CUENTa maYUsculas y MINUSCULas'
    # Act:
    result = ww6.count_upper_lower_cases(string_to_count)
    # Assert:
    assert result == ('Upper = 16. Lower = 21')


# Unit Test probar que falla si recibe integer.
def test_returns_error_receiving_int_instead_of_letters():
    # Arrange:
    string_to_count = 54878734
    # Act Assert:
    with pytest.raises(TypeError):
        ww6.count_upper_lower_cases(string_to_count)
