import random

# Génération d'une chaîne de même longueur que le message pour le chiffrement de Vernam
def generer_chaine_longueur_fixe(longueur):
    caracteres = [chr(i) for i in range(97, 122)]                          # Création d'une liste de caractères ASCII minuscules
    return ''.join(random.choice(caracteres) for _ in range(longueur))     # Génération d'une chaîne aléatoire de longueur fixe en choisissant aléatoirement des caractères de la liste

# Chiffrement du message avec le chiffre de Vernam
def chiffre_vernam(texte_a_chiffrer, cle):
    texte_chiffre = ""                          # Initialisation du texte chiffré
    cle_index = 0                               # Initialisation de l'indice de la clé
    cle = cle.upper()                           # Conversion de la clé en majuscules
    for lettre in texte_a_chiffrer:                    # Pour chaque lettre dans le texte à chiffrer
        if lettre.isalpha():                           # Si la lettre est alphabétique
            if lettre.isupper():                       # Si la lettre est en majuscule
                lettre_chiffree = chr((ord(lettre) + ord(cle[cle_index]) - 2 * ord('A')) % 26 + ord('A'))   # Calcul du caractère chiffré en utilisant le chiffre de Vernam
                cle_index = (cle_index + 1) % len(cle)           # Passage au caractère suivant de la clé
            else:                                                # Si la lettre est en minuscule
                lettre_chiffree = chr((ord(lettre) + ord(cle[cle_index]) - 2 * ord('a')) % 26 + ord('a'))   # Calcul du caractère chiffré en utilisant le chiffre de Vernam
                cle_index = (cle_index + 1) % len(cle)      # Passage au caractère suivant de la clé
            texte_chiffre += lettre_chiffree                # Ajout du caractère chiffré au texte chiffré
        else:                                               # Si la lettre n'est pas alphabétique
            texte_chiffre += lettre                         # Conserve les caractères non-alphabétiques dans le texte chiffré
    return texte_chiffre                                    # Renvoyer le texte chiffré


texte="bonjour"
# Création aleatoire d'un masque de meme longueur que notre message
longueur = len(texte)
masque = generer_chaine_longueur_fixe(longueur)
texte_chiffrer = chiffre_vernam(texte,masque)

print("Texte a chiffrer : "+texte+"\n")
print("Masque de longueur "+str(longueur)+" a été générer : "+masque+"\n")
print("Texte chiffré : "+texte_chiffrer+"\n")


# Définition de la fonction pour déchiffrer un texte avec le chiffre de Vernam
def dechiffre_vernam(texte_a_dechiffrer, cle):
    texte_dechiffre = ""
    cle_index = 0 
    cle = cle.upper()                           # Conversion de la clé en majuscules
    for lettre in texte_a_dechiffrer:           # Pour chaque caractere dans le texte à déchiffrer
        if lettre.isalpha():                    # Si le caractere est une lettre
            if lettre.isupper():                # Si le caractere est en majuscule
                # Déchiffrement du caractère en utilisant la clé de Vernam et l'alphabet en majuscules
                lettre_dechiffree = chr((ord(lettre) - ord(cle[cle_index]) + 26) % 26 + ord('A'))
                cle_index = (cle_index + 1) % len(cle)                   # Passage au caractère suivant de la clé
            else:                                                        # Si la lettre est en minuscule
                # Déchiffrement du caractère en utilisant la clé de Vernam et l'alphabet en minuscules
                lettre_dechiffree = chr((ord(lettre) - ord(cle[cle_index]) + 26) % 26 + ord('a'))
                cle_index = (cle_index + 1) % len(cle)                  # Passage au caractère suivant de la clé
            texte_dechiffre += lettre_dechiffree                        # Ajout du caractère déchiffré au texte resultat
        else:
            texte_dechiffre += lettre                                   # Sinon on garde et recopie le caractère tel quel
    return texte_dechiffre  # Renvoyer le texte déchiffré


# Dechiffrage du texte decompressé par la methode Vernam et grace au masque envoyé par Huffman
texte_final = dechiffre_vernam(texte_chiffrer, masque)

print("Texte déchiffré avec le même masque : "+texte_final+"\n")
