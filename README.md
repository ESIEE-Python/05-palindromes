# Palindromes

Un [palindrome(https://fr.wikipedia.org/wiki/Palindrome)] est un mot ou une phrase qui se lit indifféremment de droite à gauche et de gauche à droite. L'objectif est d'écrire du code qui permet de vérifier si une chaine de caractère est un palindrome ou pas.

Le fichier ``main.py`` contient :

- une fonction secondaire ``ispalindrome()`` qui a pour but de vérifier si une chaine de caractère est un palindrome ou pas. 
  
  - elle prend en argument une chaine de caractères ``s`` ;
  - et retourne un booléen exprimant la vérité de « ``s`` est un palindrome ». 
  
- la fonction principale ``main()`` qui fait quelques appels à la fonction secondaire permettant de vérifier son bon fonctionnement .

## To do

1️⃣ Ecrire le code de la fonction secondaire.

> [!TIP]
Pour traiter efficacement le problème des caractères accentués, utiliser la méthode [translate()](https://docs.python.org/3/library/stdtypes.html#str.translate) qui prend en argument une table de correspondance créée avec la méthode statique [str.maketrans()](https://docs.python.org/3/library/stdtypes.html#str.maketrans)

2️⃣ Ecrire quelques appels à la fonction secondaire dans ``main()``.

3️⃣ Exécuter le programme depuis le terminal

    $ python main.py

4️⃣ Une fois le code fonctionnel, le soumettre aux tests unitaires. Le grade obtenu est le pourcentage de tests réussis. 

    $ pytest .python

Si le grade n'est pas satisfaisant, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le grade est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/python/chapters/16-style.html). Scorer cette qualité

    $ pylint main.py

Si le score n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages

6️⃣ Lorsque le grade et le score ``pylint`` sont satisfaisants, pusher le travail pour évaluation

    $ git pull
    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.
