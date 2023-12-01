from string import ascii_uppercase


def encode(word, key):
    word, key = word.upper(), key.upper() # On met les chaines en majuscules
    x, y = [ascii_uppercase.find(letter) for letter in word], ([ascii_uppercase.find(letter) for letter in key] * (len(word)//len(key) + 1))[:len(word)] # On cree les listes x et y du chiffrage de Vigenere (cf exercice)
    z = [(x[i] + y[i]) % 26 for i in range(len(word))] # On calcule tous les restes modulo 26 de x + y

    return "".join([ascii_uppercase[i] for i in z]) # On renvoie la chaine chiffree

print(encode("scientifique", "math"))
print(encode("toto", "de"))


def decode(unknow, key):
    unknow, key = unknow.upper(), key.upper()  # On met les chaines en majuscules
    z, y = [ascii_uppercase.find(letter) for letter in unknow], ([ascii_uppercase.find(letter) for letter in key] * (len(unknow)//len(key) + 1))[:len(unknow)]  # On cree les lites z et y
    x = [(z[i] - y[i]) % 26 for i in range(len(z))]  # On calcule le nombre x qui additionne a y est congru a z modulo 26

    return "".join([ascii_uppercase[i] for i in x]) # On affiche le mot dechiffre a partie des valeurs x

print(decode("YMABQILB", "deux"))


def brute_force(unknow):
    for n in range(3, 5):  # On ne considere que les cles ayant au moins 4 caracteres

        with open("liste_de_mots_francais.txt", encoding="utf-8") as file:  # On stocke les mots francais dans le set "words"
            words = set(line.strip() for line in file)

        key = [0] * n  # Liste prenant toutes les valeurs de cle possibles de longueur n

        for tour in range(26**(n-1)): # Ici il s'agit d'une (n-1)-liste des lettres de l'alphabet. (seulement n-1 car la derniere lettre est prise en compte ci-dessous)

            for i in range(26): # Ici on s'occupe de la derniere lettre

                if decode(unknow, "".join([ascii_uppercase[k] for k in key])).lower() in words: # Si on a trouve un mot francais
                    file.close() # On ferme notre fichier
                    return f"Clé : {''.join([ascii_uppercase[k] for k in key])}\nMot : {decode(unknow, ''.join([ascii_uppercase[k] for k in key]))}"  # On affiche de le mot dechiffre et sa cle

                key[-1] += 1

            for o, p in enumerate(key[::-1]): # Ici on s'occupe d'incrementer les valeurs de key pour tester une nouvelle cle
                if p >= 25:
                    key[len(key)-1 -o-1] += 1
                    key[len(key)-1 - o] = 0

                if key[len(key)-1 -o-1] <= 25:
                    break

    file.close()
    return "On a rien trouve !"

print(brute_force("ERPTOTRETREHTHRETHE"))