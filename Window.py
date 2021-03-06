import pygame
from Gameplay import Gameplay
import time


class Window:
    # starting settings
    name = 'surviv'
    music_path = None

    def __init__(self):
        pygame.init()
        #setting window's namewe
        pygame.display.set_caption(self.name)

        self.gameplay = Gameplay()
        self.height = self.gameplay.get_screen_height()
        self.width = self.gameplay.get_screen_width()


        # to play a music in a background
        if self.music_path is not None:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.gameplay.set_screen(self.screen)

    def start(self):
        stopped = False
        clock = pygame.time.Clock()
        pygame.font.init()
        old_epoch = time.time()
        while not stopped:
            # Triggering events: using mouse and keyboard
            for event in pygame.event.get():
                self.gameplay.on_press(event)

                # Exiting a game either by closing event or by game option
                if event.type == pygame.QUIT or self.gameplay.has_quited():
                    #self.gameplay.quit()
                    stopped = True

            timedelta = 0.4*clock.tick(60)
            self.gameplay.play(timedelta)
            self.gameplay.draw()
            if (time.time() - old_epoch) >= self.gameplay.area_expansion_time:
                self.gameplay.extend_area_width()
                old_epoch = time.time()

            # refreshes screen
            pygame.display.flip()

