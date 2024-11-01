# Projet de Codage et Cryptographie Master 1 - UB - 2023/2024

# Introduction
La cryptographie et le codage sont des domaines cruciaux dans la sécurisation des données et des communications. Ils permettent de garantir la confidentialité, l’intégrité et l’authenticité desinformations échangées, notamment dans un contexte où les menaces informatiques sont de plus en plus nombreuses et sophistiquées.


# Contexte 
Ce projet, réalisé en binôme, consiste à effectuer une série de manipulations sur une lettre codée et chiffrée, en suivant les étapes décrites dans un scénario.

L’objectif principal de ce projet est de développer nos compétences en matière de codage, décodage, chiffrement et déchiffrement, en utilisant différentes techniques et algorithmes très connus dans le monde du codage et de la cryptographie comme : 
- Le code de Hamming
- Décodage du texte en ASCII
- Chiffre de Vigenère
- Chiffre de Vernam
- Compression/décompression par la méthode de Huffman


# Scénario
Une personne A trouve une lettre chiffrée, elle la déchiffre et la lie.
Puis, elle la crypte et la compresse pour l'envoyer à une personne B, pour qu'elle puisse la lire à son tour.

Selon ce scénario donné, nous avons listé ce qu'il faut faire sous forme d'étape pour chaque personne (A et B).

## Étapes Réalisées par la personne A

1. **Lecture de la lettre en binaire**
2. **Correction du message binaire** à l’aide des bits de contrôle
3. **Retrait des bits de contrôle**
4. **Décodage du texte en ASCII**
5. **Déchiffrage du message**
6. **Lecture de la lettre et chiffrement de celle-ci** 
7. **Compression du message chiffré**
8. **Envoi du message crypté et compressé**, accompagné du masque.

## Étapes Réalisées par la personne B

1. **Décompression du message chiffré**
2. **Déchiffrement en utilisant le masque**
3. **Lecture de la lettre**


## Contenu des Fichiers et Dossiers

- **`projet_23_24_lettre.txt`** : La lettre de départ trouvée par la personne A.
- **`programme.py`** : Le script principal qui exécute l'intégralité du scénario, produisant un fichier `.txt` en sortie pour chaque étape du processus.

# Instructions d'Exécution

Pour exécuter ce code Python, utilisez la commande suivante (en faisant bien attention à avoir la "lettre" au même lieu d'éxécution) :
```bash
python3 programme.py
```

## Détails Additionnels

Pour plus de détails sur chaque étape et méthode de codage/cryptographie utilisée, vous pouvez consulter le dossier **Test unitaire**. Ce dossier contient des scripts individuels pour tester chaque méthode séparément.


# Bilan du Projet de Codage et Cryptographie

Ce projet nous a permis d'explorer et de mettre en œuvre diverses techniques d’encodage, de décodage, de compression, de décompression, ainsi que de chiffrement et de déchiffrement. Nous avons appris à implémenter ces méthodes de manière efficace et à les adapter spécifiquement au cas étudié (traitement d'une lettre).

Au cours de ce projet, nous avons :

- Approfondi nos connaissances en cryptographie et en codage.
- Développé des bonnes pratiques de programmation et en terme de securité.
- Renforcé notre capacité à travailler en équipe et à résoudre des problèmes complexes.
- Amélioré nos compétences en communication pour présenter nos résultats de manière claire et structurée.

# Auteurs
- EL MAGHOUM Fayçal
- EMIR-MOUNGONDO Cristan

# Bibliographie  
http ://v.vincent.u-bourgogne.fr/0ENS/THEO-INFO/index.html
Cours de M1 - Codage et Cryptographie, par Vincent Vajnovszki et GENESTIER Richard,
UB - UFR Sciences et techniques, Dijon

---  Avril 2024
