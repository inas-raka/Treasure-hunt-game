import time
import sys
blah = "Dear traveller...\n You have stepped into the eagles domain\n You must naviagte around a series of mazes\n Along the way you will find items treasure or... your worst enemy\n Be careful of your next step\n"
for l in blah:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.0000001)

class person:
    def __init__ (self,name)

map_selection=input("please enter which territory you would like to claim back first\n to expand Shqipria please enter [1] \n to get back Dardania please enter [2] \n To conquer Ilirdia please enter [3]\n To bring back Mal I Zi please enter [4]\n To conquer Cameria please press [5]")
if map_selection==1:
    map=print("Welcome to Shqipria\n Be carefull\n Here you can find swords,helmets but also guards!\n You will first face Kruje then move onto the centre Tirana")