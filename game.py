import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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

ball_radius = 10
ball_white = pygame.Rect(WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_black = pygame.Rect(3 * WIDTH // 4, HEIGHT // 2, ball_radius * 2, ball_radius * 2)
ball_white_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
ball_black_speed = [random.choice([-5, 5]), random.choice([-5, 5])]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_white = ball_white.move(ball_white_speed)
    ball_black = ball_black.move(ball_black_speed)

    if ball_white.left < 0 or ball_white.right > WIDTH:
        ball_white_speed[0] *= -1
    if ball_white.top < 0 or ball_white.bottom > HEIGHT:
        ball_white_speed[1] *= -1

    if ball_black.left < 0 or ball_black.right > WIDTH:
        ball_black_speed[0] *= -1
    if ball_black.top < 0 or ball_black.bottom > HEIGHT:
        ball_black_speed[1] *= -1

    white_grid_x = ball_white.centerx // GRID_SIZE
    white_grid_y = ball_white.centery // GRID_SIZE
    if grid[white_grid_y][white_grid_x] != WHITE:
        grid[white_grid_y][white_grid_x] = WHITE

    black_grid_x = ball_black.centerx // GRID_SIZE
    black_grid_y = ball_black.centery // GRID_SIZE
    if grid[black_grid_y][black_grid_x] != BLACK:
        grid[black_grid_y][black_grid_x] = BLACK

    screen.fill(GRAY)
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.circle(screen, BLACK, ball_white.center, ball_radius)
    pygame.draw.circle(screen, WHITE, ball_black.center, ball_radius)

    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Day: {sum(row.count(WHITE) for row in grid)} | Night: {sum(row.count(BLACK) for row in grid)}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
