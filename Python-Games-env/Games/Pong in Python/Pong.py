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
BALL_RADIUS = 10
player1_score = 0
player2_score = 0


WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")


class Paddle:
    PAD_VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, windows):
        pygame.draw.rect(
            windows, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.PAD_VEL
        else:
            self.y += self.PAD_VEL


class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        pygame.draw.circle(windows, RED, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def draw(windows, paddles, ball):
    windows.fill(BLACK)

    for paddle in paddles:
        paddle.draw(windows)

    for i in range(10, HEIGHT, HEIGHT//10):
        if i % 2 == 1:
            continue
        pygame.draw.rect(windows, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(windows)

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_z] and left_paddle.y - left_paddle.PAD_VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.PAD_VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.PAD_VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.PAD_VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y < + left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = diff_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= right_paddle.y and ball.y < + right_paddle.y + right_paddle.height:
            if ball.x + + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                diff_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = diff_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def main():
    run = True
    clock = fps

    left_paddle = Paddle(10, HEIGHT//2 - HALF_PAD_HEIGHT,
                         PAD_WIDTH, PAD_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PAD_WIDTH, HEIGHT //
                          2 - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WINDOWS, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

    pygame.quit()


if __name__ == '__main__':
    main()
