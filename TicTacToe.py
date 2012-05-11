
import sys

class TicTacToe:
    
    def main(self):
        print "Welcome to the TicTacToe AI"
        board = self.initialize()
        self.games = []
        self.wins = []
        for turn in xrange(10):
            a = self.getWinner(board)
            if a:
                self.printBoard(board)
                print "player %i wins" % a
                break
            if turn%2 == 1:
                self.printBoard(board)
                print "please enter move in the form i,j"
                i,j = self.getMove()
                board[i][j] = turn%2 + 1
            else:
                board = self.AI_Play(board,turn%2+1)
                #self.printStats()
        print "Thank you come again"
    
    # prints stats about how the AI arrives at ts decision
    def printStats(self):
        
        print "There are", self.games.count(1), "1"
        print "There are", self.games.count(-1), "-1"
        print "There are", self.games.count(0), "0"
        print "player 1 wins %i times" % self.wins.count(1)
        print "player 2 wins %i times" % self.wins.count(2)
        print "There are %i draws" % self.wins.count(-1)
        self.games = []
        self.wins = []
    
    # parses the move from the use input
    def getMove (self):
        [i,j] =  map(int,sys.stdin.readline().split(","))
        return i,j
    
    # returns a board with initially empty slots
    def initialize(self):
        return [[0,0,0] for i in xrange(3)]
    
    # prints the board
    def printBoard(self, board):
        for line in board:
            print "-------------"
            print "|",
            for cell in line:
                print self.getSymbol(cell),"|",
            print "\n",
        print "-------------"

    # just returns the symbolic representaion of the piece on the console
    def getSymbol(self, cell):
        if cell == 0: return " "
        if cell == 1: return "X"
        if cell == 2: return "O"
    
    # This uses the minMax method and returns the move with the best score
    # it actually returns the resultant board
    def AI_Play (self, board, AI_Player_ID):
        plays = []
        generator = self.moveGenerator(board, AI_Player_ID)
        for b in generator:
            score = self.minMax(b, AI_Player_ID, False)
            plays.append((score, b))
        plays.sort()
        for score,b in plays:
            print "this board got a score of %f"%score
            self.printBoard(b)
        score,res = plays[-1]
        return res
    
    # falsely named minMax it is actually just summing up the score at each level
    # the wins and games lists are just for debugging
    def minMax (self, board, AI_Player_ID, myTurn):
        a = self.getWinner(board)
        #self.wins.append(a)
        if a :
            if a == AI_Player_ID:
                #self.games.append(1)
                return 1
            if a == -1 :
                #self.games.append(0)
                return 0
            if a == (AI_Player_ID % 2 + 1) :
                #self.games.append(-1)
                return -1
            else : print "fail"
        generator = self.moveGenerator(board, myTurn and AI_Player_ID or ((AI_Player_ID%2)+1))
        scores = []
        for b in generator:
            score = self.minMax(b,AI_Player_ID,not myTurn)
            scores.append(score)
        return 0.1*sum(scores)
    
    # Dumb generator returns randomly generated moves
    def moveGenerator (self, board, player):
        for i in xrange(3):
            for j in xrange(3):
                if not board[i][j]:
                    b = self.copy(board)
                    b[i][j] = player
                    yield b
    
    # it clones the board which is problematic because
    # it is a list of lists so list[:] doesnt work
    def copy(self,board):
        res=[]
        for line in board:
            res.append(line[:])
        return res
    
    # Uses check method to return the winner or -1 for a draw
    # it also retrurns None if the game isnt over yet
    def getWinner (self, board):
        for i in xrange(3):
            if self.checkCol(board, i):
                return board[0][i]
            if self.checkRow(board, i):
                return board[i][0]
        if self.checkBackSlash(board):
            return board[0][0]
        if self.checkForwardSlash(board):
            return board[0][-1]
        if self.isFilled(board):
            return -1
    
    # Check for a Draw
    def isFilled(self, board):
        for line in board:
            for cell in line:
                if cell == 0: return False
        return True
    
    # Various checks for a winner
    # returns the winner or False if nobody won
    def checkCol (self, board, colIndex):
        a = board[0][colIndex]
        for line in board:
            if line[colIndex] != a: return False
        return a

    def checkRow (self, board, rowIndex):
        a = board[rowIndex][0]
        if board[rowIndex] == [a,a,a]: return a
        return False
    
    def checkBackSlash (self, board):
        a = board[0][0]
        for i in xrange(3):
            if board[i][i] != a: return False
        return a

    def checkForwardSlash (self, board):
        a = board[0][-1]
        for i in xrange(3):
            if board[-(i+1)][i] != a: return False
        return a

    def waysOfWinning(self, board):
        pass

if __name__ == "__main__" :
    t = TicTacToe()
    t.main()
