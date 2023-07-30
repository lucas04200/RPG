#!/Users/Ldech/AtelierAlgo/DM_RPG/arme.py
# -*-coding:Utf-8 -*



class Arme():
    
    def __init__(self, NomArme="Epée en bois",DgtArme=10):
        self._NomArme = NomArme
        self._DgtArme = DgtArme

    def GetNomArme(self):
        #getter de NomArme
        return self._NomArme 

    def SetNomArme(self, NomArme):
        #setter de NomArme
        self._NomArme = NomArme
    NomArme = property(GetNomArme, SetNomArme)

    def GetDgtArme(self):
        #getter de DgtArme
        return self._DgtArme
    
    def SetDgtArme(self, DgtArme):
        #setter de DgtArme 
        self._DgtArme = DgtArme
    DgtArme = property(GetDgtArme,SetDgtArme)

    def ChangerArme(self,NomArme,DgtArme):
        # pouvoir permettre au personnage que l'on souhaite de changer d'arme
        self._NomArme = NomArme
        self._DgtArme = DgtArme


    def __repr__(self):
        return """{} - Classe : Personnage 
        {} - point de vie, {} - Mana,
        {} - Arme ({} dégât de cette arme) 
        """.format(self._nom, self._PdtVie, self._Mana,  self._NomArme,self._DgtArme)
 
