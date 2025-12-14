import os

class Menu :
    def Menu_Principale(self) :
        print("""
1. Ajouter un étudiant
2. Afficher tous les étudiants
3. Calculer la moyenne d’un étudiant
4. Afficher l’étudiant ayant la meilleure moyenne
5. Quitter """)
        CH = int(input("Votre Choix (1-5):"))
        while CH < 1 or CH > 5 :
            print("Error (1-5) !!")
            CH = int(input("Votre Choix (1-5) :"))
        return CH   
    
class DataBase:
    def __init__(self):
        self.Data_Etudent = [
            {"nom": "Ahmed", "age": 12, "notes": [12, 9, 18]},
            {"nom": "Yassen", "age": 16, "notes": [14, 12.2, 20]}
        ]

    def Ajout_Etudent(self):
        print("_________ Ajouter un étudiant _________")
        nom = input("Entrer le nom : ")
        age = int(input("Entrer l'âge : "))
        n1 = float(input("Note 1 : "))
        n2 = float(input("Note 2 : "))
        n3 = float(input("Note 3 : "))
        while not (0 <= n1 <= 20 and 0 <= n2 <= 20 and 0 <= n3 <= 20):
              print("Les notes doivent être entre 0 et 20 ❌")
              n1 = float(input("Note 1 : "))
              n2 = float(input("Note 2 : "))
              n3 = float(input("Note 3 : "))

            

        self.Data_Etudent.append({
            "nom": nom,
            "age": age,
            "notes": [n1, n2, n3]
        })

    def Afficher_Etudent(self):
        print("_________ Liste des étudiants _________")
        for e in self.Data_Etudent:
            print(f"Nom : {e['nom']}")
            print(f"Age : {e['age']}")
            print(f"Notes : {e['notes']}")
            print("-" * 30)

    def Calcule_Moyenne(self) :
        while True :
            nom = input("Entrer le nom de l'étudiant : ")

            for e in self.Data_Etudent:
                if nom.lower() == e['nom'].lower() :
                   moyenne = sum(e['notes']) / len(e['notes'])
                   print(f"Moyenne de {e['nom']} : {moyenne:.2f}")
                   return  0
            print("Étudiant introuvable ❌")
    
    def meilleure(self) :
        list_Name = []
        list_Moyenne = []
        for e in self.Data_Etudent:
            moyenne = sum(e['notes']) / len(e['notes'])
            list_Name.append(e['nom'])
            list_Moyenne.append(moyenne)
        moyenne_max = max(list_Moyenne)
        print(f"meilleure est {list_Name[list_Moyenne.index(moyenne_max)]}({moyenne_max})")

                                
class App :
    def __init__(self):
        self.Menu = Menu()
        self.DataBase = DataBase()
    
    def Start_App(self) :
        while True :
            CH = int(self.Menu.Menu_Principale())
            if CH == 1 :
                self.DataBase.Ajout_Etudent()
            elif CH == 2 :
                self.DataBase.Afficher_Etudent()
            elif CH == 3 :
                self.DataBase.Calcule_Moyenne()
            elif CH == 4 :
                self.DataBase.meilleure()
            else :
                quit()
            
            CH2 = input("Tu veux returen a Menu (Y-N) !!")
            if CH2.lower()  == 'y' :
                os.system("cls")
                continue
            elif CH2.lower()  == 'n' :
                quit()


C = App()
C.Start_App()