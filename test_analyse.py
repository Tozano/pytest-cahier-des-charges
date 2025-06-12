import pytest
from analyse import moyenne, regression_lineaire

def test_moyenne_valide():
    assert moyenne([1, 2, 3]) == pytest.approx(2.0)

def test_moyenne_vide():
    with pytest.raises(ValueError):
        moyenne([])

@pytest.mark.parametrize("x, y, a_attendu, b_attendu", [
    ([0, 1, 2], [0, 2, 4], 2.0, 0.0),
    ([1, 2, 3], [2, 2, 2], 0.0, 2.0),
])
def test_regression_valide(x, y, a_attendu, b_attendu):
    a, b = regression_lineaire(x, y)
    assert round(a, 3) == a_attendu
    assert round(b, 3) == b_attendu

def test_regression_erreurs():
    with pytest.raises(ValueError):
        regression_lineaire([], [])
    with pytest.raises(ValueError):
        regression_lineaire([1,1,1], [2,2,2])