import random

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



texte = "experimentation"
freq = frequences_binaire(texte)
arbre = arbre_huffman(freq)
codes = codage_huffman(arbre)
texte_compressé = compression_huffman(texte, codes)

print("Fréquences des éléments binaires:", freq,"\n")
print("Arbre de Huffman:", arbre,"\n")
print("Codage de Huffman:", codes,"\n")
print("Texte binaire compressé:", texte_compressé,"\n")



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
print("Texte décompressé:", texte_decompressé+"\n")