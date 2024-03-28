import pygame
import sys
from GameController import GameController
from objects.bg_stars import StarObj, set_star_list, all_star_move

class GameView:
    def __init__(self, title : str, size : tuple[int, int]):
        """
        Set window title, along with width and height with the assigned tuple
        """
        self.width = size[0]
        self.height = size[1]
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.game_objects = []  # List to store all game objects
        self.fps = 60 # Sets default target frame rate

    def add_game_object(self, game_object):
        """
        Adds a game object to be drawn by the game.
        """
        self.game_objects.append(game_object)

    def update_controller(self, controller = GameController):
        # TODO - Register player's moves with the controller object
        for object in self.game_objects:
            if object.is_player:
                controller.register_action(pygame.K_LEFT, object.move_left)
                controller.register_action(pygame.K_RIGHT, object.move_right)
                # TODO - Implement logic for remaining controls 
        return controller

    def run(self):
        """
        Runs game, checks events and draws objects
        """
        # Create a contorler object and then update it to register all player moves
        controller = GameController()
        controller = self.update_controller(controller)
        clock_tick = self.clock.tick(self.fps)  # set frame rate limit

        # Sets number of stars to be drawn in background
        total_stars = 250

        # List of boolean values used to determine if the star is near of far.
        starlist = [] 
        if len(starlist) == 0:
            starlist = set_star_list(self.width, self.height, starlist, total_stars)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))  # Clear screen with black

            # Draw stars on screen and move them
            all_star_move(starlist, self.screen, (self.width, self.height), clock_tick)

            # Updates all objects associated with controller
            controller.handle_keys(pygame.key.get_pressed(), clock_tick)

            # Draw all game objects
            for game_object in self.game_objects:
                game_object.move()
                game_object.draw(self.screen)

            pygame.display.flip()
            
