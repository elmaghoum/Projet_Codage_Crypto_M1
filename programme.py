import random

def hamming_codage(texte_original):
    resultat = ""       # Initialisation de resultat qui contiendra le resultat apres Hamming
    cpt_erreur = 0      # Initialisation de cpt_erreur qui comptera le nombre d'erreur

    print("Ensuite, il utilise le code de Hamming sur la lettre:")
    # Parcours du texte original par morceau de 7 bit
    for i in range(0, len(texte_original), 7):
        # Extraction des 7 caractères actuels
        code_original = list(texte_original[i:i + 7])
        code_corrigee = list(texte_original[i:i + 7])

        # Calcul des bits de contrôle
        c5 = (int(code_original[0]) + int(code_original[1]) + int(code_original[2])) % 2
        c6 = (int(code_original[0]) + int(code_original[1]) + int(code_original[3])) % 2
        c7 = (int(code_original[1]) + int(code_original[2]) + int(code_original[3])) % 2

        # Vérification et correction des erreurs
        if (int(code_original[4]) != c5 and int(code_original[5]) != c6 and c7 == int(code_original[6])):
            print("C1 est erroné")
            print(code_original)
            cpt_erreur += 1
            code_corrigee[0] = str(1 - int(code_original[0]))  # Correction du bit de données
            print(code_corrigee)
        elif (int(code_original[4]) != c5 and int(code_original[5]) != c6 and c7 != int(code_original[6])):
            print("C2 est erroné")
            print(code_original)
            cpt_erreur += 1
            code_corrigee[1] = str(1 - int(code_original[1]))  # Correction du bit de données
            print(code_corrigee)
        elif (int(code_original[4]) != c5 and int(code_original[5]) == c6 and c7 != int(code_original[6])):
            print("C3 est erroné")
            print(code_original)
            cpt_erreur += 1
            code_corrigee[2] = str(1 - int(code_original[2]))  # Correction du bit de données
            print(code_corrigee)
        elif (int(code_original[4]) == c5 and int(code_original[5]) != c6 and c7 != int(code_original[6])):
            print("C4 est erroné")
            print(code_original)
            cpt_erreur += 1
            code_corrigee[3] = str(1 - int(code_original[3]))  # Correction du bit de données
            print(code_corrigee)

        # Conversion de la liste corrigée en chaîne de caractères et ajout au résultat final
        code_corrigee_str = "".join(code_corrigee)
        resultat += code_corrigee_str

    # Affichage du nombre total d'erreurs détectées
    print("Il y a " + str(cpt_erreur) + " erreur(s)")
    return resultat

def retrait_bits_controle(resultat):
    print("\nHamming retire ensuite les bits de controle")
    # Retire les 3 bits de controle et garde que les 4 bits d'info
    resultat2 = ""
    for i in range(0, len(resultat), 7):
        code = list(resultat[i:i+7])
        code_sansControle = code[:4]
        code_sansControle_str = "".join(code_sansControle)
        resultat2 += code_sansControle_str

    return resultat2

print(" - DEBUT DU SCRIPT -")
print("Hamming découvre une lettre, l'enrichit d'un code correcteur d'erreur et l'envoie à son ami Huffman")
print("Huffman reçois la lettre et commence par la lire.\n")

# Ouvre le fichier en mode lecture
with open("projet_23_24_lettre.txt", "r") as f:
    # Lit tout le contenu du fichier 
    texte_original = f.read()
    # Supprime les caractères de nouvelle ligne et de retour a la ligne
    texte_original = texte_original.replace('\n', '').replace('\r', '')

resultat_hamming = hamming_codage(texte_original)

# Écriture du texte corrigé dans un nouveau fichier
with open("1.Lettre_corrigee.txt", "w") as f:
    f.write(resultat_hamming)
    print("\nLes résultats de l'étape de Hamming ont été enregistrés dans le fichier '1.Lettre_corrigee.txt'\n")

resultat_sans_controle = retrait_bits_controle(resultat_hamming)

# Écriture du message binaire sans bit de controle dans un nouveau fichier
with open("2.Lettre_corrigee_sans_bit_de_controle.txt", "w") as f:
    f.write(resultat_sans_controle)
print("Les résultats du retrait des bit de controle ont été enregistrés dans le fichier '2.Lettre_corrigee_sans_bit_de_controle.txt'\n")


def conversion_en_ASCII(resultat2):
    caracteres = ""
    for i in range(0, len(resultat2), 8):
        octet = resultat2[i:i+8]             # Extrait un octet de 8 bits de resultat2
        caractere = chr(int(octet, 2))       # Convertir l'octet binaire en caractère ASCII
        caracteres += caractere

    return caracteres

print("\nEnsuite, Huffman convertit ces resultat (message codé en binaire) en ASCII")
message_code = conversion_en_ASCII(resultat_sans_controle)

