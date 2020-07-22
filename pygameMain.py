import pygame
import os

import ImTrying

pygame.font.init()

WIDTH, HEIGHT = 750, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shortest and Safest Path")


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

    def draw(self, window, type_of_path):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].draw(window, i * self.gap + 25, j * self.gap + 25, self.gap, type_of_path)

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
                if (self.squares[i][j].node != None):
                    self.squares[i][j].node.adjacentNodes = adjacencyList[counter].adjacentNodes
                    counter += 1

    def redo(self):
        self.numbers_selected = 0
        row, col = self.find_first_selected()
        if row != -1:
            self.squares[row][col].selected_first = False

        row, col = self.find_second_selected()
        if row != -1:
            self.squares[row][col].selected_second = False

    def find_first_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].node != None:
                    if self.squares[i][j].selected_first:
                        return i, j
        return -1, -1

    def find_second_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].node != None:
                    if self.squares[i][j].selected_second:
                        return i, j
        return -1, -1

    def get_row_col_of_square(self, name):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.squares[i][j].node != None:
                    if self.squares[i][j].node.intersectionName == name:
                        return i, j
        return -1, -1

    def draw_path(self, window, previous_map, name, source, color):
        row, col = self.get_row_col_of_square(name)
        if row != -1:
            if name != source:
                previous_node = previous_map[name]
                for i in range(len(self.squares[row][col].node.adjacentNodes)):
                    if self.squares[row][col].node.adjacentNodes[i][0].intersectionName == previous_node:
                        if (self.squares[row][col].node.adjacentNodes[i][1] == "W"):
                            pygame.draw.line(window, color,
                                             (self.squares[row][col].x, self.squares[row][col].y - self.width), (
                                                 self.squares[row][col].x,
                                                 self.squares[row][col].y - self.gap + self.width), 3)
                            break
                        elif (self.squares[row][col].node.adjacentNodes[i][1] == "E"):
                            pygame.draw.line(window, color,
                                             (self.squares[row][col].x, self.squares[row][col].y + self.width), (
                                                 self.squares[row][col].x,
                                                 self.squares[row][col].y + self.gap - self.width), 3)
                            break
                        elif (self.squares[row][col].node.adjacentNodes[i][1] == "S"):
                            pygame.draw.line(window, color,
                                             (self.squares[row][col].x + self.width, self.squares[row][col].y), (
                                                 self.squares[row][col].x + self.gap - self.width,
                                                 self.squares[row][col].y), 3)
                            break
                        elif (self.squares[row][col].node.adjacentNodes[i][1] == "N"):
                            pygame.draw.line(window, color,
                                             (self.squares[row][col].x - self.width, self.squares[row][col].y), (
                                                 self.squares[row][col].x - self.gap + self.width,
                                                 self.squares[row][col].y), 3)
                            break
                self.draw_path(window, previous_map, previous_node, source, color)


class Square:
    def __init__(self, width, node=None):
        self.width = width
        self.x = 0
        self.y = 0
        self.selected_first = False
        self.selected_second = False
        self.node = node

    def draw(self, window, x, y, gap, type_of_path):
        self.x = x
        self.y = y
        if (self.node != None):
            thickness = 1
            for i in range(len(self.node.adjacentNodes)):
                if (self.node.adjacentNodes[i][1] == "W"):
                    pygame.draw.line(window, (0, 0, 0), (x, y - self.width), (x, y - gap + self.width), thickness)
                elif (self.node.adjacentNodes[i][1] == "E"):
                    pygame.draw.line(window, (0, 0, 0), (x, y + self.width), (x, y + gap - self.width), thickness)
                elif (self.node.adjacentNodes[i][1] == "S"):
                    pygame.draw.line(window, (0, 0, 0), (x + self.width, y), (x + gap - self.width, y), thickness)
                elif (self.node.adjacentNodes[i][1] == "N"):
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
            if type_of_path != "Shortest":
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


