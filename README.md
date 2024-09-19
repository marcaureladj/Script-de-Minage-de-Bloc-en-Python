# Script de Minage de Bloc en Python

Ce projet implémente un script simple de minage de blocs en Python. Le script utilise le **multiprocessing** pour paralléliser le processus de minage, permettant à plusieurs cœurs de CPU de tester différents nonces en parallèle afin de trouver un hash valide qui respecte la difficulté requise.

## Table des matières
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple](#exemple)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fonctionnalités

- **Hachage SHA-256** : Utilise la bibliothèque `hashlib` pour calculer des hachages SHA-256.
- **Traitement en parallèle** : Utilise le **multiprocessing** pour exploiter plusieurs cœurs CPU afin de miner plus rapidement.
- **Difficulté personnalisable** : Modifiez la difficulté du minage en changeant le nombre de zéros requis au début du hash.
- **Barre de progression** : Utilise `tqdm` pour afficher une barre de progression indiquant l'avancée du minage.

## Prérequis

- Python 3.6+
- Bibliothèques :
  - `tqdm` : Pour afficher des barres de progression.

## Installation

Pour commencer, clonez ce dépôt et installez les dépendances requises :

```bash
# Cloner le dépôt
git clone https://github.com/marcaureladj/Script-de-Minage-de-Bloc-en-Python.git

# Aller dans le répertoire du projet
cd nom-du-repertoire

# Installer les dépendances
pip install tqdm
```

## Utilisation

Pour exécuter le script de minage, lancez simplement le fichier `main.py` avec Python :

```bash
python main.py
```

Vous pouvez modifier la difficulté du minage et le nombre de nonces à tester en ajustant les variables suivantes dans le script :

```python
DIFFICULTY = 6  # Ajustez le nombre de zéros requis au début du hash
MAX_TESTED_NONCE = 50000000  # Définissez le nombre maximum de nonces à tester
```

Le script s'exécutera, affichera une barre de progression et imprimera le hash valide du bloc ainsi que le nonce une fois la solution trouvée.

## Exemple

Voici un exemple de l'exécution du script :

```bash
Block trouvé avec le hash : 00000000000000000000cb1c466ea12f0ee1c5370495e8b8d16138210488f047, et le nonce : 12345678
Minage fini!
```

## Contribuer

N'hésitez pas à contribuer à ce projet ! Forkez le dépôt, apportez vos modifications, puis soumettez une pull request.

1. Forkez le dépôt.
2. Créez une nouvelle branche pour votre fonctionnalité : `git checkout -b nom-de-la-fonctionnalité`.
3. Committez vos modifications : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`.
4. Poussez vers la branche : `git push origin nom-de-la-fonctionnalité`.
5. Ouvrez une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
```
