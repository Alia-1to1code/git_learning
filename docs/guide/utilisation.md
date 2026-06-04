# Utilisation

## Le module calculator

Le module `src.calculator` fournit quatre opérations arithmétiques de base.

### Import

```python
from src.calculator import add, subtract, multiply, divide
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
``` 

!!! warning "Attention"
    La fonction `divide` lève une `ValueError` si le diviseur est égal à zéro.