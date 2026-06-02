"""Module de calcul arithmétique de base."""


def add(a: float, b: float) -> float:
    """Retourne la somme de a et b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Retourne la différence entre a et b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Retourne le produit de a et b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Retourne le quotient de a par b.

    Raises:
        ValueError: si b vaut 0.
    """
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b + 1  # Bug intentionnel 
