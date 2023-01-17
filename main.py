#Crée par Chamuel Munoz
#Exercice POO2
#date: 16-01-2023

from random import randint

def lancer_de():
    randint(1,6)
def des():
    list = [lancer_de(), lancer_de(), lancer_de(), lancer_de()] #on crée une liste avec 4 objects qui ont une valeur aleatoire entre 1 et 6
    x = min(list) #on identifie le plus petit ds objects et on l'elimine
    self.list.remove(x)
    return sum(list)

class NPC():
    def __init__(self):
        self.force = des()
        self.agilite = des()
        self.constitution = des()
        self.intelligence = des()
        self.sagesse = des()
        self.charisme = des()
        self.armure = randint(1,12)
        self.nom = str
        self.race = str
        self.espece = str
        self.vie = randint(1,20)
        self.job = str
    def affiche(self):
        print(f'''
        force : {self.force} 
        agilite : {self.agilite} 
        constution : {self.constitution} 
        intelligence : {self.intelligence} 
        sagesse :{self.sagesse}  
        charisme : {self.charisme}  
        armure :{self.armure} 
        nom :{self.nom} 
        race :{self.race} 
        espece : {self.espece}
        vie : {self.vie}
        proffesion:{self.job}
        ''')

class kobold(NPC):
    def attaque(self, npc):
        dommage_f = lancer_de()
        npc.vie = npc.vie - dommage_f

    def dommage_subis(self, dommage_s):
        self.vie = self..vie - dommage_s

class hero(NPC):
    def attaque(self, npc):
        dommage_f = lancer_de()
        npc.vie = npc.vie - dommage_f

    def dommage_subis(self, dommage_s):
        self.vie = self.vie - dommage_s





