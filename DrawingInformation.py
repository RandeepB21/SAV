import pygame 
import math 
 
class DrawInformation: 
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255) 
    GREEN = (0, 255, 0) 
    RED = (255, 0, 0) 
    BLUE = (0, 0, 255) 
    BACKGROUND_COLOUR = WHITE  
    GREYS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)] 
    SIDE_PADDING = 100 
    TOP_PADDING = 150 
    SMALL_FONT = pygame.font.SysFont('arial', 30) 
    LARGE_FONT = pygame.font.SysFont('arial', 40) 
 
    def __init__(self, width, height, list): 
        self.width = width 
        self.height = height 
        self.window = pygame.display.set_mode((width, height)) 
        pygame.display.set_caption("Sorting Algorithm Visualization") 
        self.set_list(list) 
 
    def set_list(self, list): 
        self.list = list 
        self.minimum_value = min(list) 
        self.maximum_value = max(list) 
        self.bar_width = round((self.width - self.SIDE_PADDING) / len(list)) 
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.maximum_value - self.minimum_value)) 
        self.start_x = self.SIDE_PADDING // 2 
 
