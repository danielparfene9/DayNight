import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (131, 135, 141)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Bounce Game")


grid = [[GRAY for _ in range(WIDTH // GRID_SIZE)] for _ in range(HEIGHT // GRID_SIZE)]


for y in range(len(grid)):
    for x in range(len(grid[0]) // 2):
        grid[y][x] = WHITE

for y in range(len(grid)):
    for x in range(len(grid[0]) // 2, len(grid[0])):
        grid[y][x] = BLACK

ball_radius = 12
ball_white = pygame.Rect(WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_black = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_white_speed = [random.choice([-10, 10]), random.choice([-10, 10])]
ball_black_speed = [random.choice([-10, 10]), random.choice([-10, 10])]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_white = ball_white.move(ball_white_speed)
    ball_black = ball_black.move(ball_black_speed)


    if math.sqrt(ball_white_speed[0] ** 2 + ball_white_speed[1] ** 2) == 0:
        ball_white_speed = [random.choice([-10, 10]), random.choice([-10, 10])]


    if math.sqrt(ball_black_speed[0] ** 2 + ball_black_speed[1] ** 2) == 0:
        ball_black_speed = [random.choice([-10, 10]), random.choice([-10, 10])]


    white_grid_x = min(max(ball_white.centerx // GRID_SIZE, 0), len(grid[0]) - 1)
    white_grid_y = min(max(ball_white.centery // GRID_SIZE, 0), len(grid) - 1)
    if grid[white_grid_y][white_grid_x] == BLACK:
        dx = ball_white.centerx - white_grid_x * GRID_SIZE - GRID_SIZE / 2
        dy = ball_white.centery - white_grid_y * GRID_SIZE - GRID_SIZE / 2
        angle = math.atan2(dy, dx)
        speed = math.sqrt(ball_white_speed[0] ** 2 + ball_white_speed[1] ** 2)
        ball_white_speed[0] = speed * math.cos(2 * angle) * -1
        ball_white_speed[1] = speed * math.sin(2 * angle) * -1
        grid[white_grid_y][white_grid_x] = WHITE


    black_grid_x = min(max(ball_black.centerx // GRID_SIZE, 0), len(grid[0]) - 1)
    black_grid_y = min(max(ball_black.centery // GRID_SIZE, 0), len(grid) - 1)
    if grid[black_grid_y][black_grid_x] == WHITE:
        dx = ball_black.centerx - black_grid_x * GRID_SIZE - GRID_SIZE / 2
        dy = ball_black.centery - black_grid_y * GRID_SIZE - GRID_SIZE / 2
        angle = math.atan2(dy, dx)
        speed = math.sqrt(ball_black_speed[0] ** 2 + ball_black_speed[1] ** 2)
        ball_black_speed[0] = speed * math.cos(2 * angle) * -1
        ball_black_speed[1] = speed * math.sin(2 * angle) * -1
        grid[black_grid_y][black_grid_x] = BLACK


    if ball_white.left < 0 or ball_white.right > WIDTH:
        ball_white_speed[0] *= -1
    if ball_white.top < 0 or ball_white.bottom > HEIGHT:
        ball_white_speed[1] *= -1

    if ball_black.left < 0 or ball_black.right > WIDTH:
        ball_black_speed[0] *= -1
    if ball_black.top < 0 or ball_black.bottom > HEIGHT:
        ball_black_speed[1] *= -1

    screen.fill(GRAY)
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.circle(screen, BLACK, ball_white.center, ball_radius)
    pygame.draw.circle(screen, WHITE, ball_black.center, ball_radius)

    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Day: {sum(row.count(WHITE) for row in grid)} | Night: {sum(row.count(BLACK) for row in grid)}",
                       True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(144)

pygame.quit()
