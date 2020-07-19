import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 750, 750

class Grid:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.numbers_selected = 0
		self.squares = [[]]
		width = (WIDTH // rows) // 5
		for i in range(rows + 1):
			self.squares.append([])
			for j in range(cols + 1):
				self.squares[i].append(Square(width))

	def draw(self, window):
		gap = WIDTH // self.rows
		thickness = 1
		for i in range(self.rows):
			pygame.draw.line(window, (0, 0, 0), (0, i * gap), (WIDTH, i * gap), thickness)
			pygame.draw.line(window, (0, 0, 0), (i * gap, 0), (i * gap, HEIGHT), thickness)
		for i in range(self.rows + 1):
			for j in range(self.cols + 1):
				self.squares[i][j].draw(window, i * gap, j * gap)

	def selected_square(self, pos):
		row, col = self.rows + 5, self.rows + 5
		moe = WIDTH // self.rows // 5
		for i in range(self.rows + 1):
			if abs(pos[0] - i * (WIDTH // self.rows)) <= moe:
				row = i
				break
		for i in range(self.rows + 1):
			if abs(pos[1] - i * (WIDTH // self.rows)) <= moe:
				col = i
				break
		if (row < self.rows + 1) and (col < self.cols + 1):
			if self.numbers_selected == 0:
				self.squares[row][col].selected_first = True
				self.numbers_selected += 1
			elif self.numbers_selected == 1 and self.squares[row][col].selected_first != True:
				self.squares[row][col].selected_second = True
				self.numbers_selected += 1
				

class Square:
	def __init__(self, width):
		self.width = width
		self.selected_first = False
		self.selected_second = False

	def draw(self, window, x, y):
		x -= self.width // 2
		y -= self.width // 2
		if self.selected_first:
			pygame.draw.rect(window, (0, 0, 255), (x, y, self.width, self.width))
		elif self.selected_second:
			pygame.draw.rect(window, (255, 0, 0), (x, y, self.width, self.width))
		else:
			pygame.draw.rect(window, (0, 0, 0), (x, y, self.width, self.width), 1)


def main():
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Shortest and Safest Path")
	run = True

	board = Grid(15, 15)

	def redraw_window(window, number_of_streets):
		window.fill((255,255,255))
		board.draw(window)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				board.selected_square((x,y))

		redraw_window(window, 5)
		pygame.display.update()


main()
