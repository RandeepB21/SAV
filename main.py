import pygame 
pygame.init() 
from list import * 
from DrawInformation import DrawInformation 
from sorting_algorithms import * 
from Drawing import * 
 
 
def main(): 
    run = True 
    clock = clock = pygame.time.Clock() 
 
 
    n = 50 
    min_val = 0 
    max_val = 100 
    sorting = False 
    ascending = True 
 
 
    sorting_algorithm = bubble_sort 
    sorting_algorithm_name = "Bubble Sort" 
    sorting_algorithm_generator = None 
 
 
    algorithm_names = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Shell Short", "Cocktain Sort"] 
    algorithms = [bubble_sort, insertion_sort, selection_sort, shell_sort, cocktain_sort] 
    i = 0 
 
 
    list = generate_starting_list(n, min_val, max_val) 
 
 
    draw_information = DrawInformation(800, 600, list) 
 
 
    while run: 
        clock.tick(60) 
 
 
        if sorting: 
            try: 
                next(sorting_algorithm_generator) 
 
 
            except StopIteration: 
                sorting = False 
        else: 
            draw(draw_information, sorting_algorithm_name, ascending) 
 
 
        for event in pygame.event.get(): 
 
 
            if event.type == pygame.QUIT: 
                run = False 
 
 
            if event.type != pygame.KEYDOWN: 
                continue 
 
 
            if event.key == pygame.K_r: 
                list = generate_starting_list(n, min_val, max_val) 
                draw_information.set_list(list) 
                sorting = False 
 
 
            elif event.key == pygame.K_SPACE and sorting == False: 
                sorting = True 
                sorting_algorithm_generator = sorting_algorithm(draw_information, ascending) 
 
 
            elif event.key == pygame.K_a and not sorting: 
                ascending = True 
 
 
            elif event.key == pygame.K_d and not sorting: 
                ascending = False 
 
 
            elif event.key == pygame.K_UP and not sorting: 
                if i != 0: 
 
 
                    i = (i - 1) % len(algorithm_names) 
                    sorting_algorithm = algorithms[i] 
                    sorting_algorithm_name = algorithm_names[i] 
 
 
            elif event.key == pygame.K_DOWN and not sorting: 
                i = (i + 1) % len(algorithm_names) 
                sorting_algorithm =  algorithms[i] 
                sorting_algorithm_name = algorithm_names[i] 
 
 
    pygame.quit() 
 
 
 
if __name__ == "__main__": 
    main() 
