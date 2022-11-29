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
WIDTH = 800
HEIGHT = 600
PAD_HEIGHT = 100
PAD_WIDTH = 20
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
HALF_PAD_WIDTH = PAD_WIDTH / 2
BALL_RADIUS = 20
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
player1_score = 0
player2_score = 0


WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")


class Paddle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, windows):
        pygame.draw.rect(windows, WHITE,
                         (self.x, self.y, self.width, self.height))


def draw(windows, paddles):
    windows.fill(BLACK)

    for paddle in paddles:
        paddle.draw(windows)
    pygame.display.update()


def main():
    run = True
    clock = fps

    left_paddle = Paddle(10, HEIGHT//2 - HALF_PAD_HEIGHT,
                         PAD_WIDTH, PAD_HEIGHT)

    right_paddle = Paddle(WIDTH - 10 - PAD_WIDTH, HEIGHT//2 - HALF_PAD_HEIGHT,
                          PAD_WIDTH, PAD_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WINDOWS, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()
