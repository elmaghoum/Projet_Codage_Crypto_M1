
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

# Exemple avec "icla", cencé donné le mot "test"
message_code = "icla"
cle = "python"

# Ligne P, on cherche I : on trouve la colonne T
# Ligne Y, on cherche C : on trouve la colonne E
# Ligne T, on cherche L : on trouve la colonne S
# Ligne H, on cherche A : on trouve la colonne T

#Exemple de Wikipedia
#message_code = "V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY"
#cle = "musique"

message_decode = dechiffrer_vigenere(message_code, cle)

print("Le message codé est : "+message_code)
print("Le message décodé est : "+message_decode)