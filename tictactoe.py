class Grid:
    #This is intended to be a local 2 player game, so we init 2 players
    def __init__(self, input_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], player_1 = 'X', player_2 = 'O'):
        #self.coordinates maps the location of the grid to a "Row - Column" arrangement that makes it easier to use (user gives indication like Middle(row) - Center(column) instead of x and y coordinates)
        self.coordinates = {"Top - Left" : [0,0], "Top - Center" : [0,1], "Top - Right" : [0,2], "Middle - Left" : [1,0], "Middle - Center" : [1,1], "Middle - Right" : [1,2], "Bottom - Left" : [2, 0], "Bottom - Center" : [2,1], "Bottom - Right" : [2,2]}
        self.grid = input_grid
        self.is_empty = True
        self.is_full = False
        self.winner = None
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_plays = {"Player 1" : [], "Player 2" : []}

    #Prints out the 3 lists used as a grid for better comprehension
    def check_grid(self):
        print(*self.grid, sep = "\n")
    
    #Checks if the grid is full or not, if it is full and the game has no winner, it's a draw
    def grid_is_full(self):
        counter = 0
        for row in self.grid:
            for item in row:
                if item != '-':
                    counter += 1
        if counter == 9:
            self.is_full = True
            print("This grid is full !")
        self.is_full = False
    
    #This is the biggest part, it checks every possible way of winning (8 total) and returns the winning row / column / diagonal.
    def check_winner(self):
        win_string = ''
        for player, play in self.player_plays.items():
            if "Top - Left" in play and "Top - Center" in play and "Top - Right" in play:
                win_string = player + " wins with Top Row"
                break
            elif "Middle - Left" in play and "Middle - Center" in play and "Middle - Right" in play:
                win_string = player + " wins with Middle Row"
                break
            elif "Bottom - Left" in play and "Bottom - Center" in play and "Bottom - Right" in play:
                win_string = player + " wins with Bottom Row"
                break
            elif "Top - Left" in play and "Middle - Left" in play and "Bottom - Left" in play:
                win_string = player + " wins with Left Column"
                break
            elif "Top - Center" in play and "Middle - Center" in play and "Bottom - Center" in play:
                win_string = player + " wins with Center Column"
                break
            elif "Top - Right" in play and "Middle - Right" in play and "Bottom - Right" in play:
                win_string = player + " wins with Right Column"
                break
            elif "Top - Left" in play and "Middle - Center" in play and "Bottom - Right" in play:
                win_string = player + " wins with Diagonal"
                break
            elif "Top - Right" in play and "Middle - Center" in play and "Bottom - Left" in play:
                win_string = player + " wins with Diagonal"
                break
        if win_string != '':
            self.winner = player
            print(win_string)
            return win_string

    #Player 1 turn, if the move he tried making is invalid (coordinates wrong or coordinates already occupied), it loops back to the beginning
    def player_1_turn(self):
        play_done = False
        play = input("Player 1 : Where do you want to play ? ")
        if play in self.coordinates:
            self.player_plays["Player 1"].append(play)
            play_x = self.coordinates[play][0]
            play_y = self.coordinates[play][1]
            if self.grid[play_x][play_y] != '-':
                print("Invalid Play : Ocupied")
                return play_done
            self.grid[play_x][play_y] = self.player_1
            play_done = True
            return play_done
        else:
            print("Invalid Play : Play notrecognized")
        return play_done
    #Player 2 turn, same as player 1       
    def player_2_turn(self):
        play_done = False
        play = input("Player 2 : Where do you want to play ? ")
        if play in self.coordinates:
            self.player_plays["Player 2"].append(play)
            play_x = self.coordinates[play][0]
            play_y = self.coordinates[play][1]
            if self.grid[play_x][play_y] != '-':
                print("Invalid Play : Ocupied")
                return play_done
            self.grid[play_x][play_y] = self.player_2
            play_done = True
            return play_done
        else:
            print("Invalid Play : Play not recognized")
        return play_done

           
grid_1 = Grid()

print("Welcome to TicTacToe, please enter your play as follow : Row - Column. Some examples of valid plays : 'Top - Center', 'Middle - Left', etc.")

#We want the game to keep going as long as there is no tie or winner
while grid_1.is_full == False and grid_1.winner == None:
    #First impression of the blank grid
    grid_1.check_grid()
    #Player 1 plays until he has a valid turn
    while grid_1.player_1_turn() == False:
        grid_1.player_1_turn()
    #Prints grid after player turn
    grid_1.check_grid()
    #Checks if this was a winning move
    grid_1.check_winner()
    #Stops game if player 1 had made a winning move
    if grid_1.winner != None:
        break
    grid_1.grid_is_full()
    #Stops game if grid is full with no winner
    if grid_1.grid_is_full():
        break
    while grid_1.player_2_turn() == False:
        grid_1.player_2_turn()
    if grid_1.winner != None:
        break
    grid_1.check_winner()
    grid_1.grid_is_full()
    if grid_1.grid_is_full():
        break