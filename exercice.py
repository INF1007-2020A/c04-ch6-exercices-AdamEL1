#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        for i in range(0, 10):
            values.append(input())
        values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [input(), input()]
        for char in words[0]:
            if char not in words[1]:
                return False
    return True


def contains_doubles(items: list) -> bool:
    for i, item in enumerate(items):
        for j, words in enumerate(items):
            if item == words and 1 != j:
                return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    average = {}
    for i in student_grades.items():
        average[i[0]] = get_average(i[1])
    max = 0
    max_key = ""
    for items in average.items():
        if max < items[1]:
            max = items[1]
            max_key = items[0]
    return {max_key: max}


def get_average(l: list):
    val = 0
    for i in l:
        val += int(i)
    return val / len(l)


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = [sentence.count(alphabet[i] or alphabet[i].upper()) for i in range(0, len(alphabet))]
    for i in range(0, len(letters)):
        letters[i] = [letters[i], i]
    letters.sort()
    for i in range(0, len(letters)):
        if letters[len(letters)-1-i][0] > 5:
            print(f"{alphabet[letters[len(letters)-1-i][1]]} : {letters[len(letters)-1-i][0]}")

    #Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    ## order()

    print(f"On vérifie les anagrammes...")
    ## anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    ## recipes = get_recipes()

    print("On affiche une recette au choix...")


## print_recipe(recipes)


if __name__ == '__main__':
    main()
