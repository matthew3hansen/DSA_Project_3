import pygame
import os

import ImTrying

pygame.font.init()

WIDTH, HEIGHT = 750, 750

class Grid:
	def __init__(self, rows, cols, array):
		self.rows = rows
		self.cols = cols
		self.numbers_selected = 0
		self.squares = [[]]
		self.array = array
		self.width = (WIDTH // rows) // 5
		self.gap = WIDTH // self.rows
		new_array = []

		for i in range(rows):
			self.squares.append([])
			for j in range(cols):
				self.squares[i].append(Square(self.width))
		
		for i in range(0, rows):
			for j in range(0, cols):
				self.squares[i][j].node = array[i][j]


	def draw(self, window):
		for i in range(self.rows):
			for j in range(self.cols):
				self.squares[i][j].draw(window, i * self.gap + 25, j * self.gap + 25, self.gap)

	def get_mouse_position(self, pos):
		row, col = self.rows + 5, self.rows + 5
		moe = WIDTH // self.rows // 5
		for i in range(self.rows):
			if abs(pos[0] - i * (WIDTH // self.rows) - 25) <= moe:
				row = i
				break
		for i in range(self.rows):
			if abs(pos[1] - i * (WIDTH // self.rows) - 25) <= moe:
				col = i
				break
		return row, col

	def selected_square(self, pos):
		row, col = self.get_mouse_position(pos)

		if (row < self.rows) and (col < self.cols):
			if self.squares[row][col].node != None:
				if self.numbers_selected == 0:
					self.squares[row][col].selected_first = True
					self.numbers_selected += 1
					return 1
				elif self.numbers_selected == 1 and self.squares[row][col].selected_first != True:
					self.squares[row][col].selected_second = True
					self.numbers_selected += 1
					return 2
		return 0

	def add_adjacency_node_list(self, adjacencyList):
		counter = 0
		for i in range(self.rows):
			for j in range(self.cols):
				if(self.squares[i][j].node != None):
					self.squares[i][j].node.adjacentNodes = adjacencyList[counter].adjacentNodes
					counter += 1				

	def find_first_selected(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.squares[i][j].selected_first:
					return i, j

	def find_second_selected(self):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.squares[i][j].selected_second:
					return i, j

	def get_row_col_of_square(self, name):
		for i in range(self.rows):
			for j in range(self.cols):
				if self.squares[i][j].node != None:
					if self.squares[i][j].node.intersectionName == name:
						return i, j
		return -1, -1

	def draw_path(self, window, previous_map, name, source):
		row, col = self.get_row_col_of_square(name)
		if row != -1:
			if name != source:
				previous_node = previous_map[name]
				for i in range(len(self.squares[row][col].node.adjacentNodes)):
						if self.squares[row][col].node.adjacentNodes[i][0].intersectionName == previous_node:
							if(self.squares[row][col].node.adjacentNodes[i][1] == "W"):
								pygame.draw.line(window, (0, 255, 0), (self.squares[row][col].x, self.squares[row][col].y - self.width), (self.squares[row][col].x, self.squares[row][col].y - self.gap + self.width), 3)
								break
							elif(self.squares[row][col].node.adjacentNodes[i][1] == "E"):
								pygame.draw.line(window, (0, 255, 0), (self.squares[row][col].x, self.squares[row][col].y + self.width), (self.squares[row][col].x, self.squares[row][col].y + self.gap - self.width), 3)
								break
							elif(self.squares[row][col].node.adjacentNodes[i][1] == "S"):
								pygame.draw.line(window, (0, 255, 0), (self.squares[row][col].x + self.width, self.squares[row][col].y), (self.squares[row][col].x + self.gap - self.width, self.squares[row][col].y), 3)
								break
							elif(self.squares[row][col].node.adjacentNodes[i][1] == "N"):
								pygame.draw.line(window, (0, 255, 0), (self.squares[row][col].x - self.width, self.squares[row][col].y), (self.squares[row][col].x - self.gap + self.width, self.squares[row][col].y), 3)
								break
				self.draw_path(window, previous_map, previous_node, source)


class Square:
	def __init__(self, width, node=None):
		self.width = width
		self.x = 0
		self.y = 0
		self.selected_first = False
		self.selected_second = False
		self.node = node

	def draw(self, window, x, y, gap):
		self.x = x
		self.y = y
		if(self.node != None):
			thickness = 1
			for i in range(len(self.node.adjacentNodes)):
				if(self.node.adjacentNodes[i][1] == "W"):
					pygame.draw.line(window, (0, 0, 0), (x, y - self.width), (x, y - gap + self.width), thickness)
				elif(self.node.adjacentNodes[i][1] == "E"):
					pygame.draw.line(window, (0, 0, 0), (x, y + self.width), (x, y + gap - self.width), thickness)
				elif(self.node.adjacentNodes[i][1] == "S"):
					pygame.draw.line(window, (0, 0, 0), (x + self.width, y), (x + gap - self.width, y), thickness)
				elif(self.node.adjacentNodes[i][1] == "N"):
					pygame.draw.line(window, (0, 0, 0), (x - self.width, y), (x - gap + self.width, y), thickness)

			x -= self.width // 2
			y -= self.width // 2
			if self.selected_first:
				pygame.draw.rect(window, (0, 100, 255), (x, y, self.width, self.width))
			elif self.selected_second:
				pygame.draw.rect(window, (255, 0, 0), (x, y, self.width, self.width))
			else:
				pygame.draw.rect(window, (0, 0, 0), (x, y, self.width, self.width), 1)
			x += self.width // 2
			y += self.width // 2

			font = pygame.font.SysFont("comicsans", 20)
			text = font.render(str(self.node.weight), 1, (0, 0, 0))
			window.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


def find_alist_index_from_array(array, source):
	counter = 0
	for i in range(len(array)):
		for j in range(len(array[0])):
			if array[i][j] != None:
				if array[i][j].intersectionName == source:
					return counter
				counter += 1


def main_function():
	rows, columns = ImTrying.findDimensionsOfMap()
	array = ImTrying.createArray(rows, columns)
	adjacencyList, intersectionNameDictionary = ImTrying.createAdjacencyList(array, rows, columns)
	
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Shortest and Safest Path")
	run = True

	board = Grid(10, 10, array)
	board.add_adjacency_node_list(adjacencyList)

	show_path = False


	def redraw_window(window, number_of_streets, show_path):
		window.fill((255, 255, 255))
		board.draw(window)
		if show_path:
			row_1, col_1 = board.find_first_selected()
			row_2, col_2 = board.find_second_selected()
			source = board.squares[row_1][col_1].node.intersectionName
			destination = board.squares[row_2][col_2].node.intersectionName
			board.draw_path(window, previous_map, destination, source)


	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				number_selected = board.selected_square((x,y))
				if number_selected == 1:
					row_1, col_1 = board.find_first_selected()
					source = board.squares[row_1][col_1].node.intersectionName
					index = find_alist_index_from_array(array, source)
					weight_map, previous_map = ImTrying.shortest_path_visual(adjacencyList, index)
				if number_selected == 2:
					show_path = True

		redraw_window(window, 5, show_path)
		pygame.display.update()


main_function()
