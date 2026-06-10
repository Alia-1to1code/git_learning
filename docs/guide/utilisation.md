# Utilisation
## Le module calculator
Le module `src.calculator` fournit cinq opérations arithmétiques de base.

### Import
```python
from src.calculator import add, subtract, multiply, divide, power
```

### Exemples
```python
# Addition
result = add(10, 5)
print(result)   # 15

# Division avec gestion d'erreur
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)    # Division par zéro impossible.

# Division avec flottant nul — même comportement
try:
    result = divide(10, 0.0)
except ValueError as e:
    print(e)    # Division par zéro impossible.
```

!!! warning "Attention"
    La fonction `divide` lève une `ValueError` si le diviseur est égal à zéro,
    que ce soit un entier (`0`) ou un flottant (`0.0`).