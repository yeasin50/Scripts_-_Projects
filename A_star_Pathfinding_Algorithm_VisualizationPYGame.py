import pygame
import math
from queue import PriorityQueue

# Set start and end point 1st, you can remove by mouse right key
# To start algo press Space Key
# go tectwithTim channel for more details

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A Path Finding Algorithm")

RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =(0, 0, 255)

YELLOW = (255, 255, 0)
WHITE = (255, 255,255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255,165, 0)
GRAY = (125, 125, 125)
TURQUOISE = (64, 244, 208)


class Block:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = WHITE
        self.neighbors = []
        self.total_rows = total_rows

    def get_pos(self):
        return self.row , self.col
    
    def is_Closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE


    def make_close(self):
        self.color= RED

    def make_open(self):
        self.color = GREEN
        
    def make_barier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color= TURQUOISE
    
    def make_reset(self):
        self.color = WHITE

    def make_path(self):
        self.color= PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors =[]

        if self.row < self.total_rows -1 and not grid[self.row +1][self.col].is_barrier(): #fall down to x
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row -1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col > 0 and not grid[self.row][self.col -1].is_barrier(): #left
            self.neighbors.append(grid[self.row][self.col-1])

        if self.col < self.total_rows -1 and not grid[self.row][self.col +1].is_barrier(): #right
            self.neighbors.append(grid[self.row][self.col + 1])


    #every object will be judge as uniquly 
    def __lt__(self, value):
        return False


def reconstruct_path(came_from,  current, draw):

    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algothim(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from= {}
    g_score = {block: float("inf") for row in grid for block in row}
    g_score[start] = 0

    f_score = {block: float("inf") for row in grid for block in row}
    f_score[start] = h(start.get_pos(),end.get_pos())

    #Priority Queue doen't have to value existence 
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2] #just for node poss
        open_set_hash.remove(current)

        if current == end: 
            reconstruct_path(came_from, end, draw)
            end.make_path()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add((neighbor))
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_close()

        
    return False

# heuristic functions
def h(p1, p2):
    x1, y1= p1
    x2, y2 = p2
    return abs(x1- x2) + abs(y1 - y2)


def make_grid(rows, width):
    grid = []
    gap = width//rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            block = Block(i, j, gap, rows)
            grid[i].append(block)
    return grid



def draw_grid(win, rows, width):
    
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0,i* gap),(width, i*gap)) 
        for j in range(rows):
            pygame.draw.line(win, GRAY, (j* gap, 0), (j*gap , width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for block in row:
            block.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_poss(poss, rows, width):
    gap = width// rows
    y, x = poss

    row = y//gap
    col = x// gap
    return row, col


def main(win, width):
    rows = 40
    grid = make_grid(rows, width)

    start = None
    end = None
    run = True
    started = False

    while run:
        draw(win, grid,rows,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:#LEFT
                poss = pygame.mouse.get_pos()
                row, col = get_clicked_poss(poss, rows, width)
                # print(row, col)
                block = grid[row][col]

                if not start and block != end:
                    start = block
                    start.make_start()

                elif not end and block != start:
                    end = block
                    end.make_end()

                elif block != end and block != start:
                    block.make_barier()

            elif pygame.mouse.get_pressed()[2]: #RIGHT
                poss = pygame.mouse.get_pos()
                row, col= get_clicked_poss(poss, rows, width)
                block =  grid[row][col]
                block.reset()

                if block == start :
                    start = None
                elif block == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    
                    for row in grid:
                        for block in row:
                            block.update_neighbors(grid)
                    
                    algothim(lambda: draw(win, grid, rows, width),grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, width)


    pygame.quit()


main(WIN, WIDTH)