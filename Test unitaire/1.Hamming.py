import random

def hamming_codage(texte_original):
    resultat = ""       # Initialisation de resultat qui contiendra le resultat apres Hamming
    cpt_erreur = 0      # Initialisation de cpt_erreur qui comptera le nombre d'erreur

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
    print("c5=" + str(c5) + "  /   c6="+str(c6)+"  /  c7="+str(c7))
    print("\nIl y a " + str(cpt_erreur) + " erreur(s)")
    return resultat

def retrait_bits_controle(resultat):
    # Retire les 3 bits de controle et garde que les 4 bits d'info
    resultat2 = ""
    for i in range(0, len(resultat), 7):
        code = list(resultat[i:i+7])
        code_sansControle = code[:4]
        code_sansControle_str = "".join(code_sansControle)
        resultat2 += code_sansControle_str

    return resultat2


#texte_original="0101100"    #Exemple sans erreur
texte_original="1100111"    # Exemple avec 1 erreur
print("Mot : "+texte_original+"\n")
resultat_hamming = hamming_codage(texte_original)

print("\nRésultats de l'étape de Hamming : \n"+resultat_hamming)

resultat_sans_controle = retrait_bits_controle(resultat_hamming)
print("\nRésultats du retrait des bit de controle : \n"+resultat_sans_controle)
