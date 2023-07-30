#!/Users/Ldech/AtelierAlgo/DM_RPG/RPG_V2.py
# -*-coding:Utf-8 -*


from arme import Arme
from personnage import *
from pyfiglet import Figlet

nom = input("veuillez entrer le nom de votre personnage : ")

f = Figlet(font='slant')
print(f.renderText('RPG VERSION FINAL'))

while True:
    #étape1 bis : choisir le type de combattant
  
    
    while True:
        
        choix = input("""Vous êtes ?
            1 - Un guerrier (120 points de vie, attaque puissante)
            2 - un mage Rouge (100 points de vie , boule de feu)
            3 - un mage blanc (100 points de vie, sort de soin)
            4 - un paladin (100 points de vie, sort de soin & attaque puissante)
            0 - Quitter le jeu
            alors ? : """)

        try:
            choix = int(choix)
            break
        except ValueError:
            print('entrez un nombre svp. Recommencez...')

            
    # choisir la classe de notre personnage 
       

    if choix == 1:
        perso = Guerrier(nom,120,0,"épée en bois",20)
        print(perso)
        
    if choix == 2:
        perso = MageRouge(nom,100,100,"épée en bois",20)
        print(perso)
    
    if choix == 3:
        perso = MageBlanc(nom,100,100,"épée en bois",20)
        print(perso)
        
    if choix == 4:
        perso = Paladins(nom,100,100,"épée en bois",20)
        print(perso)
    if choix == 0:
        print("Merci d'avoir joué !!!")
        exit
        break
    if choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix != 0:
        print("Veuillez rentrer une valeur entre 0 et 4 ! Merci de recommencer")

        continue
    
    
 
    
#gestion des erreurs 
    
    while True:
        #étape 2 : choisir l'adversaire à attaquer 
        reponse = input("""qui voulez vous combattre? :
            1 - Jean le gobelin (75pv,armé d'un gourdin (15 dg) )         
            2 - Michel l'orc (100pv, armé d'une épée rouillée (20dg) )
            3 - Jacque le troll (200pv, armé d'une hache (30dg) )
            0 - Quitter le jeu
            alors ? : """)
        
        try:
            reponse = int(reponse)
            break
        except ValueError:
            print('entrez un nombre svp. Recommencez...')

      

# validation du méchant a attaquer 

    if reponse == 1:
        mechant = Personnage("Jean le gobelin",75,0,"Gourdin",15)
        print(perso)
        print(mechant)
    if reponse == 2:
        mechant = Personnage("Michel l'orc",100,0,"Epée rouillée",20)
        print(perso)
        print(mechant)
    if reponse == 3:
        mechant = Personnage("Jacque le troll",200,0,"Hache",30)
        print(perso)
        print(mechant)
    if reponse == 0:
        print("Merci d'avoir joué !!!")
        exit
        break
    if reponse != 1 and reponse != 2 and reponse != 3 and reponse != 0:
        print("Veuillez rentrer une valeur entre 0 et 3 ! Merci de recommencer depuis le menu personnage")

        continue
    
    
# étape 3 les choix en fonctions de notre classe 


    while perso.PdtVie != 0 or mechant.PdtVie != 0:
        
       
        if perso.PdtVie == 0 and mechant.PdtVie == 0:
            print("Egalité !")
        
        
       
        # Si on choisi la classe Guerrier
        
        if choix == 1:
            action = input("""Que voulez vous faire ?
            1 - Attaquer
            2 - Changer d'arme ( Epée ( 45 dgt ))
            3 - Attaque puissante ( DgtArme*1.5 )
            Alors ? : """)

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
            if action == 2:
                mechant.Attaque(perso)
                perso.Arme= Arme("Epée",45)
                print(perso)
                print(mechant)
            if action == 3:
                perso.attaquePuissante(mechant)
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action != 1 and action != 2 and action != 3:
                print("Veuillez rentrer une valeur entre 1 et 3 !")

                continue
            if mechant.PdtVie <= 0:

                print("Il est mort, bravo!")
                break
            if perso.PdtVie <= 0:

                    print("W A S T E D")
                    break
          
            continue
            

        # si on choisi la classe MageRouge
        
        if choix == 2:
            action = input("""Que voulez vous faire ?
            1 - Attaquer 
            2 - Changer d'arme ( Epée ( 45 dgt ))
            3 - Méditer ( +40 Mana )
            4 - Lancer une boule de feu (-60 Mana )
            Alors ? : """)
            
            while True:

                try:
                    action = int(action)
                    break
                except ValueError:

                    break

            
            if action == 1:
                perso.Attaque(mechant)
                mechant.Attaque(perso)
                print(perso)
                print(mechant)

            if action == 2:
                mechant.Attaque(perso)
                perso.Arme = Arme("Epée",45)
                print(perso)
                print(mechant)
            if action == 3:
                perso.RecevoirMana()
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action == 4:
                perso.bouleDeFeu(mechant)
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action != 1 and action != 2 and action != 3 and action != 4:
                print("Veuillez rentrer une valeur entre 1 et 4 !")
  
                continue
            if mechant.PdtVie <= 0:

                print("Il est mort, bravo!")
                break
            if perso.PdtVie <= 0:

                    print("W A S T E D")
                    break
            continue
        
        # si on choisi la classe MageBlanc
        
        if choix == 3:
            action = input("""Que voulez vous faire ?
            1 - Attaquer 
            2 - Changer d'arme ( Epée ( 45 dgt ))
            3 - Méditer (+40 Mana)
            4 - Soigner ( ( Vie*2 ) & ( Mana-35 ) )
            Alors ? : """)
            
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

            if action == 2:
                mechant.Attaque(perso)
                perso.Arme= Arme("Epée",45)
                print(perso)
                print(mechant)
            if action == 3:
                perso.RecevoirMana()
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action == 4:
                perso.Soigner()
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action != 1 and action != 2 and action != 3 and action != 4:
                print("Veuillez rentrer une valeur entre 1 et 4 !")

                continue
            if mechant.PdtVie <= 0:

                print("Il est mort, bravo!")
                break
            if perso.PdtVie <= 0:

                    print("W A S T E D")
                    break
            continue
        
        #si on choisi le paladin
        
        if choix == 4:
            action = input("""Que voulez vous faire ?
            1 - Attaquer 
            2 - Changer d'arme ( Epée ( 45 dgt ))
            3 - Méditer ( +40 Mana )
            4 - Soigner ( ( Vie*2 ) & ( Mana-35 ))
            5 - Attaque Puissante( DgtArme*1.5 )
            Alors ? : """)
            
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
            if action == 2:
                mechant.Attaque(perso)
                perso.Arme= Arme("Epée",45)
                print(perso)
                print(mechant)
            if action == 3:
                perso.RecevoirMana()
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action == 4:
                perso.Soigner()
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action == 5:
                perso.attaquePuissante(mechant)
                mechant.Attaque(perso)
                print(perso)
                print(mechant)
            if action != 1 and action != 2 and action != 3 and action !=4 and action != 5:
                print("Veuillez rentrer une valeur entre 1 et 5 !")

                continue
            if mechant.PdtVie <= 0:

                print("Il est mort, bravo!")
                break
            if perso.PdtVie <= 0:

                    print("W A S T E D")
                    break
            continue

#end game 
