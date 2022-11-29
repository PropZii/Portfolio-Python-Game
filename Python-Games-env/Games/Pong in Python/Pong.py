import pygame
pygame.init()
fps = pygame.time.Clock()
FPS = 60

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# globals
WIDTH = 900
HEIGHT = 700
PAD_HEIGHT = 80
PAD_WIDTH = 6
BALL_RADIUS = 20
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
player1_score = 0
player2_score = 0


WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")

# game loop


def draw(windows):
    windows.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    clock = fps

    while run:
        clock.tick(FPS)
        draw(WINDOWS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()
