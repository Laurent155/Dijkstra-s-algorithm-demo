from dijkstra import *
import pygame


def transform_pos(pos):
    pos_mod = [0, 0]
    pos_mod[0] = pos[0] // 20
    pos_mod[1] = pos[1] // 20

    return pos_mod


def add_obstacle(obs, vertex):
    if vertex not in obs:
        obs.append(vertex)


def remove_obstacle(obs, vertex):
    if vertex in obs:
        obs.remove(vertex)


def set_destinations(event, start, end, c):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            start = True
            c += 1
            print(c)
        elif event.key == pygame.K_e:
            end = not end


def main():
    set_up_graph = True
    win.fill((255, 255, 255))
    draw_window(win)
    pygame.display.update()
    start_vertex = [-1, -1]
    end_vertex = [-1, -1]
    obstacles = []
    set_start = False
    set_end = False
    g = Graph()
    while set_up_graph:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    set_start = not set_start
                elif event.key == pygame.K_e:
                    set_end = not set_end
                elif event.key == pygame.K_b:
                    set_up_graph = False
            if pygame.mouse.get_pressed()[0] and (set_start, set_end) == (True, False):
                vertex = transform_pos(pygame.mouse.get_pos())
                start_vertex = vertex
            if pygame.mouse.get_pressed()[0] and (set_start, set_end) == (False, True):
                vertex = transform_pos(pygame.mouse.get_pos())
                end_vertex = vertex
            if pygame.mouse.get_pressed()[0] and (set_start, set_end) == (False, False):
                vertex = transform_pos(pygame.mouse.get_pos())
                add_obstacle(obstacles, vertex)
            elif pygame.mouse.get_pressed()[2] and (set_start, set_end) == (False, False):
                vertex = transform_pos(pygame.mouse.get_pos())
                remove_obstacle(obstacles, vertex)
        win.fill((255, 255, 255))
        update_window(win, start_vertex, end_vertex, obstacles)
        pygame.display.update()
    create_graph(g, obstacles)
    d = dijkstra_algorithm(g, start_vertex, end_vertex)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        final_update(win, start_vertex, end_vertex, obstacles, d[-1], d[1])



main()
