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
        ValueError: si b vaut 0 ou 0.0.
    """
    if b == 0 or b == 0.0:
        raise ValueError("Division par zéro impossible.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Retourne la base élevée à la puissance de l'exposant.

    Raises:
        TypeError: si la base ou l'exposant n'est pas un nombre.
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("La base et l'exposant doivent être des nombres.")
    return base ** exponent
