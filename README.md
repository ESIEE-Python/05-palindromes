> [!CAUTION]
Ce travail s'effectue dans [l'environnement Github](https://perso.esiee.fr/~courivad/courses/utils/misc-01-github-environment.html)

# Palindromes

Un [palindrome(https://fr.wikipedia.org/wiki/Palindrome)] est un mot ou une phrase qui se lit indifféremment de droite à gauche et de gauche à droite. L'objectif est d'écrire du code qui permet de vérifier si une chaine de caractère est un palindrome ou pas.

Le fichier ``main.py`` contient :

- une fonction secondaire ``ispalindrome()`` qui a pour but de vérifier si un mot est un palindrome ou pas. 
  
  - elle prend en argument une chaine de caractères ``s`` ;
  - et retourne un booléen exprimant la vérité de « ``s`` est un palindrome ».
  
- la fonction principale ``main()`` qui fait quelques appels à la fonction secondaire permettant de vérifier son bon fonctionnement .

## Informations complémentaires

Il existe plusieurs stratégies pour résoudre le problème.

### Algorithme itératif

On peut utiliser un algorithme itératif "bas niveau" en parcourant les caractères de la chaîne simultanément à partir du début et de la fin. Le terme "bas niveau" est employé parce que la solution s'intéresse aux éléments constitutifs de la chaîne de caractère, pas à la chaîne elle même. Cet algorithme fonctionne mais ne tire pas partie des fonctionnalités de Python.

### Approche "haut niveau"

Une approche "haut niveau" ou *pythonique* va a contrario considérer la chaîne de caractère comme l'élément de base. Elle ne nécessite donc pas d'itérations.On utilise exclusivement le slicing et les [méthodes de chaines de caractères](https://docs.python.org/3/library/stdtypes.html#string-methods). Lesquelles ? Cette façon de faire est plus concise, plus performante et doit être privilégiée.

### Algorithme récursif

On peut également utiliser la récursivité. Quels sont les cas de base ? Quel est l'appel récursif ?

### Le problème des caractères accentués

Avant de tester le caractère palindromique de la chaine de caractères, les caractères accentués qui la composent devront être "désaccentués". Ce peut être fait par un enchainement de méthodes ``replace()`` mais le problème sera plus élégamment traité avec la méthode [translate()](https://docs.python.org/3/library/stdtypes.html#str.translate).

<!-- START INSERT -->

## To do

1️⃣ Ecrire (ou modifier) le code de la fonction secondaire.

2️⃣ Si nécessaire, ajouter (ou modifier) les appels à la fonction secondaire logés dans la fonction principale ``main()``. Cela permet de tester la fonction secondaire sur quelques cas simples.

3️⃣ Exécuter le programme depuis le terminal. Tant que la fonction secondaire ne retourne pas les résultats attendus, répéter le cycle 1️⃣ 2️⃣ 3️⃣.

    $ python main.py

4️⃣ Lorsque les résultats obtenus à l'étape 3️⃣ sont satisfaisants, soumettre le code à une procédure de test plus robuste, les tests unitaires.

    $ pytest .python

Le score de test ``ST`` obtenu est le pourcentage de tests réussis. Tant que certains tests échouent, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le score de test ``ST`` est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/courses/utils/sources/python-23-codequality.html).

    $ pylint main.py

Si le score de qualité ``SQ`` n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages dans le terminal

6️⃣ Lorsque les scores ``ST`` et ``SQ`` sont satisfaisants, pusher le travail vers votre repo distant. Ce travail est susceptible d'être pris en compte dans l'évaluation de l'unité.

    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.

<!-- END INSERT -->
