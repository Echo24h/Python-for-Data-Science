# ft_package

Un package Python d'exemple pour l'exercice 09.

## Build

```bash
pip install build
python -m build
```

## Installation

Vous pouvez installer ce package en utilisant pip. Assurez-vous d'avoir Python installé sur votre système.

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

ou

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Vérification

```bash
pip show -v ft_package
```

## Utilisation

Après l'installation, vous pouvez utiliser ce package dans vos scripts Python comme ceci :

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## Suppression

Pour supprimer ce package, utilisez la commande pip suivante :

```bash
pip uninstall ft_package
```
