from random import choice
from unidecode import unidecode

nb_erreur = 0


def afficher(nb_erreur):
    if nb_erreur == 0:
        zero_faute = ("""

       """)
        return zero_faute

    if nb_erreur == 1:
        une_fautes = ("""

        _________ 

       """)

        return une_fautes

    if nb_erreur == 2:
        deux_fautes = ("""

        |
        |                                            
        |                
        |               
        |_________

        """)
        return deux_fautes

    if nb_erreur == 3:
        trois_fautes = ("""
        
        |''''''''''''''''
        |                                           
        |               
        |               
        |_________ 
        
        """)
        return trois_fautes

    if nb_erreur == 4:
        quatres_fautes = ("""
        
        |''''''''''''''''|
        |                                           
        |               
        |               
        |_________ 
        
        """)
        return quatres_fautes

    if nb_erreur == 5:
        cinq_fautes = ("""
        
        |''''''''''''''''|
        |                O                             
        |                 
        |                
        |_________ 
        
        """)
        return cinq_fautes

    if nb_erreur == 6:
        six_fautes = ("""
        
        |''''''''''''''''|
        |                O                             
        |                | 
        |               
        |_________ 
        
        """)
        return six_fautes

    if nb_erreur == 7:
        sept_fautes = ("""
        
        |''''''''''''''''|
        |                O                             
        |               /| 
        |               
        |_________ 
        
        """)
        return sept_fautes

    if nb_erreur == 8:
        huit_fautes = ("""
        
        |''''''''''''''''|
        |                O                             
        |               /|\  
        |               
        |_________ 
        
        """)
        return huit_fautes

    if nb_erreur == 9:
        neuf_fautes = ("""
        
        |''''''''''''''''|
        |                O                             
        |               /|\  
        |               / 
        |_________ 
        
        """)
        return neuf_fautes

    if nb_erreur == 10:
        dix_fautes = ("""

        |''''''''''''''''|
        |                O                             
        |               /|\  
        |               / \ 
        |_________ 
        
                GAME OVER
        """)
        return dix_fautes


def word():
    ma = ("1: Mot aléatoire")
    md = ("2: Mot défini")
    choix = 0
    while choix not in ("1", "2"):
        print("Mot aléatoire = 1 ou Mot défini = 2")
        try:
            choix = (int(input("1: \ 2: ")))
        except ValueError:
            continue
        if choix == 1:
            print("Vous avez choisi le mode : {}".format(ma))
            with open("mots_pendu.txt", "r", encoding='utf8') as f:
                contenu = f.readlines()
            return unidecode(choice(contenu)).upper().replace('\n', '')
        if choix == 2:
            print("Vous avez choisi le mode : {}".format(md))
            mot_definie = str(input("Taper le mot à trouver : "))
            return unidecode(mot_definie).upper().replace('\n', '')
        else:
            continue


def underscore(mot, L=[]):
    r = ""
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '

    return r[:-1]


def saisie():
    lettre = input('Entrez une lettre: ')
    if len(lettre) > 1 or len(lettre) < 1 or ord(lettre) < 65 or ord(lettre) > 122:
        return saisie()
    else:
        return lettre.upper()

# Programme principal


lettres_proposées = []
mot_à_deviner = word()
affichage = underscore(mot_à_deviner)
print("Mot à deviner :", affichage)


while '_' in affichage and nb_erreur < 10:
    lettre = saisie()
    if lettre not in lettres_proposées:
        lettres_proposées += [lettre]

    if lettre not in mot_à_deviner:
        nb_erreur += 1

    affichage = underscore(mot_à_deviner, lettres_proposées)
    print('\nMot à deviner : ', affichage, ' '*10,
          'Nombre d\'erreurs maximum : ', 10-nb_erreur, afficher(nb_erreur))

if nb_erreur == 1:
    pt = ('point')
else:
    pt = ('points')

if '_' not in affichage:
    print("Bien joué, vous avez gagné")
else:
    print("Vous avez perdu")
