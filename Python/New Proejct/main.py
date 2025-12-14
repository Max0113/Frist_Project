from os import system


def clear():
    """Clear the console screen."""
    system("cls")


class Login:
    """
    Class to manage user login with username and password verification.
    """

    def __init__(self):
        self.username = ""
        self.password = ""

    def verify_username(self, valid_usernames):
        """
        Prompt for username and verify if it is in the list of valid usernames.
        :param valid_usernames: List of allowed usernames (case insensitive).
        :return: True if username is valid, False otherwise.
        """
        self.username = input("Enter your Username: ").lower()
        return self.username in valid_usernames

    def verify_password(self, valid_passwords):
        """
        Prompt for password and verify if it is in the list of valid passwords.
        :param valid_passwords: List of allowed passwords.
        :return: True if password is valid, False otherwise.
        """
        self.password = input("Enter your Password: ")
        return self.password in valid_passwords


class Menu:
    """
    Class for displaying menus and capturing user choices.
    """

    def main_menu(self):
        """Display the main menu and return the user's choice as a string."""
        print("""
        ======================================
                         Main Menu
        ======================================
          1- Client Management
          2- Employee Management
          3- Money Management
          4- File Management
          5- Quit
        """, end="")
        while True:
            choice = input("Enter your choice: ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def clients_menu(self):
        """Display the client management menu and return user choice."""
        print("""
        ======================================
                       Clients Menu
        ======================================
          1- Add a client
          2- Remove a client
          3- Return to main menu
        """, end="")
        while True:
            choice = input("Enter your choice: ")
            if choice in ['1', '2', '3']:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def employees_menu(self):
        """Display the employee management menu and return user choice."""
        print("""
        ======================================
                      Employees Menu
        ======================================
          1- Add an employee
          2- Remove an employee
          3- Employee Salary
          4- Employee Points
          5- Return to main menu
        """, end="")
        while True:
            choice = input("Enter your choice: ")
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def files_menu(self):
        """Display the file management menu and return user choice."""
        print("""
        ======================================
                       File Menu
        ======================================
          1- Employee data
          2- Client data
          3- Bounce money

        """, end="")
        choice = input("Enter your choice: ")
        return choice


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
              2- Gestion des Employe
              3- Gestion des Monye
              4- Gestion des fichier
              5- Quit
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
              4- les argen de Bounce

        """,end="")
        x = input("      Entrer choix : ")
        return x
        
class BD_clients :
    def __init__(self):
        self.clients = [["D00", "D01", "D02"], ["Younes", "Amin", "Ahmed"], [1200, 2333, 2133]]
    
    def Afficher_clients(self):
        print("\t |   ID   |     Name     |      Argen    |")
        print("\t----------------------------------------------")
        for i in range(len(self.clients[0])):  # parcourir par index
            id_client = self.clients[0][i]
            name_client = self.clients[1][i]
            argent_client = self.clients[2][i]
            print(f"\t |  {id_client:^4}   | {name_client:^12} |  {argent_client:^10}  |")
    
    def Add_clients(self) :
        id = input("Entrer Id :")
        name = input("Entrer name :")
        argen = float(input("Entrer argen :"))
        self.clients[0].append(id)
        self.clients[1].append(name)
        self.clients[2].append(argen)

    def Remove_clients(self) :
        id_client = input("Entrer l'ID du client à supprimer : ")
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
    
    def Somme_Argon(self) :
        argent_client = 0
        for i in range(len(self.clients[0])):  # parcourir par index
            argent_client += self.clients[2][i]
        return argent_client



class BD_Employ :
    def __init__(self):
        self.Employ = [["D00", "D01", "D02"], ["mohamed", "yasune", "max"], ["amzil", "borase", "londry"],["mohamed@gmail.com","mohamed@gmail.com","max@gmail.com"], [1200.0, 2333.0, 2133.0], [12.0, 0.0, -3.0]]
    
    def Afficher_Employ(self):
        print("\t |  ID  |     Name     |     Prénom    |       gmail       |     Argen     |     Pointer    |")
        print("\t ---------------------------------------------------------------------------------------------")
        for i in range(len(self.Employ[0])):  # parcourir par index
            id_Employ = self.Employ[0][i]
            name_Employ = self.Employ[1][i]
            Prénom_Employ = self.Employ[2][i]
            gmail_Employ = self.Employ[3][i]
            argent_Employ = self.Employ[4][i]
            Points_Employ = self.Employ[5][i]
            print(f"\t |  {id_Employ}   | {name_Employ:^12} |  {Prénom_Employ:^10}  |  {gmail_Employ:^15}  |  {argent_Employ:^10} |  {Points_Employ:^10}  |")
    
    def Add_Employ(self) :
        id = input("Entrer Id :")
        name = input("Entrer name :")
        Prénom = input("Entrer Prénom :")
        gmail = input("Entrer Gmail :")
        argen = float(input("Entrer argen :"))
        Points = float(input("Entrer Pointer :"))
        self.Employ[0].append(id)
        self.Employ[1].append(name)
        self.Employ[2].append(Prénom)
        self.Employ[3].append(gmail)
        self.Employ[4].append(argen)
        self.Employ[5].append(Points)

    def Remove_Employ(self) :
        id_client = input("Entrer l'ID du client à supprimer : ")
        if id_client in self.Employ[0]:
            index = self.Employ[0].index(id_client)
            # Supprimer le client
            for i in range(6) :
                self.Employ[i].pop(index)
            clear()
            print("Employé supprimé avec succès !")
        else:
            print("ID non trouvé.")

class System_Bounce :
    def __init__(self):
        self.Menu = Menu()
        self.LogoIN = LogoIN()
        self.BD_clients = BD_clients()
        self.BD_Employ = BD_Employ()
    
    def start_sys(self) :
        while True :
            V1 = self.LogoIN.Verife_Usernam(["youness","max"])
            V2 = self.LogoIN.Verife_Password(["123456","56780"])
            if V1 and V2 :
                clear()
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
            elif CH == 2:
                clear()
                self.BD_Employ.Afficher_Employ()
                CH1 = int(self.Menu.Menu_Employe())
                if CH1 == 1:
                    self.BD_Employ.Add_Employ()
                elif CH1 == 2:
                    self.BD_Employ.Remove_Employ()
                elif CH1 == 3:
                    clear()
                    continue
            
            elif CH == 3: 
                clear()
                print("la Bounce :",self.BD_clients.Somme_Argon(),"$")
                CH3 = input("Quit ou No :")
                if CH3.upper() == "NO" :
                    clear()
                    continue
                else :
                    quit()
            
            else :
                quit()
        
        def GestionMone(self) :
            pass

        
x = System_Bounce()
x.start_sys()