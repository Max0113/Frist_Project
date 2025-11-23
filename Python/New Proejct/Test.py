class Base_Donne:
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
            print("Client supprimé avec succès !")
        else:
            print("ID non trouvé.")

x = Base_Donne()
x.Afficher_clients()
x.Remove_clients()
x.Afficher_clients()