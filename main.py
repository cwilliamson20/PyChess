#TODO: figure out how to draw the board itself
#TODO: make piece class, maybe with a list of valid moves to look through each time?
import pygame, sys

# setup
pygame.init()

# GAME CONSTANTS
screen_size = 1024
square_size = int(screen_size / 8)
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
pygame.display.set_caption("PyChess")
dark_square_color = (50, 168, 102)
light_square_color = (235, 237, 235)
dark_piece_color = pygame.Color('black')
light_piece_color = pygame.Color('white')

square = pygame.Rect(0, 0, square_size, square_size)

# initialize all 64 squares on the board
# each list in squares represents a horizontal row of squares on the board
squares = [[],[],[],[],[],[],[],[]]
y_coord = 0
for row in squares:
    x_coord = 0
    for i in range(0,8):
        row.append(pygame.Rect(x_coord, y_coord, square_size, square_size))
        x_coord += square_size
    y_coord += square_size


# game loop
while True:
    # look at all in game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw the board base (8 x 8 alternating color squares)
    for i in range(0, len(squares)):
        # odd rows start with light color
        # even rows start with dark color
        if i % 2 != 0:
            # odd row
            for a in range(0,8,2):
                pygame.draw.rect(screen, light_square_color, squares[i][a])
                pygame.draw.rect(screen, dark_square_color, squares[i][a+1])
        else:
            # even row
            for a in range(0,8,2):
                pygame.draw.rect(screen, dark_square_color, squares[i][a])
                pygame.draw.rect(screen, light_square_color, squares[i][a+1])



    # update game window after looking at events
    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

