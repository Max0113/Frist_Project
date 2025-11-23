from tkinter import *
from os import *


def clear() :
    system("cls")


class LogoIN :
    def __init__(self):
         self.Usernam = ""
         self.Password = ""

    def Verife_Usernam(self, T):
        self.Usernam = input("Entre votre Username : ").lower()
        return self.Usernam in T

    def Verife_Password(self, P):
        self.Password = input("Entre votre Password : ")
        return self.Password in P


class Menu :
    def Menu_Pr(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- Gestion des clients
              4- Gestion des Monye
              5- Gestion des fichier
              6- Quit
        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_Pr_chaf(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- Gestion des clients
              2- Gestion des clients VIP
              3- Gestion des Employe
              4- Gestion des Monye
              5- Gestion des fichier
              6- Quit
        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_clients(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- Ajout une clients
              2- remove une clients
              3- return a Menu_Pr
        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_clients_VIP(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- Ajout une clients
              2- remove une clients
              3- return a Menu_Pr
        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_Employe(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- Ajout une Employe
              2- remove une Employe
              3- saler de une Employe
              4- points de une Employe
              5- return a Menu_Pr
        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_ficher(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- les donne de Employe
              2- les donne de clients
              3- les argen de Bounce

        """,end="")
        x = input("      Entrer choix : ")
        return x
    
    def Menu_ficher_chef(self) :
        print("""
            ======================================
                             Menu
            ======================================
              1- les donne de Employe
              2- les donne de clients
              3- les donne de clientsVIP
              4- les argen de Bounce

        """,end="")
        x = input("      Entrer choix : ")
        return x
        
class BD_clients :
    def __init__(self):
        self.clients = [[1, 2, 3], ["Younes", "Amin", "Ahmed"], [1200, 2333, 2133]]
    
    def Afficher_clients(self):
        print(" |  ID  |     Name     |     Argen    |")
        print("----------------------------------------")
        for i in range(len(self.clients[0])):  # parcourir par index
            id_client = self.clients[0][i]
            name_client = self.clients[1][i]
            argent_client = self.clients[2][i]
            print(f" |  {id_client}   | {name_client:^12} |  {argent_client:^10}  |")
    
    def Add_clients(self) :
        id = int(input("Entrer Id :"))
        name = input("Entrer name :")
        argen = float(input("Entrer argen :"))
        self.clients[0].append(id)
        self.clients[1].append(name)
        self.clients[2].append(argen)

    def Remove_clients(self) :
        id_client = int(input("Entrer l'ID du client à supprimer : "))
        if id_client in self.clients[0]:
            index = self.clients[0].index(id_client)
            # Supprimer le client
            self.clients[0].pop(index)
            self.clients[1].pop(index)
            self.clients[2].pop(index)
            clear()
            print("Client supprimé avec succès !")
        else:
            print("ID non trouvé.")

class BD_clientsVIP :
    def __init__(self):
        self.clientsVIP = [[1, 2, 3], ["Younes", "Amin", "Ahmed"], [1200, 2333, 2133]]
    
    def Afficher_clientsVIP(self):
        print(" |  ID  |     Name     |     Argen    |")
        print("----------------------------------------")
        for i in range(len(self.clientsVIP[0])):  # parcourir par index
            id_client = self.clientsVIP[0][i]
            name_client = self.clientsVIP[1][i]
            argent_client = self.clientsVIP[2][i]
            print(f" |  {id_client}   | {name_client:^12} |  {argent_client:^10}  |")
    
    def Add_clientsVIP(self) :
        id = int(input("Entrer Id :"))
        name = input("Entrer name :")
        argen = float(input("Entrer argen :"))
        self.clientsVIP[0].append(id)
        self.clientsVIP[1].append(name)
        self.clientsVIP[2].append(argen)

    def Remove_clientsVIP(self) :
        id_client = int(input("Entrer l'ID du client à supprimer : "))
        if id_client in self.clientsVIP[0]:
            index = self.clientsVIP[0].index(id_client)
            # Supprimer le client
            self.clientsVIP[0].pop(index)
            self.clientsVIP[1].pop(index)
            self.clientsVIP[2].pop(index)
            clear()
            print("Client supprimé avec succès !")
        else:
            print("ID non trouvé.")

class BD_Employ :
    def __init__(self):
        self.Employ = [[1, 2, 3], ["mohamed", "yasune", "max"], ["amzil", "borase", "londry"], [1200, 2333, 2133], [12, 0, -3]]
    
    def Afficher_Employ(self):
        print(" |  ID  |     Name     |     Prénom    |     Argen     |     Pointer    |")
        print("----------------------------------------")
        for i in range(len(self.Employ[0])):  # parcourir par index
            id_client = self.Employ[0][i]
            name_client = self.Employ[1][i]
            Prénom_client = self.Employ[2][i]
            argent_client = self.Employ[3][i]
            Points_client = self.Employ[4][i]
            print(f" |  {id_client}   | {name_client:^12} |  {Prénom_client:^10}  |  {argent_client:^10}$ |  +{Points_client:^10}  |")
    
    def Add_Employ(self) :
        id = int(input("Entrer Id :"))
        name = input("Entrer name :")
        Prénom = input("Entrer Prénom :")
        argen = float(input("Entrer argen :"))
        Points = float(input("Entrer Pointer :"))
        self.Employ[0].append(id)
        self.Employ[1].append(name)
        self.Employ[2].append(Prénom)
        self.Employ[3].append(argen)
        self.Employ[4].append(Points)

    def Remove_Employ(self) :
        id_client = int(input("Entrer l'ID du client à supprimer : "))
        if id_client in self.Employ[0]:
            index = self.Employ[0].index(id_client)
            # Supprimer le client
            self.Employ[0].pop(index)
            self.Employ[1].pop(index)
            self.Employ[2].pop(index)
            self.Employ[3].pop(index)
            self.Employ[4].pop(index)
            clear()
            print("Client supprimé avec succès !")
        else:
            print("ID non trouvé.")

class System_Bounce :
    def __init__(self):
        self.Menu = Menu()
        self.LogoIN = LogoIN()
        self.BD_clients = BD_clients()
        self.BD_clientsVIP = BD_clientsVIP()
        self.BD_Employ = BD_Employ()
    
    def start_sys(self) :
        while True :
            V1 = self.LogoIN.Verife_Usernam(["youness","max"])
            V2 = self.LogoIN.Verife_Password(["123456","56780"])
            if V1 and V2 :
                print("Login Success \n")
                self.part1()
            else : 
                print("Verfie ton Password or Usernam !!")
    
    def part1(self):
        while True:   # boucle menu principal
            CH = int(self.Menu.Menu_Pr())

            # Gestion des clients
            if CH == 1:
                clear()
                self.BD_clients.Afficher_clients()
                CH1 = int(self.Menu.Menu_clients())
                if CH1 == 1:
                    self.BD_clients.Add_clients()
                elif CH1 == 2:
                    self.BD_clients.Remove_clients()
                elif CH1 == 3:
                    clear()
                    continue

            # Quitter
            elif CH == 6:
                print("Bye 👋")
                exit()

        
x = System_Bounce()
x.start_sys()