# Écriture du message convertie en ASCII dans un nouveau fichier
with open("3.Lettre_convertie_ASCII.txt", "w") as f:
    f.write(message_code)
    f.close
print("Les résultats de la conversion de la lettre en ASCII ont été enregistrés dans le fichier '3.Lettre_convertie_ASCII.txt'\n")

print("Obtenant une suite de caractères incohérents, il la décripte à l'aide du chiffre de Vigenere")
# Définition de la table de Vigenère comme indiquer sur le Rapport()
def creer_table_vigenere():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table_vigenere = []
    for i in range(len(alphabet)):
        decalage = alphabet[i:] + alphabet[:i]
        table_vigenere.append(decalage)
    return table_vigenere

# Déchiffrement du message avec la méthode de Vigenère
def dechiffrer_vigenere(message, cle):
    table_vigenere = creer_table_vigenere()         # Création de la table de Vigenère
    cle_repetee = ''                                # Initialisation de la clé répétée
    indice_cle = 0                                  # Initialisation de l'indice de la clé
    message_dechiffre = ''                          # Initialisation du message déchiffré
    caractere_accentues = ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'à', 'á', 'â', 'ã', 'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'ù', 'ú', 'û', 'ü', 'ý']

    for caractere in message:                            # Pour chaque caractère du message 
        if caractere in caractere_accentues:             # Si le caractère est accentué
            message_dechiffre += caractere               # Garder et recopier le caractère tel quel  
        elif caractere.isalpha():                        # Si le caractère est une lettre 
            while len(cle_repetee) <= indice_cle:        # Tant que la longueur de la clé répétée est inférieure ou égale à l'indice de la clé 
                cle_repetee += cle[indice_cle % len(cle)].upper()     # Répéter la clé jusqu'à ce qu'elle ait la même longueur que le message, en la convertissant en majuscules
            cle_actuelle = cle_repetee[indice_cle]                    # Prendre le caractère actuel de la clé répétée
            index_cle = ord(cle_actuelle) - ord('A')                  # Trouver l'index du caractère de la clé dans l'alphabet
            if caractere.isupper():                                   # Si le caractère du message est en majuscule
                index_message = ord(caractere) - ord('A')                        # Trouver l'index du caractère du message dans l'alphabet
                index_dechiffrement = (index_message - index_cle) % 26           # Calculer l'index de déchiffrement en utilisant la méthode de Vigenère
                message_dechiffre += table_vigenere[0][index_dechiffrement]      # Ajouter le caractère déchiffré au message
            else:                                                                # Si le caractère du message est en minuscule
                index_message = ord(caractere) - ord('a')                               # Trouver l'index du caractère du message dans l'alphabet
                index_dechiffrement = (index_message - index_cle) % 26                  # Calculer l'index de déchiffrement en utilisant la méthode de Vigenère
                message_dechiffre += table_vigenere[0][index_dechiffrement].lower()     # Ajouter le caractère déchiffré au message, en minuscule
            indice_cle += 1                                                             # Passer au caractère suivant de la clé
        else:                                           # Si le caractère n'est ni une lettre ni accentué
            message_dechiffre += caractere              # Garder et recopier le caractère tel quel
    return message_dechiffre                            # Renvoyer le message déchiffré


cle = "python"
message_decode = dechiffrer_vigenere(message_code, cle)

#Écriture du message déchiffré dans un fichier
with open("4.Message_déchiffré.txt", "w") as f:
    f.write(message_decode)
    f.close
print("Les résultats du déchiffrage de la lettre ASCII par Vigenère ont été enregistrés dans le fichier '4.Message_déchiffré.txt'\n")

print("Huffman veut maintenant envoyé ce message à Hamming, pour cela il rechiffre la lettre")
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


# Création aleatoire d'un masque de meme longueur que notre message
longueur = len(message_decode)
masque = generer_chaine_longueur_fixe(longueur)

texte_chiffrer = chiffre_vernam(message_decode,masque)
#Écriture du message rechiffrée dans un nouveau fichier
with open("5.Message_rechiffré.txt", "w") as f:
    f.write(texte_chiffrer)
    f.close
print("Les résultats du rechiffrage de la lettre par Vernam ont été enregistrés dans le fichier '5.Message_rechiffré.txt'\n")

with open("masque.txt", "w") as f:
    f.write(masque)
    f.close
print("Le masque utilisé pour le chiffrage par Vernam a été enregistrés dans le fichier 'masque.txt', ce marque doit être envoyé a Hamming afin qu'il puisse déchiffrer la lettre") 


print("Huffman apres avoir compressé la lettre (par Vernam) compresse maintenant cette lettre avant de l'envoyé à Hamming")

