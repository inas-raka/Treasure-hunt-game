import time
import sys

print('''
 *******************************************************************************
           |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
 |                   |  ,-"_,=""     `"=.|                  |
 |___________________|__"=._o`"-._        `"=.______________|___________________
           |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
 ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 /______/______/______/______/______/______/______/______/______/______/_____ /
 *******************************************************************************
 ''')

blah = "Dear traveller...\n You have stepped into the eagles domain\n You must naviagte around a series of mazes\n Along the way you will find items treasure or... your worst enemy\n Be careful of your next step"
for l in blah:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.02)

choice=input("You will now have the choice of 4 classes\n [1]Archer class - grants you 1 bow and 5 arrows\n[2]Mele class - grants you 1 sword \n[3]Healer class\n[4]Defence class\nSelect your class: ")
if choice==1:
    player_inventory.add_item("Bow", 1)
    player_inventory.add_item("Arrows", 5)
if choice==2:
    player_inventory.add_item("Sword", 1)
if choice==3:
    player_inventory.add_item("Healing potion", 2)
if choice==4:
    player_inventory.add_item("Shield", 1)
    player_inventory.add_item("Helmet", 1)

class Player():
    def __init__(self, given_name,given_setup):
        self.name = given_name
        self.setup=given_setup
        self.health = 100
        self.energy = 100
        self.inventory_max_weight = 50
        self.inventory = []
      
    def calculate_inventory_size(self):
        # write code here

        map_selection=input("please enter which territory you would like to claim back first\n to expand Shqipria please enter [1] \n to get back Dardania please enter [2] \n To conquer Ilirdia please enter [3]\n To bring back Mal I Zi please enter [4]\n To conquer Cameria please press [5]")
        if map_selection==1:
            map=print("Welcome to SHQIPRIA\n Be carefull\n Here you can find SWORDS,HELMETS but also GUARDS!\n You will first face KRUJE then move onto the centre TIRANA")
        if map_selection==2:
            map=print("Welcome to DARDANIA\n Be carefull\n Here you can find AXES,CHESTPLATES but also REBELS!\n You will first face the city of KACANIK then move onto the centre PRISHTINA")
        if map_selection==3:
            map=print("Welcome to ILIRDIA\n Be carefull\n Here you can find BOWS,LEGGINGS but also EVIL POLICE!\n You will first face KUMANOVO then move onto the centre SHKUP")
        if map_selection==4:
            map=print("Welcome to MAL I ZI\n Be carefull\n Here you can find MACES,BOOTS but also HYENAS!\n You will first face the beaches of ULQIN then move onto the centre BUDVA")
        if map_selection==5:
            map=print("Welcome to CAMERIA\n Be carefull\n Here you can find SPEARS,SHIELDS but also THIEVES!\n You will first face LELOVA then move onto the centre KONSIPOL")
        