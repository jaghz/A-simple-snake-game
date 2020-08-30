import random
class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
    
    def take_step(self, position):
        self.body = [position] + self.body[0:len(self.body)-1]
    def set_direction(self, direction):
        self.direction = direction
        

class Apple: 
    def __init__(self, height, width):
        self.position = (random.randrange(0,height-1), random.randrange(0,width-1))
        
        
UP = (-1,0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0, -1)
class Game:     
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board=[]
        self.snake = Snake([(2, 2), (3,2), (4,2), (5,2), (6,2),(7,2)], UP)
    
    def board_matrix(self):
        # Create the game board with given height and width
        self.board = [[' ']*self.width for i in range(self.height)]
           
    def render(self):
        print("Height: ", self.height)
        print("Width: ", self.width)
        appleSpawned = False
        gameRunning = True
        x = input("position (wasd) or (q) to quit: ")
        gameAtStart = True
        while gameRunning:
            if x == 'q':
                break
            
            self.board = [[' ']*self.width for i in range(self.height)]
            
                                
                
            # Update snake position
            if x == 'd' or x == 'D':
                self.snake.set_direction((RIGHT))
                position = (self.snake.direction[0] + self.snake.body[0][0], 
                            self.snake.direction[1]+self.snake.body[0][1])
                if position[1] >= self.width or self.board[position[0]][position[1]] != ' ':
                    print("you lose!")
                    break
                #self.snake.take_step(position)
            elif x == 'a' or x == 'A':
                self.snake.set_direction(LEFT)
                position = (self.snake.direction[0]+self.snake.body[0][0],
                            self.snake.direction[1]+self.snake.body[0][1])
                
                if position[1] < 0 or self.board[position[0]][position[1]] != ' ':
                    print("you lose!")
                    break
                #self.board = [[' ']*self.width for i in range(self.height)]
                #self.snake.take_step(position)
            elif x == 's' or x == 'S' :
               # self.board = [[' ']*self.width for i in range(self.height)]
                self.snake.set_direction(DOWN)
                position = (self.snake.direction[0]+self.snake.body[0][0],
                            self.snake.direction[1]+self.snake.body[0][1])
                
                if position[0] >= self.height or self.board[position[0]][position[1]] != ' ': #snake always starts in vertical position
                    print("you lose!")
                    break
                if gameAtStart:
                    print("the snake ate himself!")
                    print("you lose!")
                    break
                #self.snake.take_step(position)
            elif x == 'w' or x == 'W':
                self.snake.set_direction(UP)
                #self.board = [[' ']*self.width for i in range(self.height)]

                position = (self.snake.direction[0]+self.snake.body[0][0],
                            self.snake.direction[1]+self.snake.body[0][1])
                if position[0] < 0  or self.board[position[0]][position[1]] != ' ':
                    print("you lose!")
                    break       
            elif x == '':
                position = (self.snake.direction[0]+self.snake.body[0][0],
                            self.snake.direction[1]+self.snake.body[0][1])
                if position[0] < 0 or position[0] >= self.height or self.board[position[0]][position[1]] != ' ':
                    print("you lose!")
                    break
            if position in self.snake.body:
                print("the snake ate himself!")
                print("you lose!")
                break
            self.snake.take_step(position)
            
            print('position: ', position)
            # Render the snake's position on the board
            for coordinate in self.snake.body:
                xPos = coordinate[0]
                yPos = coordinate[1]
                for i in range(self.height):
                    if i == xPos:
                        for j in range(len(self.board[0])):
                            if j == yPos:
                                if (xPos, yPos) == self.snake.body[0]:
                                    self.board[i][j] = 'X'
                                else:
                                    self.board[i][j] = 'O'
            
            if appleSpawned is False:
                appleX, appleY = 2, 2
                while self.board[appleX][appleY] != ' ':
                    apple = Apple(self.height, self.width)
                    appleX = apple.position[0]
                    appleY = apple.position[1]
                
                appleSpawned = True
                appleEaten = False
            if appleEaten is False:
                self.board[appleX][appleY] = 'o'
            
            if (appleX, appleY) == (position[0],position[1]):
                self.board[appleX][appleY] = 'X'
                appleEaten = True
                appleSpawned = False
                tail = self.snake.body[-1]
                newTail = (tail[0]+self.snake.direction[0], tail[1]+self.snake.direction[1])
                self.snake.body.append(newTail)
                
            # Render the board
            verticalBorderTop = ''
            for i in range(0, self.width+1):
                if i == 0 :
                    verticalBorderTop += '+'
                elif i == self.width:
                    verticalBorderTop += '_+'
                else:
                    verticalBorderTop +='_ ' 
                    
            verticalBorderBottom = ''
            for i in range(0, self.width+1):
                if i == 0 :
                    verticalBorderBottom += '+'
                elif i == self.width:
                    verticalBorderBottom += '-+'
                else:
                    verticalBorderBottom +='--' 
                    
            print(verticalBorderTop)
            for i in range(self.height):
                for j in range(len(self.board[0])):
                    if j == 0 :
                        print("|", end = '')
                    if j == len(self.board[0])-1:
                        print(self.board[i][j], end = "")
                        print("|", end = "")
                    else:
                        if j != len(self.board[0])-1:
                            print(self.board[i][j], end = " ")
                        else:
                            print(self.board[i][j])
                print("\t")
            print(verticalBorderBottom)
            gameAtStart = False
            x = input("position (wasd) or (q) to quit: ")
            
                

    
        
x = Game(10, 15)
x.board_matrix()
x.render()
        
        
        