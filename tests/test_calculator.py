"""Tests unitaires pour le module calculator."""

import pytest
from src.calculator import add, subtract, multiply, divide, power


class TestAdd:
    def test_integers_positifs(self):
        assert add(2, 3) == 5

    def test_avec_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_nombres_negatifs(self):
        assert add(-2, -3) == -5

    def test_flottants(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtract:
    def test_soustraction_simple(self):
        assert subtract(10, 4) == 6

    def test_resultat_negatif(self):
        assert subtract(3, 7) == -4


class TestMultiply:
    def test_multiplication_simple(self):
        assert multiply(3, 4) == 12

    def test_par_zero(self):
        assert multiply(5, 0) == 0

    def test_flottants(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)


class TestDivide:
    def test_division_simple(self):
        assert divide(10, 2) == 5.0

    def test_division_flottants(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_division_par_zero_leve_exception(self):
        with pytest.raises(ValueError, match="Division par zéro impossible"):
            divide(5, 0)

    def test_division_par_zero_flottant_leve_exception(self):
        with pytest.raises(ValueError, match="Division par zéro impossible"):
            divide(10, 0.0)


class TestPower:
    def test_cas_classique(self):
        assert power(2, 3) == 8.0

    def test_exposant_zero(self):
        assert power(5, 0) == 1.0

    def test_exposant_negatif(self):
        assert power(2, -2) == pytest.approx(0.25)

    def test_base_negative(self):
        assert power(-2, 3) == -8.0

    def test_parametres_invalides_levent_exception(self):
        with pytest.raises(TypeError, match="La base et l'exposant doivent être des nombres"):
            power("deux", 3)