# Compression par la méthode de Huffman
def frequences_binaire(texte_binaire):
    freq = {}                          # Initialisation du tableau des fréquences
    for bit in texte_binaire:          # Pour chaque bit dans le texte binaire
        if bit in freq:                # Si le bit existe déjà dans le tableau de fréquences
            freq[bit] += 1             # Incrémenter sa fréquence
        else:
            freq[bit] = 1              # Ajouter le bit avec une fréquence de 1 au tableau
    return freq                        # Renvoyer le tableau de fréquences

def arbre_huffman(freq):
    arbres = [(freq[bit], bit) for bit in freq]         # Crée d'une liste de tuples (fréquence, bit) 
    while len(arbres) > 1:                              # Tant qu'il reste plus d'un arbre
        arbres.sort(key=lambda x: x[0])                 # Trie les arbres par fréquence
        gauche = arbres.pop(0)                          # Récupère et retire l'arbre le moins fréquent
        droite = arbres.pop(0)                          # Récupère et retire le deuxième arbre le moins fréquent)
        nouveau = (gauche[0] + droite[0], gauche, droite)       # Crée un nouvel arbre avec les deux arbres précédents comme fils
        arbres.append(nouveau)                                  # Ajoute le nouvel arbre à la liste des arbres
    return arbres[0]                                            # Renvoie l'arbre source

def codage_huffman(arbre):
    codes = {}                                  # Initialisation du tableau de codes de Huffman
    def parcours_arbre(noeud, code=''):
        if len(noeud) == 2:                          # Si le nœud est une feuille
            codes[noeud[1]] = code                   # Ajoute le bit et son code au tableau
        else:
            parcours_arbre(noeud[1], code + '0'     )           # Parcours le fils gauche avec un ajout de '0' au code
            parcours_arbre(noeud[2], code + '1')                # Parcours le fils droit avec un ajout de '1' au code
    parcours_arbre(arbre)                                       # Commence le parcours à partir de la racine de l'arbre
    return codes                                                # Renvoie le tableau de codes de Huffman

def compression_huffman(texte_binaire, codes):
    texte_compressé = ''                            # Initialisation du texte compressé
    for bit in texte_binaire:                       # Pour chaque bit dans le texte binaire
        texte_compressé += codes[bit]               # Ajoute le code correspondant à chaque bit au texte compressé
    return texte_compressé                          # Renvoie le texte compressé



texte_binaire = texte_chiffrer
freq = frequences_binaire(texte_binaire)
arbre = arbre_huffman(freq)
codes = codage_huffman(arbre)
texte_compressé = compression_huffman(texte_binaire, codes)

#print("Fréquences des éléments binaires:", freq)
#print("Arbre de Huffman:", arbre)
#print("Codage de Huffman:", codes)
#print("Texte binaire compressé:", texte_compressé)


#Écriture du texte déchiffré dans un fichier
with open("6.Message_rechiffré_compressé.txt", "w") as f:
    f.write(texte_compressé)
print("Les résultats de la lettre rechiffré et compressé ont été enregistrés dans le fichier '6.Message_rechiffré_compressé.txt'\n")


print("\nHamming reçois le message ainsi que le masque")
print("Il commence pas décompressé le message")
# Décompression par la methode de Huffman
# Pour la décompression on a juste besoin du texte compressé et de l'arbre precedent
def decompression_huffman(texte_compressé, arbre):
    texte_decompressé = ''               # Initialisation du texte décompressé
    racine = arbre                      # Initialisation de la racine de l'arbre

    # Parcourir l'arbre de Huffman pour récupérer les elements 
    for bit in texte_compressé:                    # Pour chaque bit dans le texte compressé
        if bit == '0':  # Si le bit est 0
            racine = racine[1]                     # Aller à l'enfant gauche
        else:  # Si le bit est 1
            racine = racine[2]                     # Aller à l'enfant droit

        if len(racine) == 2:                       # Si on atteint une feuille de l'arbre
            texte_decompressé += racine[1]         # Ajouter l'element au texte décompressé
            racine = arbre                         # Retourner à la racine de l'arbre pour le prochain element

    return texte_decompressé                       # Renvoyer le texte décompressé


# Utilisation de la fonction pour décompresser le texte
texte_decompressé = decompression_huffman(texte_compressé, arbre)

with open("7.message_crypté_décommpressé.txt", "w") as f:
    f.write(texte_decompressé)
print("Les résultats de la lettre chiffré décompressé ont été enregistrés dans le fichier '7.Message_chiffré_décompressé.txt'\n")

print("Une fois décompressé, il utilise le masque pour décrypté le message")
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
texte_final = dechiffre_vernam(texte_decompressé, masque)

with open("8.Texte_final_lu_par_Hamming.txt", "w") as f:
    f.write(texte_final)
print("Les résultats de la lettre dechiffré par Vernam ont été enregistrés dans le fichier '8.Texte_final_lu_par_Hamming.txt'\n")
print("Une fois le message décrypté, Hamming peut enfin lire le message.")