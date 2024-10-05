import pytest
from HW_Bubble_sort import inverse_bubble_sort

# 1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:



#     1. Funciona con una lista pequeña.
def test_bubble_sort_passes_with_short_list():
    # Arrange:
    test_list = [0, 32,-11, 7, -6]
    # Act:
    result = inverse_bubble_sort(test_list)
    # Assert:
    assert result == [-11, -6, 0, 7, 32]


#     2. Funciona con una lista grande (de más de 100 elementos).
def test_bubble_sort_passes_with_large_list():
    # Arrange:
    test_list = [105, 104, 103, 102, 101, 100, 99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,-55,54,53,52,51,50,49,48,47,46,45,44,-43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,-26,25,-24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,-5,4,3,2,1,0,-1]
    # Act:
    result = inverse_bubble_sort(test_list)
    # Assert:
    assert result == [-55, -43, -26, -24, -5, -1, 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]


#     3. Funciona con una lista vacía.
def test_bubble_sort_passes_with_empty_list():
    # Arrange:
    test_list = []
    # Act:
    result = inverse_bubble_sort(test_list)
    # Assert:
    assert result == None


#     4. No funciona con parámetros que no sean una lista.
def test_bubble_sort_returns_error_with_str():
    # Arrange:
    test_list = "I'm not a list"
    # Act Assert:
    with pytest.raises(TypeError):
        inverse_bubble_sort(test_list)

