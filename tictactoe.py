class Grid:

    def __init__(self, is_empty = True, input_grid = [['', '', ''], ['', '', ''], ['', '', '']], player_1 = 'x', player_2 = 'o'):
        self.grid = input_grid
        self.is_empty = True
        self.is_full = False
        self.winner = None
        self.player_1 = player_1
        self.player_2 = player_2

    def check_grid(self):
        print(*self.grid, sep = "\n")
    
    def grid_is_full(self):
        counter = 0
        for row in self.grid:
            for item in row:
                if item != '':
                    counter += 1
        if counter == 9:
            self.is_full = True
            print("This grid is full !")
    
    def check_winner(self):
        for n in range(0, 3):
            if self.grid[0][n] == self.grid[1][n] and self.grid[1][n] == self.grid[2][n]:
                if self.grid[0][n] == 'x':
                    self.winner = 'x'
                elif self.grid[0][n] == 'o':
                    self.winner = 'o'
            elif self.grid[n][0] == self.grid[n][1] and self.grid[n][1] == self.grid[n][2]:
                if self.grid[n][0] == 'x':
                    self.winner = 'x'
                elif self.grid[n][0] == 'o':
                    self.winner ='o'
            elif self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
                if self.grid[0][0] == 'x':
                    self.winner = 'x'
                elif self.grid[0][0] == 'o':
                    self.winner ='o'
            elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
                if self.grid[0][2] == 'x':
                    self.winner = 'x'
                elif self.grid[0][2] == 'o':
                    self.winner ='o'
            else:
                if self.is_full:
                    print("It's a draw")
        print(self.winner)
    
    def player_1_turn(self):
        x = int(input("Player 1 give X coordinates for next move :"))
        y = int(input("Player 1 give Y coordinates for next move :"))
        if self.grid[x][y] == '':
            self.grid[x][y] = self.player_1
        else:
            print('Invalid play')
    
    def player_2_turn(self):
        x = int(input("Player 2 give X coordinates for next move :"))
        y = int(input("Player 2 give Y coordinates for next move :"))
        if self.grid[x][y] == '':
            self.grid[x][y] = self.player_2
        else:
            print('Invalid play')



            
grid_1 = Grid()

while grid_1.is_full == False and grid_1.winner == None:
    grid_1.check_grid()
    grid_1.player_1_turn()
    grid_1.check_grid()
    grid_1.check_winner()
    grid_1.grid_is_full()
    grid_1.player_2_turn()
    grid_1.check_grid()
    grid_1.check_winner()
    grid_1.grid_is_full()