def main_function(type_of_path):
    rows, columns = ImTrying.findDimensionsOfMap()
    array = ImTrying.createArray(rows, columns)
    adjacencyList, intersectionNameDictionary = ImTrying.createAdjacencyList(array, rows, columns)

    run = True

    board = Grid(10, 10, array)
    board.add_adjacency_node_list(adjacencyList)

    show_path = False

    def redraw_window(window, show_path):
        window.fill((128, 128, 128))
        board.draw(window, type_of_path)
        text_font = pygame.font.SysFont("comicsans", 30)

        info = "Press 'r' to redo. Press 'b' to go back to main menu"
        project_info = text_font.render(info, 1, (255, 255, 255))
        window.blit(project_info, (WIDTH / 2 - project_info.get_width() / 2, HEIGHT - project_info.get_height()))

        if show_path:
            row_1, col_1 = board.find_first_selected()
            row_2, col_2 = board.find_second_selected()
            source = board.squares[row_1][col_1].node.intersectionName
            destination = board.squares[row_2][col_2].node.intersectionName
            if type_of_path == "Safest":
                board.draw_path(window, previous_map, destination, source, (0, 255, 0))
            elif type_of_path == "Shortest":
            	board.draw_path(window, previous_map, destination, source, (255, 69, 0))
            else:
                board.draw_path(window, previous_map_shortest, destination, source, (255, 69, 0))
                board.draw_path(window, previous_map_safest, destination, source, (0, 255, 0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_b:
                    run = False
                if event.key == pygame.K_r:
                    show_path = False
                    board.redo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                number_selected = board.selected_square((x, y))
                if number_selected == 1:
                    row_1, col_1 = board.find_first_selected()
                    source = board.squares[row_1][col_1].node.intersectionName
                    index = find_alist_index_from_array(array, source)
                    if type_of_path != "Both":
                        weight_map, previous_map = ImTrying.shortest_path_visual(adjacencyList, index, type_of_path)
                    else:
                        weight_map_shortest, previous_map_shortest = ImTrying.shortest_path_visual(adjacencyList, index,
                                                                                                   "Shortest")
                        weight_map_safest, previous_map_safest = ImTrying.shortest_path_visual(adjacencyList, index,
                                                                                               "Safest")
                if number_selected == 2:
                    show_path = True

        redraw_window(window, show_path)
        pygame.display.update()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    byline_font = pygame.font.SysFont("comicsans", 30)
    subtitle_font = pygame.font.SysFont("comicsans", 40)
    text_font = pygame.font.SysFont("comicsans", 30)
    game_font = pygame.font.SysFont("comicsans", 18)
    run = True
    while run:
        window.fill((255, 100, 100))
        title_label = title_font.render("SAFEST PATH FINDER", 1, (255, 255, 255))
        window.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, title_label.get_height()))

        byline_label = byline_font.render("Made by Team Trifecta", 1, (255, 255, 255))
        window.blit(byline_label, (WIDTH / 2 - byline_label.get_width() / 2, 1.8*title_label.get_height() +byline_label.get_height()))

        how_label = subtitle_font.render("How To Play:", 1, (255, 255, 255))
        window.blit(how_label,
                    (WIDTH / 2 - how_label.get_width() / 2, 3 * title_label.get_height() + how_label.get_height()))

        how_to_play = "Select two squares: first one is the source, second one is destination"
        project_info = text_font.render(how_to_play, 1, (255, 255, 255))
        window.blit(project_info, (
            WIDTH / 2 - project_info.get_width() / 2, 3.9 * title_label.get_height() + project_info.get_height()))

        safest_info = "Press 'd' to start the program looking for the safest path"
        project_info = text_font.render(safest_info, 1, (255, 255, 255))
        window.blit(project_info, (
            WIDTH / 2 - project_info.get_width() / 2, 4.2 * title_label.get_height() + 2 * project_info.get_height()))

        game_info = "(The numbers, 1 through 9, represent how dangerous that intersection, with 9 being the most dangerous)"
        project_info = game_font.render(game_info, 1, (255, 255, 255))
        window.blit(project_info, (
            WIDTH / 2 - project_info.get_width() / 2, 4.2 * title_label.get_height() + 6 * project_info.get_height()))

        shortest_info = "Press 's' to start the program looking for the shortest path"
        project_info = text_font.render(shortest_info, 1, (255, 255, 255))
        window.blit(project_info, (
            WIDTH / 2 - project_info.get_width() / 2, 4.8 * title_label.get_height() + 4 * project_info.get_height()))

        info = "Press 'b' to show both safest and shortest Path"
        project_info = text_font.render(info, 1, (255, 255, 255))
        window.blit(project_info, (
            WIDTH / 2 - project_info.get_width() / 2, 5.2 * title_label.get_height() + 5 * project_info.get_height()))

        infoSubtext = "(Green: Safest; Orange: Shortest)"
        infoSub_label = text_font.render(infoSubtext, 1, (255,255,255))
        window.blit(infoSub_label, (
            WIDTH / 2 - infoSub_label.get_width() / 2, 5.6 * title_label.get_height() + 5 * infoSub_label.get_height()))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    main_function("Safest")
                if event.key == pygame.K_s:
                    main_function("Shortest")
                if event.key == pygame.K_b:
                    main_function("Both")
                if event.key == pygame.K_q:
                    run = False
    pygame.quit()


main_menu()
