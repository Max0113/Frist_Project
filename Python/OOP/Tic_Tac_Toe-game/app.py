import os

def clear_wind() :
    os.system("cls")

class Player :
    def __init__(self):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self) :
        while True :
            name = input ("entre your name player : ")
            if name.isalpha() :
               self.name = name
               break
            print("Invalid name. plase use letters only .")

    def choose_symbol(self) :
        while True :
            symbol = input (f"player {self.name} entre your symbol : ")
            if symbol.isalpha() and len(symbol) == 1 :
               self.symbol = symbol.upper()
               break
            print("Invalid name. plase use a single letters .")

class Menu :
    def start_main(self) :
        x = """
          welcome to my X-0 game
          1 - Start Game
          2 - Quit Game
          entrer your choose 1 et 2 : """
        choose = int(input(x))
        return choose
    
    def End_main(self) :
        x = """
          Game OVER!!
          1 - restart Game
          2 - Quit Game
          entrer your choose 1 et 2 : """
        choose = int(input(x))
        return choose
    
class Board :

    def __init__(self):
        self.borad = []
        for i in range(1,10) :
            self.borad.append(str(i))
    
    def display_board(self) :
        for i in range(0,9,3) :
            print('|'.join(self.borad[i:i+3]))
            if i < 6 :
                print("-"*10)
        
    def updata_board(self , choice , symbol) :
        if self.is_valid_move(choice) :
            self.borad[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self , choice) :
        return self.borad[choice - 1].isdigit()
    
    def rest_board(self) :
        self.borad = []
        for i in range(1,10) :
            self.borad.append(str(i))

class Game() :
    def __init__(self):
        self.player = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self) :
        choice = self.menu.start_main()
        if choice == 1 :
            self.setup_game()
            self.play_game()
        else :
            self.Quit_game()

    def setup_game(self) :
        for Number , player in enumerate(self.player) :
            print(f"Player {Number + 1} : ")
            player.choose_name()
            player.choose_symbol()
            print('-'*20)
            # clear_wind()

    def play_game(self) :
        while True :
            self.play_turn() 
            if self.check_win() or  self.check_draw() :
                choise = self.menu.End_main()
                if choise == 1 :
                    self.rest_game()
                else :
                    self.Quit_game()
                    break

    def play_turn(self) :
        player = self.player[self.current_player_index] 
        self.board.display_board()
        print (f" {player.name}'s start playing ({player.symbol})")
        while True :
            try:
                cell_player = int(input("enter number of place (1-9) : "))
                if  1 <= cell_player <= 9 and self.board.updata_board(cell_player , player.symbol) :
                    break
                else :
                    print("enter une number enter 1-9")
            except ValueError :
                print("An error enter noumber entre 1-9")
        self.switch_player() 
        clear_wind()

    def switch_player(self) :
        self.current_player_index = 1 - self.current_player_index
    
    def rest_game(self) :
        self.board.rest_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self) :
        b = self.board.borad
        win_conditions = [
        [0, 1, 2],  # الصف الأول
        [3, 4, 5],  # الصف الثاني
        [6, 7, 8],  # الصف الثالث
        [0, 3, 6],  # العمود الأول
        [1, 4, 7],  # العمود الثاني
        [2, 5, 8],  # العمود الثالث
        [0, 4, 8],  # القطر الرئيسي
        [2, 4, 6],  # القطر الثانوي
        ]
        for comba in win_conditions :
            a , b1 , c = comba
            if b[a] == b[b1] == b[c] and not b[a].isdigit() :
                self.board.display_board()
                return True
        return False

    def check_draw(self) :
        return all(not cell.isdigit() for cell in self.board.borad )


    def Quit_game(self) :
        print (" thnik you for playing ??")
        quit()
    
game = Game()
game.start_game()