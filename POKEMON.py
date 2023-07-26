
import time
import numpy as np
import sys


def delay_print(s):
    
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, nom, types, moves, EVs, health='00000000000000000000'):
        
        self.nom = nom
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTAQUE']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 


    def fight(self, Pokemon2):
        
        print("!-----COMBAT POKEMON-----!")
        print(f"\n{self.nom}")
        print("TYPE/", self.types)
        print("ATTAQUE/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.nom}")
        print("TYPE/", Pokemon2.types)
        print("ATTAQUE/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        #Avantages de types

        version = ['Feu', 'Eau', 'Plante']
        for i,k in enumerate(version):
            if self.types == k:
                # Les deux du même type
                if Pokemon2.types == k:
                    string_1_attack = '\nAttaque pas très efficace...'
                    string_2_attack = '\nAttaque pas très efficace...'

                # Pokemon2 Fort
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nAttaque pas très efficace...'
                    string_2_attack = '\nAttaque très efficace!'

                # Pokemon2 Faible
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nAttaque très efficace!'
                    string_2_attack = '\nAttaque pas très efficace...'


        # Tant que les pokemons ont de la vie
        while (self.bars > 0) and (Pokemon2.bars > 0):

            # Print la vie de chaque pokemon
            print(f"\n{self.nom}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.nom}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.nom}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.nom} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determiner les damages
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Ajouter des barres de vie
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "0"

            time.sleep(1)
            print(f"\n{self.nom}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.nom}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Regarde si le pokemon est mort
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.nom + ' est KO.')
                break

            #  Tour du Pokemon2

            print(f"Go {Pokemon2.nom}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.nom} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determiner les damages
            self.bars -= Pokemon2.attack
            self.health = ""

            #Ajouter des barres de vie
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "0"

            time.sleep(1)
            print(f"{self.nom}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.nom}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.nom + ' est KO.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Feu', ['Lance Flamme', 'Vol', 'Brûlure', 'Poing de feu'], {'ATTAQUE':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Eau', ['Pistolet d eau', 'Bulles d eau', 'Cascade', 'Surf'],{'ATTAQUE': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Plante', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTAQUE':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Feu', ['Ember', 'Scratch', 'Tackle', 'Poing de feu'],{'ATTAQUE':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Eau', ['Bulles d eau', 'Tackle', 'Headbutt', 'Surf'],{'ATTAQUE': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Plante', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTAQUE':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Feu', ['Ember', 'Scratch', 'Flamethrower', 'Poing de feu'],{'ATTAQUE':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Eau', ['Bulles d eau', 'Pistolet d eau', 'Headbutt', 'Surf'],{'ATTAQUE': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Plante', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTAQUE':4, 'DEFENSE':6})


    Charizard.fight(Blastoise) 