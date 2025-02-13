from os import system
from time import sleep

def clear(secs):
  sleep(secs)
  system('cls')

clear(0)

def loadingScreen(cycle,msg):
  while cycle > 0:
    load = ['/ ','| ','\\ ','--']        
    for i in load:
      print(i,msg)
      clear(0.1)
    cycle -= 1

loadingScreen(0,'Loading')

tennisA = {'Character' : 'Tennis Mom | Attacker' , 'Health Points' : '10' , 'Normal Attack' : 'Deals 2 dmg' , 'Skill' : 'Deal 2 dmg. At the end of the round,deal 1 to all enemies' , 'Ultimate' : 'Normal Attacks will deal dmg towards all enemies.'}


for key, value in tennisA.items():
  print(key+':',value)

print()