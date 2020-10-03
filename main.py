import pygame
import math

WIDTH, HEIGHT = 800, 600
POINTS_COUNT = 200
RADIUS = 200
STEP = 0.005
COLOR = (200, 200, 200)

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Times table')
font = pygame.font.SysFont('consolas', 60)
clock = pygame.time.Clock()


def inp():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()


# get positions of n points in a circle with radius r
def get_points(r, n):
	return [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r) for x in range(0, n + 1)]


points = get_points(RADIUS, POINTS_COUNT)
# multiplication factor
factor = 1


def loop():
	global factor
	screen.fill((0, 0, 0))
	# draw points
	for i in points:
		pygame.draw.circle(screen, COLOR, translate(i), 2)
	# draw lines
	for current in range(1, POINTS_COUNT):
		start = translate(points[current % POINTS_COUNT])
		end = translate(points[int(current * factor) % POINTS_COUNT])
		pygame.draw.line(screen, COLOR, start, end, 1)
	factor += STEP

	# display text
	text = font.render(str(int(factor)), True, (255, 255, 255))
	text_rect = text.get_rect(center=(WIDTH // 2, int(HEIGHT * 0.45) - RADIUS))
	screen.blit(text, text_rect)

	pygame.display.update()


# translate given position to the center of the screen
def translate(t):
	return tuple(map(lambda x: int(sum(x)), zip(t, (WIDTH // 2, HEIGHT * 0.55))))


while True:
	inp()
	loop()
	clock.tick(144)
