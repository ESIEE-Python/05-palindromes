import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import ispalindrome


input_output = [("Ésope reste ici et se repose", True), ("La mariée ira mal", True), ("élu par cette crapule", True),
                ("Et la marine va venir à Malte", True), ("Tu l'as trop écrasé, César, ce Port-Salut", True),
                ("À révéler mon nom, mon nom relèvera", True), ("Karine alla en Irak", True),
                ("ni palindrome ne mord ni lapin", True), ("Si bene te tua laus taxat, sua laute tenebis", True),
                ("A man, a plan, a canal : Panama", True),
                ("Eh ! ça va, la vache ?", True), ("L'essentiel est invisible pour les yeux", False),
                ("Je pense, donc je suis", False), ("Il faut agir, non pas rêver", False), ("La vie est un défi", False),
                ("L'ami naturel ? Le rut animal", True), ("Savoir, c'est pouvoir", False), ("L'amour est aveugle", False),
                ("La simplicité est la sophistication suprême", False), ("L'union fait la force", False),
                ("Engage le jeu que je le gagne", True), ("Tout est bien qui finit bien", False), ("L'important, c'est d'aimer", False),
                ("essayasse", True), ("Oh ! cela te perd, répéta l'écho", True),
                ("Noël a trop par rapport à Léon", True), ("Et si l'arôme des bottes révèle madame, le verset t'obsède, moraliste", True),
                ("4 834 872 952 820 199 705 196 890 986 915 079 910 282 592 784 384", True),
                ("4 834 872 952 820 199 765 196 890 986 915 079 910 282 592 784 384", False),
                ("Si Didon rêvait là-haut, Théo la verrait donc d'ici", False),
                ("rue Verlaine gela le génial rêveur", True), ("Angèle et Laurent enrôlaient les gens", False),
                ("No, it is opposed, art sees trade's opposition", True), ("Émile-Éric, notre valet, alla te laver ton ciré élimé", True),
                ("À révéler mon nom, mon nom se relèvera", False), ("ni palindrome ne mord ni lapin", True)]


@pytest.mark.parametrize("input,expected", input_output)
def test(input, expected):
    assert ispalindrome(input) == expected, input
