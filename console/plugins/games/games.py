from random import randint

def startGame(commandLine):
    game = commandLine.split(' ')[1]
    
    if game == "tictactoe" or game == "ticTacToe" or game == "TicTacToe":
        ttt = ticTacToe()
        ttt.startGame()

class ticTacToe():
    def __init__(self):
        self.pos = [
            "", "", "",
            "", "", "",
            "", "", ""
        ]

        self.player1 = "-"
        self.player2 = "-"
        self.curLetter = 0
        self.choose = 0
    
    def startGame(self):
        while True:
            choose = input("Choose between X or O: ")
            
            if choose == "X" or choose == "O":
                self.player1 = choose

                if choose == "X":
                    self.player2 = "O"
                else:
                    self.player2 = "X"
                
                break
            else:
                print("\nYou can only choose X or O\n")

        firstPlayer = randint(0, 100)

        if(firstPlayer >= 51):
            self.curLetter = self.player1
            print("\nPlayer 1 is going to be the first to play\n")
        else:
            self.curLetter = self.player2
            print("\nPlayer 2 is going to be the first to play\n")

        self.printScreen()
        self.game()

    def game(self):
        while True:
            self.putLetterInScreen()

            if self.events() == "X":
                if self.player1 == "X":
                    print("\nPlayer 1 won!\n")
                    break
                else:
                    print("\nPlayer 2 won!\n")
                    break

            elif self.events() == "O":
                if self.player1 == "O":
                    print("\nPlayer 1 won!\n")
                    break
                else:
                    print("\nPlayer 2 won!\n")
                    break

            elif self.events() == "-":
                print("\nGame Over! Nobody won\n")
                break

    def printScreen(self):
        print(f"\n {self.pos[0]} | {self.pos[1]} | {self.pos[2]} \n---------\n {self.pos[3]} | {self.pos[4]} | {self.pos[5]} \n---------\n {self.pos[6]} | {self.pos[7]} | {self.pos[8]} \n")

    def putLetterInScreen(self):
        while True:
            try:
                self.choose = int(input("Choose a position between 1 and 9: "))
                
                if self.choose < 1 or self.choose > 9:
                    print("\nChoose a number between 1 and 9\n")
                elif self.pos[self.choose - 1] != "":
                    print("\nThis position already was choosen\n")
                else:
                    break

            except ValueError:
                print("\nChoose a number\n")

        self.pos[self.choose -1] = self.curLetter

        if self.curLetter == "X":
            self.curLetter = "O"
        else:
            self.curLetter = "X"

        self.printScreen()

    def checkOWins(self):
        for i in range(0, 6, 3):
            if self.pos[i] == self.pos[i + 1] == self.pos[i + 2] == "O":
                return True

        for i in range(0, 3):
            if self.pos[i] == self.pos[i + 3] == self.pos[i + 6] == "O":
                return True

        if self.pos[0] == self.pos[4] == self.pos[8] == "O":
            return True

        if self.pos[2] == self.pos[4] == self.pos[6] == "O":
            return True

    def checkXWins(self):
        for i in range(0, 6, 3):
            if self.pos[i] == self.pos[i + 1] == self.pos[i + 2] == "X":
                return True

        for i in range(0, 3):
            if self.pos[i] == self.pos[i + 3] == self.pos[i + 6] == "X":
                return True

        if self.pos[0] == self.pos[4] == self.pos[8] == "X":
            return True

        if self.pos[2] == self.pos[4] == self.pos[6] == "X":
            return True

    def events(self):
        if self.checkXWins():
            return "X"
        elif self.checkOWins():
            return "O"
        elif "" not in self.pos:
            return "-"
        else: 
            return ""