import sys
import pygame
from pygame.locals import *

from classes import *

# http://www.learningpython.com/2006/03/12/creating-a-game-in-python-using-pygame-part-one/
class PyManMain:
    '''The Main PyMan Class - This class handles the main
    initialization and creating of the Game.'''

    def __init__(self, width = 640, height = 480):
            pygame.init()
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((self.width,
                    self.height))

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

def test():
    ''' Check for configuration, then test module '''
    if not pygame.font: print 'Warning, fonts disabled'
    if not pygame.mixer: print 'Warning, sound disabled'


if __name__ == '__main__':
    test()
    MainWindow = PyManMain()
    MainWindow.main()
