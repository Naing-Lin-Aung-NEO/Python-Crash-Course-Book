# Starting the Game Project

# Creating a Pygame Window and Responding to User Input 

import sys

import pygame

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()

#         self.screen = pygame.display.set_mode((1200, 800))
#         pygame.display.set_caption("Alien Invasion")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()
    
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Controlling the Fram Rate/ Setting the Background color

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()

#         self.screen = pygame.display.set_mode((1200, 800))
#         self.clock = pygame.time.Clock()
#         pygame.display.set_caption("Alien Invasion")

#         # Set the background color 
#         self.bg_color = '#F0F8FF'

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             # Redraw the screen during each pass through the loop.
#             self.screen.fill(self.bg_color)

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()
#             self.clock.tick(50)
    
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Creating a Setting Class 

# from settings import Setting

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         # Set the background color 
#         self.bg_color = '#F0F8FF'

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             # Redraw the screen during each pass through the loop.
#             self.screen.fill(self.setting.bg_color)

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()
#             self.clock.tick(50)
    
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Adding the Ship Image / Creating Ship Class  

# from settings import Setting

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         # Set the background color 
#         self.bg_color = '#F0F8FF'

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             # Redraw the screen during each pass through the loop.
#             self.screen.fill(self.setting.bg_color)

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()
#             self.clock.tick(50)
    
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Creating The Ship Class 

# Drawing the Ship to the Screen 

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = '#F0F8FF'

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events 
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
            
#             # Redraw the screen during each pass through the loop.
#             self.screen.fill(self.setting.bg_color)
#             self.ship.blitme()

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()
#             self.clock.tick(50)
    
# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Refactoring

# _check_events() and _update_screen Methods 

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.setting.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Exercises 

# 12.1 Blue Sky / 12.2 Game Character

# from settings import Setting2
# from ship import Plane

# class AlienInvasion2:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting2()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")
#         self.ship = Plane(self)

#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
            
#             self._check_events()
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to key presses and mouse movements."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#     def _update_screen(self):
#         """Update images on the screen, flip to the new screen."""
#         self.screen.fill(self.bg_color)
#         self.ship.blitme()
#         pygame.display.flip()

# if __name__ == '__main__':
#     """Make an instance and run the game."""
#     ai = AlienInvasion2()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Piloting the Ship 

# Responding to a Keypress 

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RIGHT:
#                     # Move the ship to the right 
#                     self.ship.rect.x += 1 
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.setting.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Allowing Continuous Movement 

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self._update_screen()
#             self.ship.update()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RIGHT:
#                     self.ship.moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     self.ship.moving_left = True

#             elif event.type == pygame.KEYUP:
#                 if event.key == pygame.K_RIGHT:
#                     self.ship.moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     self.ship.moving_left = False
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.setting.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Adjusting the Ship's Speed 

from settings import Setting
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initilize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Setting()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color 
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(50)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
