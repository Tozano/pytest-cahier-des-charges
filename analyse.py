from typing import List, Tuple

def moyenne(valeurs: List[float]) -> float:
    """Calcule la moyenne arithmétique d'une liste de nombres."""
    if not valeurs:
        raise ValueError("La liste ne peut pas être vide")
    return sum(valeurs) / len(valeurs)

def regression_lineaire(x: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Calcule les coefficients a (pente) et b (ordonnée à l'origine) du modèle
    y = a*x + b par moindres carrés ordinaires (OLS).
    Renvoie (a, b).
    """
    if len(x) != len(y) or not x:
        raise ValueError("Listes x et y doivent être de même longueur et non vides")
    x_bar = moyenne(x)
    y_bar = moyenne(y)
    num = sum((xi - x_bar)*(yi - y_bar) for xi, yi in zip(x, y))
    den = sum((xi - x_bar)**2 for xi in x)
    if den == 0:
        raise ValueError("Division par zéro dans le calcul de la pente")
    a = num / den
    b = y_bar - a * x_bar
    return a, b