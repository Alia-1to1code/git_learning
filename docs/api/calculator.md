# Référence API — calculator

### `add(a, b)`

Retourne la **somme** de `a` et `b`.

| Paramètre | Type | Description |
|-----------|------|-------------|
| `a` | `float` | Premier opérande |
| `b` | `float` | Second opérande |

**Retourne :** `float`

### `subtract(a, b)`

Retourne la **différence** entre `a` et `b`.

### `multiply(a, b)`

Retourne le **produit** de `a` et `b`.

### `divide(a, b)`

Retourne le **quotient** de `a` par `b`.

**Lève :** `ValueError` si `b == 0`.