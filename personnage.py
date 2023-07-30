#!/Users/Ldech/AtelierAlgo/DM_RPG/personnage.py
# -*-coding:Utf-8 -*


from arme import Arme


class Personnage():
    

    def __init__(self,nom,PdtVie=100, Mana=0,NomArme="Epée en bois",DgtArme=10):
        self._nom = nom 
        self._PdtVie = PdtVie 
        self._Mana = Mana
        self.Arme = Arme(NomArme, DgtArme)


    def GetNom(self):
        #prendre le nom du perso
        return self._nom

    def SetNom(self, nom):
        self._nom = nom
    nom = property(GetNom, SetNom)

    def GetPdtVie(self): 
        #getter de PdtVie
        return self._PdtVie 



    def SetPdtVie(self, PdtVie):
        #setter de PdtVie
        self._PdtVie = PdtVie
    PdtVie = property(GetPdtVie,SetPdtVie)
    
    def GetMana(self):
        #getter de Mana 
        return self._Mana

        
    def SetMana(self, Mana):
        #setter de Mana
        self._Mana = Mana
    Mana = property(GetMana,SetMana)

    def Mana_max(self):

        if self._Mana < 100:
            return True
        else:
            
            return False


    def RecevoirDegat(self, DgRecu):
        #recevoir des dégâts et perdre de la vie
        self._PdtVie = self._PdtVie - DgRecu
        if self._PdtVie < 0:
            self._PdtVie = 0
        
    
    def Attaque(self,nom):
        #infliger des attaques à un autre personnage 
        
        nom.RecevoirDegat(self.Arme.DgtArme)
    
                
    def EstVivant(self):
        #indique si le personnage est encore en vie ou non
        if self.PdtVie > 0:
            return True
        else:
            return False



    def __repr__(self):
        return """
        {} - Classe : Personnage 
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
        """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)
 
class Guerrier(Personnage):

    def attaquePuissante(self,nom):
        nom.RecevoirDegat(round(self.Arme.DgtArme*1.5))

    def __repr__(self):
        return """
        {} - Classe : Guerrier
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
        """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)

class Magicien(Personnage):
    
    def __init__(self,nom,PdtVie=100, Mana=100,NomArme="Epée en bois",DgtArme=10):
        self._nom = nom 
        self._PdtVie = PdtVie 
        self._Mana = Mana
        self.Arme = Arme(NomArme, DgtArme)
    
    def RecevoirMana(self):
        #recevoir des dégâts et perdre de la vie
        if self._Mana < 0:
            self._Mana = 0
        self._Mana = self._Mana + 40
        if self._Mana > 100:
            print("votre mana ne peux pas dépasser 100")
            self._Mana = 100
    
    def __repr__(self):
        return """
        {} - Classe : Magicien 
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
        """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)



class MageBlanc(Magicien):

    def Soigner(self):
        if self._Mana < 35:
            print("pas assez de Mana pour le sort")
        else:
            self._PdtVie = self._PdtVie * 2
        if self._PdtVie > 100:
            self._PdtVie = 100
        if self._PdtVie < 0:
            self._PdtVie = 0

        self.Mana = self._Mana - 35
        if self._Mana < 0:
            self._Mana = 0
    
    def __repr__(self):
        return """
        {} - Classe : Mage Blanc
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
        """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)

class MageRouge(Magicien):

    def bouleDeFeu(self, nom):
        
        if self._Mana < 65:
            print("pas assez de Mana pour le sort")
        else:
            nom.RecevoirDegat(60)

        
        self._Mana = self._Mana - 65
        if self._Mana < 0:
            print("vous n'avez plus de mana")
            self._Mana = 0
        
    def __repr__(self):
        return """
        {} - Classe : Mage Rouge
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
    """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)

class Paladins(Guerrier,MageBlanc):
    
    def __repr__(self):
        return """
        {} - Classe : Paladins
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
    """.format(self._nom, self._PdtVie, self._Mana,  self.Arme.NomArme,self.Arme.DgtArme)















if __name__ == "__main__":   # les actions
    joueur = Personnage("Bob", 120)
    monstre1 = Personnage("Grunt le gobelin")
    monstre2 = Personnage("Gruik l’orc")
    monstre1.Attaque(joueur)
    monstre2.Attaque(joueur)
    joueur.Arme.ChangerArme("Tronçonneuse", 55)
    monstre1.Attaque(joueur)
    monstre2.Attaque(joueur)
    joueur.Attaque(monstre1)
    monstre2.Attaque(joueur)
    joueur.Attaque(monstre1)
   


    print(joueur)
    print(monstre1)
    print(monstre2)
    print(joueur.EstVivant())
    print(monstre1.EstVivant())
    print(monstre2.EstVivant())




