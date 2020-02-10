#!/usr/bin/env python3
"""
      TASK - Print to screen a fortune
        TODO (Primary Path)
        1. Ask for users name
        2. print to screen a Basic valentines greeting for someone special
"""

__author__  = "Karim Saleh"
__email__   = "karimmoustafasaleh@gmail.com"
__licence__ = "The Unlicense"
__version__ = "12.0" 
__date__ = "2020-2-6"

import os
import arabic_new
import arabic_new_all
import english
import english_all
import hijab
import hijab_all
import friends
import friends_all
import theOffice 
import theOffice_all
import himym
import himym_all
import bbad
import bbad_all

print("\033[1;35;48mAloha there ❤️️️️️️️️ ️️️️️️️❤️️️️️️️️ ❤️️️️️️️️ ️️️️️️️❤️️️️️️️️"
      "\nFriendly message from my creator"
      "\nTo whom received the link to this abstract" 
      "\n,this is for you, Hope you have a" 
      "\nJolly Valentines ~ the creator"
      "\n \033[0m ")


def loop():
  while True:
    try:
      print("\n",name,"Please choose a category ❤️" 
      "\nBy simply typing a number that"
      "\ncorresponds with an option and pressing""\nreturn :)"
      "\n"
      "\nArabic                   - 1" 
      "\nEnglish                  - 2" 
      "\nHalal                    - 3" 
      "\nFriends TV               - 4" 
      "\nThe Office TV            - 5"
      "\nHow I Met Your Mother TV - 6"
      "\nBreaking Bad TV          - 7") 
      inp = int(input())
      if inp == 1:
        os.system('clear')
        print("\n"+"\n"+name+"\n"+arabic_new.valentine_tellings())
        break

      elif inp == 2:
        os.system('clear')
        print("\n"+"\n"+name+"\n"
        +english.valentine_tellings())
        break

      elif inp == 4: 
        os.system('clear')
        print("\n"+"\n"+name+"\n"
        +friends.valentine_tellings())
        break

      elif inp == 3:
        os.system('clear')
        print("\n"+"\n"+name+"\n"
        +hijab.valentine_tellings())
        break

      elif inp == 5:
        os.system('clear')
        print("\n"+"\n"+name+"\n"+theOffice.valentine_tellings())
        break

      elif inp == 6:
        os.system('clear')
        print("\n"+"\n"+name+"\n"+himym.valentine_tellings())
        break

      elif inp == 7:
        os.system('clear')
        print("\n"+"\n"+name+"\n"+bbad.valentine_tellings())
        break

      elif inp == 110:
        os.system('clear')
        print(arabic_new_all.valentine_tellings())
        break

      elif inp == 220:
        os.system('clear')
        print(english_all.valentine_tellings())
        break

      elif inp == 330:
        os.system('clear')
        print(hijab_all.valentine_tellings())
        break

      elif inp == 440:
        os.system('clear')
        print(friends_all.valentine_tellings())
        break

      elif inp == 550:
        os.system('clear')
        print(theOffice_all.valentine_tellings())
        break

      elif inp == 660:
        os.system('clear')
        print(himym_all.valentine_tellings())
        break

      elif inp == 770:
        os.system('clear')
        print(bbad_all.valentine_tellings())
        break

      else:
        print(name, " Please choose a category ❤️")
    except ValueError:
      os.system('clear')
      print(name +  "\033[1;31;48m" + "\nPlease select one of the categories"+"\nhoney pie ❤️️️️️️️️"+"\033[0m")

name = input("Please insert your name honey pie ❤️\n")
os.system('clear')
loop()

while True:
  print("\n\nAnother? y/n")
  ins = input()

  if ins.lower() == "y":
    os.system('clear')
    loop()

  elif ins.lower() == "n":
    break

  else:
    print("Enter y or n")
