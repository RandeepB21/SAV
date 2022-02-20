import pygame 
from DrawInformation import DrawInformation 
 
def draw(drawing_info, algoritm_name, ascending): 
    drawing_info.window.fill(drawing_info.BACKGROUND_COLOUR) 
 
    title = drawing_info.LARGE_FONT.render(f"{algoritm_name} - {'Ascending' if ascending else 'Descending'}", 1, drawing_info.RED) 
    drawing_info.window.blit(title, (drawing_info.width/2 - title.get_width()/2, 5)) 
 
    controls = drawing_info.SMALL_FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, drawing_info.BLUE) 
    drawing_info.window.blit(controls, (drawing_info.width/2 - controls.get_width()/2, 60)) 
 
    draw_list(drawing_info) 
    pygame.display.update() 
 
def draw_list(drawing_info, colour_positions = {}, clear_background = False): 
    list = drawing_info.list 
 
    if clear_background: 
        clear_rectangle = (drawing_info.SIDE_PADDING//2, drawing_info.TOP_PADDING, drawing_info.width - drawing_info.SIDE_PADDING, drawing_info.height - drawing_info.TOP_PADDING) 
        pygame.draw.rect(drawing_info.window, drawing_info.BACKGROUND_COLOUR, clear_rectangle) 
 
    for i, value in enumerate(list): 
        x = drawing_info.start_x + i * drawing_info.bar_width 
        height = (value - drawing_info.minimum_value) * drawing_info.block_height 
        y = drawing_info.height - height 
        colour = drawing_info.GREYS[i % 3] 
 
        if i in colour_positions: 
            colour = colour_positions[i] 
 
        pygame.draw.rect(drawing_info.window, colour, (x, y, drawing_info.bar_width, height)) 
 
 
    if clear_background: 
        pygame.display.update() 
