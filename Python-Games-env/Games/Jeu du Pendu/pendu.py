from random import choice
from unidecode import unidecode

my_file_path = r"Python-Games-env/Games/Jeu du Pendu/motsPendu.txt"

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
    ma = ("1: Mot al??atoire")
    md = ("2: Mot d??fini")
    choix = 0
    while choix not in ("1", "2"):
        print("Mot al??atoire = 1 ou Mot d??fini = 2")
        try:
            choix = (int(input("1: \ 2: ")))

        except ValueError:
            continue
        if choix == 1:
            print("Vous avez choisi le mode : {}".format(ma))
            with open(my_file_path, "r", encoding='utf8') as f:
                contenu = f.readlines()
            return unidecode(choice(contenu)).upper().replace('\n', '')
        if choix == 2:
            print("Vous avez choisi le mode : {}".format(md))
            mot_definie = str(input("Taper le mot ?? trouver : "))
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


lettres_propos??es = []
mot_??_deviner = word()
affichage = underscore(mot_??_deviner)
print("Mot ?? deviner :", affichage)


while '_' in affichage and nb_erreur < 10:
    lettre = saisie()
    if lettre not in lettres_propos??es:
        lettres_propos??es += [lettre]

    if lettre not in mot_??_deviner:
        nb_erreur += 1

    affichage = underscore(mot_??_deviner, lettres_propos??es)
    print('\nMot ?? deviner : ', affichage, ' '*10,
          'Nombre d\'erreurs maximum : ', 10-nb_erreur, afficher(nb_erreur))

if nb_erreur == 1:
    pt = ('point')
else:
    pt = ('points')

if '_' not in affichage:
    print("Bien jou??, vous avez gagn??")
else:
    print("Vous avez perdu")
    print("Le mot ??tait:", mot_??_deviner)
