#!/Users/Ldech/AtelierAlgo/DM_RPG/RPG.py
# -*-coding:Utf-8 -*


from arme import Arme
from personnage import Personnage
import pygame 
pygame.mixer.init()

nom = input("veuillez entrer le nom de votre personnage : ")

while True:
    
    perso  = Personnage (nom,120,0,"épée en bois",20)
    print(perso)
    
    #étape 2 : choisir l'adversaire à attaquer 
    reponse = input("""qui voulez vous combattre? :
            1 - Jean le gobelin (75pv,armé d'un gourdin (15 dg) )         
            2 - Michel l'orc (100pv, armé d'une épée rouillée (20dg) )
            3 - Jacque le troll (200pv, armé d'une hache (30dg) )
            0 - Quitter le jeu
            alors ? : """)

    while True:

        try:
            reponse = int(reponse)
            break
        except ValueError:
            print('entrez un nombre svp. Recommencez...')
            break



    if reponse == 1:
        mechant= Personnage("Jean le gobelin",75,0,"Gourdin",15)
        print(mechant)
        print(perso)
    if reponse == 2:
        mechant = Personnage("Michel l'orc",100,0,"Epée rouillée",20)
        print(mechant)
        print(perso)
    if reponse == 3:
        mechant = Personnage("Jacque le troll",200,0,"Hache",30)
        print(mechant)
        print(perso)
    if reponse == 0:
        print("Merci d'avoir joué !!!")
        exit
        break


    



    while perso.PdtVie != 0 or mechant.PdtVie != 0:
        
        action = input("""
        1 - Attaquer
        2 - Changer d'arme (Epée,45 dg)
        alors ? : """)


        while True:

            try:
                action = int(action)
                break
            except ValueError:
                print('entrez un nombre svp. Recommencez...')
                break
        
        if action == 1:
            perso.Attaque(mechant)
            mechant.Attaque(perso)
            print(perso)
            print(mechant)
            if perso.PdtVie <= 0:
                pygame.mixer.Sound('gta-v-death-sound-effect-102.wav').play()
                print("W A S T E D")
                break
            elif mechant.PdtVie <= 0:
                pygame.mixer.Sound('Zelda_open_Coffre.wav').play()
                print("Il est mort, bravo!")
                break
        if action == 2:
            mechant.Attaque(perso)
            perso.Arme= Arme("Epée",45)
            print(perso)
            print(mechant)
        if perso.PdtVie <= 0:
                pygame.mixer.Sound('gta-v-death-sound-effect-102.wav').play()
                print("W A S T E D")
                break
        continue
        

    



    
    