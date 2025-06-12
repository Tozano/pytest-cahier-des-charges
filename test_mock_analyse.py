import analyse

def test_appel_regression_lineaire(mocker):
    # Valeur simulée
    fake_a, fake_b = 3.14, 1.59
    # On stub la fonction
    mock_reg = mocker.patch('analyse.regression_lineaire', return_value=(fake_a, fake_b))
    # Appel
    x = [1, 2, 3]
    y = [2, 4, 6]
    a, b = analyse.regression_lineaire(x, y)
    # Vérifications
    mock_reg.assert_called_once_with(x, y)
    assert a == fake_a
    assert b == fake_b