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


# Adjusting the Ship's Speed / Limiting the Ship's Range

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

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
#         self.screen.fill(self.settings.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Refactoring _check_events()

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

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
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Pressing Q to Quit / Running the Game in Fullscreen Mode 

# from settings import Setting
# from ship import Ship

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#         self.settings.screen_width = self.screen.get_rect().width
#         self.settings.screen_height = self.screen.get_rect().height
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

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
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Exercises 

# 12.3 Pygame Documentation

# https://pygame.org 
# https://pygame./docs


# 12.4 Rocket 

# class Setting:
#     """Make setting for the game rocket."""
    
#     def __init__(self):
#         """Initialize game settings."""
#         # Screen Setting 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Setting 
#         self.ship_speed = 1.5

# class Rocket:
#     """A class to manage the rocket."""

#     def __init__(self, rc_game):
#         """Initialize the rocket and set tis starting position."""
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
#         self.screen_rect = rc_game.screen.get_rect()

#         # Load the iamge and ge its rect 
#         self.image = pygame.image.load('images/fighter_plane.bmp')
#         self.rect = self.image.get_rect()

#         # Start new ship at the center of the screen 
#         self.rect.center = self.screen_rect.center

#         # Store a float for the ship's exact horizontal and vartical position
#         self.x = float(self.rect.x)
#         self.y = float(self.rect.y)

#         # Movement flag; start with a ship that's not moving
#         self.moving_right = False
#         self.moving_left = False
#         self.moving_up = False
#         self.moving_down = False

#     def update(self):
#         """Update the ship's position based on the movement flag."""
#         # Update the ship's x and y value, not the rect 
#         if self.moving_right and self.rect.right < self.screen_rect.right:
#             self.x += self.setting.ship_speed
#         if self.moving_left and self.rect.left > 0:
#             self.x -= self.setting.ship_speed
#         if self.moving_up and self.rect.top > 0:
#             self.y -= self.setting.ship_speed
#         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
#             self.y += self.setting.ship_speed

#         # Update rect object from slef.x
#         self.rect.x = self.x 
#         self.rect.y = self.y 
    
#     def blitme(self):
#         """Draw the image at its current loaction."""
#         self.screen.blit(self.image, self.rect)

# class RocketGame:
#     """Model for a rocket game and it's resources."""

#     def __init__(self):
#         """Initialize the game and attributes for the game."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#         self.screen_width = self.screen.get_rect().width
#         self.screen_height = self.screen.get_rect().height
#         pygame.display.set_caption('Rocket Game')

#         self.rocket = Rocket(self)

#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the Main Loop for the Game."""
#         while True:
#             self._check_events()
#             self._update_screen()
#             self.rocket.update()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to key presses."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to key pressed."""
#         if event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = True 
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = True
#         elif event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True
#         elif event.key == pygame.K_q:
#             sys.exit()

#     def _check_keyup_events(self, event):
#         """Respond to key released."""
#         if event.key == pygame.K_RIGHT:
#             self.rocket.moving_right = False 
#         elif event.key == pygame.K_LEFT:
#             self.rocket.moving_left = False
#         elif event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False

#     def _update_screen(self):
#         """Draw image at the screen and flip to the new screen."""
#         self.screen.fill(self.bg_color)
#         self.rocket.blitme()
        
#         pygame.display.flip()

# if __name__ == '__main__':
#     rocket = RocketGame()
#     rocket.run_game()


# 12.5 Keys 

# class Keys:

#     def __init__(self):
#         pygame.init()

#         self.screen = pygame.display.set_mode((1200, 700))
#         pygame.display.set_caption("KEYS")

#     def run_file(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         sys.exit()
#                     else:
#                         print(event.key)

# if __name__ == '__main__':
#     keys = Keys()
#     keys.run_file()


# -----------------------------------------------------------------------------

# Shooting Bullets/ Storing Bullets in a Group/ Firing Bullets 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self.bullets.update()
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# from settings import Setting
# from ship import Ship
# from bullet import Bullet

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self.bullets.update()

#             # Get rid of bullets that have disappeared.
#             for bullet in self.bullets.copy():
#                 if bullet.rect.bottom <= 0:
#                     self.bullets.remove(bullet)
#             # print(len(self.bullets))

#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()



# Limiting the Number of Bullets / Creating the _update_bullets() method

# from settings import Setting
# from ship import Ship
# from bullet import Bullet

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self._update_bullets()            
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)
    
#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positons.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# 12.6 Sideways Shooter 

# from pygame.sprite import Sprite
# class Setting:
#     """Make setting for the game rocket."""
    
#     def __init__(self):
#         """Initialize game settings."""
#         # Screen Setting 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Setting 
#         self.ship_speed = 1.5

#         # Bullet Settings 
#         self.bullet_speed = 2.0

# class Bullet(Sprite):
#     """A class manage bullets fired from the ship."""
    
#     def __init__(self, rc_game):
#         super().__init__()
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
        
#         # Load the image and get its rect 
#         self.bullet_image = pygame.image.load('images/bullet_red.bmp')
#         self.bullet_image_size = pygame.transform.scale(self.bullet_image, (30, 25))
#         self.bullet_rect = self.bullet_image_size.get_rect()
#         self.bullet_rect.midleft = rc_game.rocket.rect.midleft
#         self.bullet_rect.x += 100

#         # Stor the bullet's position as a float.
#         self.x = float(self.bullet_rect.x)

#     def update(self):
#         """Move the bullet up the screen."""
#         # Update the exact position of the bullet.
#         self.x += self.setting.bullet_speed
#         # Update the rect position
#         self.bullet_rect.x = self.x
    
#     def blit_bullet(self):
#         """Draw the image to the screen."""
#         self.screen.blit(self.bullet_image_size, self.bullet_rect)

# class Rocket:
#     """A class to manage the rocket."""

#     def __init__(self, rc_game):
#         """Initialize the rocket and set tis starting position."""
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
#         self.screen_rect = rc_game.screen.get_rect()

#         # Load the iamge and ge its rect 
#         self.image = pygame.image.load('images/fighter_plane.bmp')
#         self.image_rotate = pygame.transform.rotate(self.image, -90)
#         self.image_resize = pygame.transform.scale(self.image_rotate, (125, 100))
#         self.rect = self.image_resize.get_rect()

#         # Start new ship at the center of the screen 
#         self.rect.midleft = self.screen_rect.midleft

#         # Store a float for the ship's exact vartical position
#         self.y = float(self.rect.y)

#         # Movement flag; start with a ship that's not moving
#         self.moving_up = False
#         self.moving_down = False

#     def update(self):
#         """Update the ship's position based on the movement flag."""
#         # Update the ship's x and y value, not the rect 
#         if self.moving_up and self.rect.top > 0:
#             self.y -= self.setting.ship_speed
#         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
#             self.y += self.setting.ship_speed

#         # Update rect object from slef.x
#         self.rect.y = self.y 
    
#     def blitme(self):
#         """Draw the image at its current loaction."""
#         self.screen.blit(self.image_resize, self.rect)

# class RocketGame:
#     """Model for a rocket game and it's resources."""

#     def __init__(self):
#         """Initialize the game and attributes for the game."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#         self.screen_width = self.screen.get_rect().width
#         self.screen_height = self.screen.get_rect().height
#         pygame.display.set_caption('Rocket Game')

#         self.rocket = Rocket(self)
#         self.bullets = pygame.sprite.Group()

#         self.bg_color = self.setting.bg_color

#     def run_game(self):
#         """Start the Main Loop for the Game."""
#         while True:
#             self._check_events()
#             self.rocket.update()
#             self._update_bullet()
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to key presses."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to key pressed."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()

#     def _check_keyup_events(self, event):
#         """Respond to key released."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)

#     def _update_bullet(self):
#         # Update bullet positions
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.bullet_rect.right >= self.screen.get_rect().right:
#                 self.bullets.remove(bullet)



#     def _update_screen(self):
#         """Draw image at the screen and flip to the new screen."""
#         self.screen.fill(self.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.blit_bullet()
#         self.rocket.blitme()
        
#         pygame.display.flip()

# if __name__ == '__main__':
#     rocket = RocketGame()
#     rocket.run_game()

# -----------------------------------------------------------------------------

# Chapter 13 

# AlIENS!

# Creating an Instance of the Alien 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self._update_bullets()            
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)
    
#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positons.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
    
#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Make an alien 
#         alien = Alien(self)
#         self.aliens.add(alien)
    
#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()



# Building the Alien Fleet 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self._update_bullets()            
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)
    
#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positons.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
    
#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left 
#         # Spacing between aliens is one alien width  
#         alien = Alien(self)
#         alien_width = alien.rect.width

#         current_x = alien_width
#         while current_x < (self.settings.screen_width - 2 * alien_width):
#             new_alien = Alien(self)
#             new_alien.x = current_x
#             new_alien.rect.x = current_x
#             self.aliens.add(new_alien)
#             current_x += 2 * alien_width


#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Refactoring _create_fleet()


# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien

# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initilize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()
        
#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Set the background color 
#         self.bg_color = self.settings.bg_color

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:

#             self._check_events()
#             self.ship.update()
#             self._update_bullets()            
#             self._update_screen()
#             self.clock.tick(50)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respont to key presses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()
    
#     def _check_keyup_events(self, event):
#         """Respont to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False
    
#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)
    
#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positons.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
    
#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left 
#         # Spacing between aliens is one alien width  
#         alien = Alien(self)
#         alien_width = alien.rect.width

#         current_x = alien_width
#         while current_x < (self.settings.screen_width - 2 * alien_width):
#             self._create_alien(current_x)
#             current_x += 2 * alien_width

#     def _create_alien(self, x_position):
#         # Create a alien and place it in the row.
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         self.aliens.add(new_alien)


#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()

# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Adding Rows 


# import sys

# import pygame

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Exercises 

# 13.1 Stars 

# import sys 
# import pygame
# from pygame.sprite import Sprite

# class Setting:
#     """Settings for the star game."""
    
#     def __init__(self):
#         """Initialize for the settings of screen."""
#         self.screen_width = 1300
#         self.screen_height = 700
#         self.bg_color = (0, 0, 0)

# class Star(Sprite):
#     """Create the star."""

#     def __init__(self, star_game):
#         """Initialize the star attributes."""
#         super().__init__()
#         self.screen = star_game.screen

#         # Load the image and get its rect 
#         self.image = pygame.image.load('images/star.png')
#         self.rect = self.image.get_rect()

#         # Start each new star with the top-left position
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.height


# class StarGame():
#     """To make Star game"""

#     def __init__(self):
#         """Initialize the game and the resources."""
#         pygame.init()

#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Star Game")

#         self.stars = pygame.sprite.Group()
#         self._create_fleet()
    
#     def run_game(self):
#         """Run the game by main loop."""
#         while True:
#             self._check_events()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Check the events for the game."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_event(event)
                
#     def _check_keydown_event(self, event):
#         """Check the key presses."""
#         if event.key == pygame.K_q:
#             sys.exit()

#     def _create_fleet(self):
#         """Create the star."""
#         star = Star(self)
#         star_width, star_height = star.rect.size

#         current_x, current_y = 2 * star_width, 2 * star_height
#         while current_y < (self.setting.screen_height - 3 * star_height):
#             while current_x < (self.setting.screen_width - 2 * star_width):
#                 self._create_star(current_x, current_y)
#                 current_x += 2 * star_width

#             # Get a row; rest x position and increment y position
#             current_x = 2* star_width
#             current_y += 2 * star_height

#     def _create_star(self, x, y):
#         """create the stars."""
#         new_star = Star(self)
#         new_star.rect.x = x
#         new_star.rect.y = y
#         self.stars.add(new_star)

#     def _update_screen(self):
#         """Update the screen."""
#         self.screen.fill(self.setting.bg_color)
#         self.stars.draw(self.screen)
#         pygame.display.flip()


# if __name__ == '__main__':
#     """Create the instance and run the game."""
#     star_game = StarGame()
#     star_game.run_game()


# 13.2 Better Stars 

# import sys 
# import pygame
# from pygame.sprite import Sprite

# from random import randint

# class Setting:
#     """Settings for the star game."""
    
#     def __init__(self):
#         """Initialize for the settings of screen."""
#         self.screen_width = 1300
#         self.screen_height = 700
#         self.bg_color = (0, 0, 0)

# class Star(Sprite):
#     """Create the star."""

#     def __init__(self, star_game):
#         """Initialize the star attributes."""
#         super().__init__()
#         self.screen = star_game.screen

#         # Load the image and get its rect 
#         self.image = pygame.image.load('images/star.png')
#         self.rect = self.image.get_rect()

#         # Start each new star with the top-left position
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.height


# class StarGame():
#     """To make Star game"""

#     def __init__(self):
#         """Initialize the game and the resources."""
#         pygame.init()

#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.setting.screen_width, self.setting.screen_height)
#         )
#         pygame.display.set_caption("Star Game")

#         self.stars = pygame.sprite.Group()
#         self._create_fleet()
    
#     def run_game(self):
#         """Run the game by main loop."""
#         while True:
#             self._check_events()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Check the events for the game."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_event(event)
                
#     def _check_keydown_event(self, event):
#         """Check the key presses."""
#         if event.key == pygame.K_q:
#             sys.exit()

#     def _create_fleet(self):
#         """Create the star."""
#         star = Star(self)
#         star_width, star_height = star.rect.size

#         current_x, current_y = 2 * star_width, 2 * star_height
#         while current_y < (self.setting.screen_height - 3 * star_height):
#             while current_x < (self.setting.screen_width - 2 * star_width):
#                 self._create_star(current_x, current_y)
#                 current_x += 2 * star_width

#             # Get a row; rest x position and increment y position
#             current_x = 2* star_width
#             current_y += 2 * star_height

#     def _create_star(self, x, y):
#         """create the stars."""
#         new_star = Star(self)
#         new_star.rect.x = x + self._get_star_offset()
#         new_star.rect.y = y + self._get_star_offset()
#         self.stars.add(new_star)

#     def _get_star_offset(self):
#         offset_size = 15
#         return randint(-1*offset_size, offset_size)

#     def _update_screen(self):
#         """Update the screen."""
#         self.screen.fill(self.setting.bg_color)
#         self.stars.draw(self.screen)
#         pygame.display.flip()


# if __name__ == '__main__':
#     """Create the instance and run the game."""
#     star_game = StarGame()
#     star_game.run_game()


# -----------------------------------------------------------------------------

# Making the Fleet Move 

# Moving the Alien Right 
# Creating Settings for the Fleet Direction 
# Checking Whether an Alien Has Hit the Edge 
# Dropping the Fleet and Changing Direction 

# import pygame

# import sys 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------


# Exercises 

# 13.3 Raindrops / 13.4 Steady Raindrops

# import sys 

# import pygame
# from pygame.sprite import Sprite

# class Setting:
#     """Set settings for raindrop game."""

#     def __init__(self):
#         """Initialize the attributes for the game."""
#         self.screen_width = 1300
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Set the speed of raindrop 
#         self.raindrop_speed = 1.5


# class RainDrop(Sprite):
#     """Create a model of raindrop."""

#     def __init__(self, rd_game):
#         """Initialize the attributes for the raindrop."""
#         super().__init__()
#         self.screen = rd_game.screen
#         self.settings = rd_game.settings

#         # Load the raindrop image 
#         self.image = pygame.image.load('images/raindrop.png')
#         self.rect = self.image.get_rect()

#         # Place the raindrop from the top-left of the screen.
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.height

#         # Store the exact vertical position
#         self.y = float(self.rect.y)

#     def check_disappeared(self):
#         """Check if drop has disappeared off bottom of screen."""
#         if self.rect.top > self.screen.get_rect().bottom:
#             return True
#         else:
#             return False

#     def update(self):
#         """Update the raindrop position."""
#         self.y += self.settings.raindrop_speed
#         self.rect.y = self.y 


# class RainDropGame():
#     """Overall class manage game assets and behaviors."""

#     def __init__(self):
#         """Initialize the game and create the game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height)
#         )
#         pygame.display.set_caption("RainDrop Game")

#         self.raindrops = pygame.sprite.Group()
#         self._create_drops()


#     def run_game(self):
#         """Run the game with the main loop."""
#         while True:
#             self._check_events()
#             self._update_raindrops()
#             self._update_screen()
#             self.clock.tick(60)

    
#     def _check_events(self):
#         """Respond the key events and mouse presses."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
                
    
#     def _check_keydown_events(self, event):
#         """Respond to key presses."""
#         if event.key == pygame.K_q:
#             sys.exit()

    
#     def _create_drops(self):
#         """Create a sky full of raindrops."""
#         drop = RainDrop(self)
#         drop_width, drop_height = drop.rect.size

#         current_x, current_y = drop_width, drop_height
#         while current_y < (self.settings.screen_height - 2 * drop_height):
#             while current_x < (self.settings.screen_width - 2 * drop_width):
#                 self._create_drop(current_x, current_y)
#                 current_x += 2 * drop_width

#             # Finished a row and reset the current_x and set new y position
#             current_x = drop_width
#             current_y += 2 * drop_height


#     def _create_drop(self, current_x, current_y):
#         """Create the drop and place in the grid."""
#         new_drop = RainDrop(self)
#         new_drop.y = current_y
#         new_drop.rect.x = current_x
#         new_drop.rect.y = current_y 
#         self.raindrops.add(new_drop)

#     def _create_new_row(self):
#         """Create a new row after the row disappaered."""
#         drop = RainDrop(self)
#         drop_width, drop_height = drop.rect.size

#         current_x = drop_width
#         current_y = -1 * drop_height
#         while current_x < (self.settings.screen_width - 2 * drop_width):
#             self._create_drop(current_x, current_y)
#             current_x += 2 * drop_width

#     def _update_raindrops(self):
#         """Update drop positions, and look for drops that have disappeared."""
#         self.raindrops.update()

#         # Assume we won't make new drops 
#         make_new_drops = False
#         for drop in self.raindrops.copy():
#             if drop.check_disappeared():
#                 # Remove this drop, and we'll need to make new drops
#                 self.raindrops.remove(drop)
#                 make_new_drops = True
        
#         # Make a new row of drops if needed.
#         if make_new_drops:
#             self._create_new_row()


#     def _update_screen(self):
#         """Update the images on the screen, and flip to new screen."""
#         self.screen.fill(self.settings.bg_color)
#         self.raindrops.draw(self.screen)
        
#         pygame.display.flip()
        


# if __name__ == '__main__':
#     """Make a game instance and run the game."""
#     rd_game = RainDropGame()
#     rd_game.run_game()


# -----------------------------------------------------------------------------


# Shooting Aliens 
# Detecting Bullet Collisions 
# Making Larger Bullets for testing 

# import pygame

# import sys 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#         # Check for any bullets that have hit aliens 
#         # If so, get rid of the bullet and the alien 
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Repopulating the Fleet 
# Speeding Up the Bullets 

# import pygame

# import sys 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)

#         # Check for any bullets that have hit aliens 
#         # If so, get rid of the bullet and the alien 
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new Fleet 
#             self.bullets.empty()
#             self._create_fleet()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Refactoring _update_bullets() 

# import pygame

# import sys 

# from settings import Setting
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Exercises

# 13.5 Sideways Shooter Part 2 

# import sys

# import pygame

# from random import random

# from pygame.sprite import Sprite
# class Setting:
#     """Make setting for the game rocket."""
    
#     def __init__(self):
#         """Initialize game settings."""
#         # Screen Setting 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Setting 
#         self.ship_speed = 1.5

#         # Bullet Settings 
#         self.bullet_speed = 2.0

#         # Alien settings 
#         self.alien_speed = 1 
#         self.alien_frequency = 0.008
#         self.fleet_drop_speed = 10
#         # fleet direction of 1 represent bottom; -1 represent top 
#         self.fleet_direction = 1

# class Bullet(Sprite):
#     """A class manage bullets fired from the ship."""
    
#     def __init__(self, rc_game):
#         super().__init__()
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
        
#         # Load the image and get its rect 
#         self.bullet_image = pygame.image.load('images/bullet_red.bmp')
#         self.bullet_image_size = pygame.transform.scale(self.bullet_image, (30, 25))
#         self.rect = self.bullet_image_size.get_rect()
#         self.rect.midleft = rc_game.rocket.rect.midleft
#         self.rect.x += 100

#         # Stor the bullet's position as a float.
#         self.x = float(self.rect.x)

#     def update(self):
#         """Move the bullet up the screen."""
#         # Update the exact position of the bullet.
#         self.x += self.setting.bullet_speed
#         # Update the rect position
#         self.rect.x = self.x
    
#     def blit_bullet(self):
#         """Draw the image to the screen."""
#         self.screen.blit(self.bullet_image_size, self.rect)

# class Rocket:
#     """A class to manage the rocket."""

#     def __init__(self, rc_game):
#         """Initialize the rocket and set tis starting position."""
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
#         self.screen_rect = rc_game.screen.get_rect()

#         # Load the iamge and ge its rect 
#         self.image = pygame.image.load('images/fighter_plane.bmp')
#         self.image_rotate = pygame.transform.rotate(self.image, -90)
#         self.image_resize = pygame.transform.scale(self.image_rotate, (125, 100))
#         self.rect = self.image_resize.get_rect()

#         # Start new ship at the center of the screen 
#         self.rect.midleft = self.screen_rect.midleft

#         # Store a float for the ship's exact vartical position
#         self.y = float(self.rect.y)

#         # Movement flag; start with a ship that's not moving
#         self.moving_up = False
#         self.moving_down = False

#     def update(self):
#         """Update the ship's position based on the movement flag."""
#         # Update the ship's x and y value, not the rect 
#         if self.moving_up and self.rect.top > 0:
#             self.y -= self.setting.ship_speed
#         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
#             self.y += self.setting.ship_speed

#         # Update rect object from slef.x
#         self.rect.y = self.y 

#     def center_ship(self):
#         """Center the ship on the screen."""
#         self.rect.midleft = self.screen_rect.midleft
#         self.y = float(self.rect.y)
    
#     def blitme(self):
#         """Draw the image at its current loaction."""
#         self.screen.blit(self.image_resize, self.rect)



# class Alien(Sprite):
#     """A class to represent a single alien in the fleet."""

#     def __init__(self, rc_game):
#         """Initialize the alien and set its starting position."""
#         super().__init__()
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting

#         # Load the alien image and set its rect attribute 
#         self.image = pygame.image.load('images/ufo.bmp')
#         self.image = pygame.transform.scale(self.image, (80, 80))
#         self.rect = self.image.get_rect()

#         # Start each new alien near the top left of the screen 
#         screen_rect = self.screen.get_rect()
#         self.rect.x = screen_rect.right - self.rect.width * 2  
#         self.rect.y = self.rect.height                        


#         # Store the alien's exact vertical position
#         self.y = float(self.rect.y)
    
#     def check_edges(self):
#         """Returen True if alien is at edge of screen."""
#         screen_rect = self.screen.get_rect()
#         return(self.rect.top <= 0) or (self.rect.bottom >= screen_rect.bottom)
    
#     def update(self):
#         """Move the alien to the top of bottom."""
#         self.y += self.setting.alien_speed * self.setting.fleet_direction
#         self.rect.y = self.y
        

# class RocketGame:
#     """Model for a rocket game and it's resources."""

#     def __init__(self):
#         """Initialize the game and attributes for the game."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode((
#             self.setting.screen_width, self.setting.screen_height))
#         self.screen_width = self.screen.get_rect().width
#         self.screen_height = self.screen.get_rect().height
#         pygame.display.set_caption('Rocket Game')

#         self.rocket = Rocket(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the Main Loop for the Game."""
#         while True:
#             self._check_events()
#             self.rocket.update()
#             self._update_bullet()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to key presses."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to key pressed."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()

#     def _check_keyup_events(self, event):
#         """Respond to key released."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)

#     def _update_bullet(self):
#         # Update bullet positions
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.left >= self.screen.get_rect().right:
#                 self.bullets.remove(bullet)
            
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
    
#     def _create_fleet(self):
#         """Create a grid of aliens in columns starting at the right end."""
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         screen_width = self.setting.screen_width
#         screen_height = self.setting.screen_height

#         left_margin = self.rocket.rect.right + 50

#         # Start from right side with padding of one alien width
#         start_x = screen_width - alien_width - 20

#         # Loop columns from right to left
#         current_x = start_x
#         while current_x > left_margin:
#             current_y = alien_height  
#             while current_y < (screen_height - alien_height):
#                 self._create_alien(current_x, current_y)
#                 current_y += 2 * alien_height  
#             current_x -= 2 * alien_width  
    
#     def _create_alien(self, x, y):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.y = y 
#         new_alien.rect.x = x 
#         new_alien.rect.y = y 
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break

#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.x -= self.setting.fleet_drop_speed
#         self.setting.fleet_direction *= -1

#     def _update_screen(self):
#         """Draw image at the screen and flip to the new screen."""
#         self.screen.fill(self.setting.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.blit_bullet()
#         self.rocket.blitme()
#         self.aliens.draw(self.screen)
        
#         pygame.display.flip()

# if __name__ == '__main__':
#     rocket = RocketGame()
#     rocket.run_game()


# -----------------------------------------------------------------------------

# Ending the Game 

# Detecting Alien-Ship Collisions
# Responding to Alien-Ship Collisions 
# Aliens that Reach the bottom of the Screen 

# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         self.stats = GameStats(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()
#             self.ship.update()
#             self._update_bullets()
#             self._update_aliens()
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         # Decrement ships_left.
#         self.stats.ships_left -= 1 

#         # Get rid of any remaining bullets and aliens 
#         self.bullets.empty()
#         self.aliens.empty()

#         # Create a new fleet and center the ship 
#         self._create_fleet()
#         self.ship.center_ship()

#         # pause
#         sleep(0.5)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Game Over !
# Indentifying Which parts of the game should run 

# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         self.stats = GameStats(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an active state.
#         self.game_active = True

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left.
#             self.stats.ships_left -= 1 

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Exercises 

# 13.6 Game Over 

# from time import sleep

# import sys

# import pygame
# from pygame.sprite import Sprite
# class Setting:
#     """Make setting for the game rocket."""
    
#     def __init__(self):
#         """Initialize game settings."""
#         # Screen Setting 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Setting 
#         self.ship_speed = 1.5
#         self.ship_limit = 3

#         # Bullet Settings 
#         self.bullet_speed = 2.0

#         # Alien settings 
#         self.alien_speed = 3
#         self.fleet_drop_speed = 12
#         # fleet direction of 1 represent bottom; -1 represent top 
#         self.fleet_direction = 2


# class GameStats:
#     """Track statistics for Rocket Game."""
#     def __init__(self, rc_game):
#         """Intiliaze statistics."""
#         self.setting = rc_game.setting
#         self.reset_stats()

#     def reset_stats(self):
#         """Initialize statistics that can change during the game."""
#         self.ships_left = self.setting.ship_limit


# class Bullet(Sprite):
#     """A class manage bullets fired from the ship."""
    
#     def __init__(self, rc_game):
#         super().__init__()
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
        
#         # Load the image and get its rect 
#         self.bullet_image = pygame.image.load('images/bullet_red.bmp')
#         self.bullet_image_size = pygame.transform.scale(self.bullet_image, (30, 25))
#         self.rect = self.bullet_image_size.get_rect()
#         self.rect.midleft = rc_game.rocket.rect.midleft
#         self.rect.x += 100

#         # Stor the bullet's position as a float.
#         self.x = float(self.rect.x)

#     def update(self):
#         """Move the bullet up the screen."""
#         # Update the exact position of the bullet.
#         self.x += self.setting.bullet_speed
#         # Update the rect position
#         self.rect.x = self.x
    
#     def blit_bullet(self):
#         """Draw the image to the screen."""
#         self.screen.blit(self.bullet_image_size, self.rect)

# class Rocket:
#     """A class to manage the rocket."""

#     def __init__(self, rc_game):
#         """Initialize the rocket and set tis starting position."""
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting
#         self.screen_rect = rc_game.screen.get_rect()

#         # Load the iamge and ge its rect 
#         self.image = pygame.image.load('images/fighter_plane.bmp')
#         self.image_rotate = pygame.transform.rotate(self.image, -90)
#         self.image_resize = pygame.transform.scale(self.image_rotate, (125, 100))
#         self.mask = pygame.mask.from_surface(self.image_resize)
#         self.rect = self.image_resize.get_rect()

#         # Start new ship at the center of the screen 
#         self.rect.midleft = self.screen_rect.midleft

#         # Store a float for the ship's exact vartical position
#         self.y = float(self.rect.y)

#         # Movement flag; start with a ship that's not moving
#         self.moving_up = False
#         self.moving_down = False

#     def update(self):
#         """Update the ship's position based on the movement flag."""
#         # Update the ship's x and y value, not the rect 
#         if self.moving_up and self.rect.top > 0:
#             self.y -= self.setting.ship_speed
#         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
#             self.y += self.setting.ship_speed

#         # Update rect object from slef.x
#         self.rect.y = self.y 

#     def center_ship(self):
#         """Center the ship on the screen."""
#         self.rect.midleft = self.screen_rect.midleft
#         self.y = float(self.rect.y)
    
#     def blitme(self):
#         """Draw the image at its current loaction."""
#         self.screen.blit(self.image_resize, self.rect)



# class Alien(Sprite):
#     """A class to represent a single alien in the fleet."""

#     def __init__(self, rc_game):
#         """Initialize the alien and set its starting position."""
#         super().__init__()
#         self.screen = rc_game.screen
#         self.setting = rc_game.setting

#         # Load the alien image and set its rect attribute 
#         self.image = pygame.image.load('images/ufo.bmp')
#         self.image = pygame.transform.scale(self.image, (80, 80))
#         self.rect = self.image.get_rect()

#         # Start each new alien near the top left of the screen 
#         screen_rect = self.screen.get_rect()
#         self.rect.x = screen_rect.right - self.rect.width * 2  
#         self.rect.y = self.rect.height                        


#         # Store the alien's exact vertical position
#         self.y = float(self.rect.y)
    
#     def check_edges(self):
#         """Returen True if alien is at edge of screen."""
#         screen_rect = self.screen.get_rect()
#         return (
#             self.rect.top <= 0
#             or self.rect.bottom >= screen_rect.bottom
#             or self.rect.left <= 0
#             or self.rect.right >= screen_rect.right
#         )


#     def update(self):
#         """Move the alien to the top of bottom."""
#         self.y += self.setting.alien_speed * self.setting.fleet_direction
#         self.rect.y = self.y
        

# class RocketGame:
#     """Model for a rocket game and it's resources."""

#     def __init__(self):
#         """Initialize the game and attributes for the game."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.setting = Setting()

#         self.screen = pygame.display.set_mode((
#             self.setting.screen_width, self.setting.screen_height))
#         self.screen_width = self.screen.get_rect().width
#         self.screen_height = self.screen.get_rect().height
#         pygame.display.set_caption('Rocket Game')

#         # Create instance to store game statistics
#         self.stats = GameStats(self)

#         self.rocket = Rocket(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Rocket Game in a active state 
#         self.game_active = True

#     def run_game(self):
#         """Start the Main Loop for the Game."""
#         while True:
#             self._check_events()
            
#             if self.game_active:
#                 self.rocket.update()
#                 self._update_bullet()
#                 self._update_aliens()
            
#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to key presses."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

#     def _check_keydown_events(self, event):
#         """Respond to key pressed."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = True
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()

#     def _check_keyup_events(self, event):
#         """Respond to key released."""
#         if event.key == pygame.K_UP:
#             self.rocket.moving_up = False
#         elif event.key == pygame.K_DOWN:
#             self.rocket.moving_down = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         new_bullet = Bullet(self)
#         self.bullets.add(new_bullet)

#     def _update_bullet(self):
#         # Update bullet positions
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.left >= self.screen.get_rect().right:
#                 self.bullets.remove(bullet)
            
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
    
#     def _create_fleet(self):
#         """Create a grid of aliens in columns starting at the right end."""
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         screen_width = self.setting.screen_width
#         screen_height = self.setting.screen_height

#         left_margin = self.rocket.rect.right + 50

#         # Start from right side with padding of one alien width
#         start_x = screen_width - alien_width - 20

#         # Loop columns from right to left
#         current_x = start_x
#         while current_x > left_margin:
#             current_y = alien_height  
#             while current_y < (screen_height - alien_height):
#                 self._create_alien(current_x, current_y)
#                 current_y += 2 * alien_height  
#             current_x -= 2 * alien_width  
    
#     def _create_alien(self, x, y):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.y = y 
#         new_alien.rect.x = x 
#         new_alien.rect.y = y 
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions 
#         if pygame.sprite.spritecollideany(
#             self.rocket, self.aliens, pygame.sprite.collide_mask):
#             self._ship_hit()            
            
#         # Look for aliens hitting the left end of the screen. 
#         self._check_aliens_left()


#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break

    
#     def _check_aliens_left(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.left < 0:
#                 # Treat this the same as if the ship got hit 
#                 self._ship_hit()
#                 break
    
#     def _ship_hit(self):
#         """Respond to the ship being hit by a alien."""
#         if self.stats.ships_left > 0:
#             # Decreemtn ships left 
#             self.stats.ships_left -= 1

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.rocket.center_ship()

#             # pause 
#             sleep(1)
#         else:
#             self.game_active = False

#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.x -= self.setting.fleet_drop_speed
#         self.setting.fleet_direction *= -1

#     def _update_screen(self):
#         """Draw image at the screen and flip to the new screen."""
#         self.screen.fill(self.setting.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.blit_bullet()
#         self.rocket.blitme()
#         self.aliens.draw(self.screen)
        
#         pygame.display.flip()

# if __name__ == '__main__':
#     rocket = RocketGame()
#     rocket.run_game()

# -----------------------------------------------------------------------------

# CHAPTER 14  SCORING 

# Adding the Play Button 

# Drawing the Button to the Screen / Starting the game / Resetting the Game
# Deactivating the Play Button 
# Hiding the Mouse Cursor 

# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         self.stats = GameStats(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play Button. 
#         self.play_button = Button(self, "PLAY!")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

    
#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game statistics 
#             self.stats.reset_stats()
#             self.game_active = True
#             # Hide the mosue cursor 
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining Bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create the new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()


#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left.
#             self.stats.ships_left -= 1 

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# -----------------------------------------------------------------------------

# Exercises 

# 14. Press P to Play 

# 14.2 Target Practice 

# -----------------------------------------------------------------------------

# Leveling Up 

# Modifying the Speed Setting 



# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         self.stats = GameStats(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play Button. 
#         self.play_button = Button(self, "PLAY!")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

    
#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game setting 
#             self.settings.initialize_dynamic_settings()

#             # Reset the game statistics 
#             self.stats.reset_stats()
#             self.game_active = True
#             # Hide the mosue cursor 
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining Bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create the new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()


#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left.
#             self.stats.ships_left -= 1 

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# Exercises 

# 14.3 Challenging Target Practice 


# 14.4 Difficulty Levels 

# -----------------------------------------------------------------------------

# Scoring

# Making a Scoreboard 



# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         # Create a Scoreboard
#         self.stats = GameStats(self)
#         self.sb = Scoreboard(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play Button. 
#         self.play_button = Button(self, "PLAY!")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

    
#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game setting 
#             self.settings.initialize_dynamic_settings()

#             # Reset the game statistics 
#             self.stats.reset_stats()
#             self.game_active = True
#             # Hide the mosue cursor 
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining Bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create the new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()


#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left.
#             self.stats.ships_left -= 1 

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the score information
#         self.sb.show_score()

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()



# Updating the Score as Aliens Are Shot Down 

# Resetting the Score 

# Making Sure to Score all Hits 

# High Socre 

# Displaying the Level 

# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         # Create a Scoreboard
#         self.stats = GameStats(self)
#         self.sb = Scoreboard(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play Button. 
#         self.play_button = Button(self, "PLAY!")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

    
#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game setting 
#             self.settings.initialize_dynamic_settings()

#             # Reset the game statistics 
#             self.stats.reset_stats()
#             self.sb.prep_score()
#             self.sb.prep_level()
#             self.game_active = True
#             # Hide the mosue cursor 
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining Bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create the new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()


#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if collisions:
#             for aliens in collisions.values():
#                 self.stats.score += self.settings.alien_point * len(aliens)
#             self.sb.prep_score()
#             self.sb.check_high_score()
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()

#             self.stats.level += 1
#             self.sb.prep_level()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left.
#             self.stats.ships_left -= 1 

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the score information
#         self.sb.show_score()

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()


# Diplaying the number of ship 


# import sys 
# from time import sleep

# import pygame

# from settings import Setting
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from button import Button
# from ship import Ship
# from bullet import Bullet
# from alien import Alien


# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.settings = Setting()

#         self.screen = pygame.display.set_mode(
#             (self.settings.screen_width, self.settings.screen_height))
#         pygame.display.set_caption("Alien Invasion")

#         # Create an instance to store game statistics.
#         # Create a Scoreboard
#         self.stats = GameStats(self)
#         self.sb = Scoreboard(self)

#         self.ship = Ship(self)
#         self.bullets = pygame.sprite.Group()
#         self.aliens = pygame.sprite.Group()

#         self._create_fleet()

#         # Start Alien Invasion in an inactive state.
#         self.game_active = False

#         # Make the Play Button. 
#         self.play_button = Button(self, "PLAY!")

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             self._check_events()

#             if self.game_active:
#                 self.ship.update()
#                 self._update_bullets()
#                 self._update_aliens()

#             self._update_screen()
#             self.clock.tick(60)

#     def _check_events(self):
#         """Respond to keypresses and mouse events."""
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 self._check_play_button(mouse_pos)
#             elif event.type == pygame.KEYDOWN:
#                 self._check_keydown_events(event)
#             elif event.type == pygame.KEYUP:
#                 self._check_keyup_events(event)

    
#     def _check_play_button(self, mouse_pos):
#         """Start a new game when the player clicks Play."""
#         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
#         if button_clicked and not self.game_active:
#             # Reset the game setting 
#             self.settings.initialize_dynamic_settings()

#             # Reset the game statistics 
#             self.stats.reset_stats()
#             self.sb.prep_score()
#             self.sb.prep_level()
#             self.sb.prep_ships()
#             self.game_active = True
#             # Hide the mosue cursor 
#             pygame.mouse.set_visible(False)

#             # Get rid of any remaining Bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create the new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()


#     def _check_keydown_events(self, event):
#         """Respond to keypresses."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = True
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = True
#         elif event.key == pygame.K_q:
#             sys.exit()
#         elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if collisions:
#             for aliens in collisions.values():
#                 self.stats.score += self.settings.alien_point * len(aliens)
#             self.sb.prep_score()
#             self.sb.check_high_score()
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()

#             self.stats.level += 1
#             self.sb.prep_level()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left and update the score board.
#             self.stats.ships_left -= 1 
#             self.sb.prep_ships()

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the score information
#         self.sb.show_score()

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()




# Exercises 

# 14.5 All- time High Socre 


import sys 
from time import sleep
import json
from pathlib import Path

import pygame

from settings import Setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Setting()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics.
        # Create a Scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the Play Button. 
        self.play_button = Button(self, "PLAY!")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._close_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game setting 
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics 
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            # Hide the mosue cursor 
            pygame.mouse.set_visible(False)

            # Get rid of any remaining Bullets and aliens 
            self.bullets.empty()
            self.aliens.empty()

            # Create the new fleet and center the ship 
            self._create_fleet()
            self.ship.center_ship()


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._close_game()
        elif event.key == pygame.K_SPACE:
#             self._fire_bullet()            

#     def _check_keyup_events(self, event):
#         """Respond to key releases."""
#         if event.key == pygame.K_RIGHT:
#             self.ship.moving_right = False
#         elif event.key == pygame.K_LEFT:
#             self.ship.moving_left = False

#     def _fire_bullet(self):
#         """Create a new bullet and add it to the bullets group."""
#         if len(self.bullets) < self.settings.bullets_allowed:
#             new_bullet = Bullet(self)
#             self.bullets.add(new_bullet)

#     def _update_bullets(self):
#         """Update position of bullets and get rid of old bullets."""
#         # Update bullet positions.
#         self.bullets.update()

#         # Get rid of bullets that have disappeared.
#         for bullet in self.bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 self.bullets.remove(bullet)
        
#         self._check_bullet_alien_collisions()

#     def _check_bullet_alien_collisions(self):
#         """Respond to bullet-alien collisions."""
#         # Remove any bullets and aliens that have collided.
#         collisions = pygame.sprite.groupcollide(
#             self.bullets, self.aliens, True, True)
        
#         if collisions:
#             for aliens in collisions.values():
#                 self.stats.score += self.settings.alien_point * len(aliens)
#             self.sb.prep_score()
#             self.sb.check_high_score()
        
#         if not self.aliens:
#             # Destroy existing bullets and create new fleet.
#             self.bullets.empty()
#             self._create_fleet()
#             self.settings.increase_speed()

#             self.stats.level += 1
#             self.sb.prep_level()

#     def _create_fleet(self):
#         """Create the fleet of aliens."""
#         # Create an alien and keep adding aliens until there's no room left.
#         # Spacing between aliens is one alien width and one alien height.
#         alien = Alien(self)
#         alien_width, alien_height = alien.rect.size

#         current_x, current_y = alien_width, alien_height
#         while current_y < (self.settings.screen_height - 3 * alien_height):
#             while current_x < (self.settings.screen_width - 2 * alien_width):
#                 self._create_alien(current_x, current_y)
#                 current_x += 2 * alien_width

#             # Finished a row; reset x value, and increment y value.
#             current_x = alien_width
#             current_y += 2 * alien_height

#     def _create_alien(self, x_position, y_position):
#         """Create an alien and place it in the fleet."""
#         new_alien = Alien(self)
#         new_alien.x = x_position
#         new_alien.rect.x = x_position
#         new_alien.rect.y = y_position
#         self.aliens.add(new_alien)

#     def _update_aliens(self):
#         """Check if the fleet is at an edge, then update positions."""
#         self._check_fleet_edges()
#         self.aliens.update()

#         # Look for alien-ship collisions.
#         if pygame.sprite.spritecollideany(self.ship, self.aliens):
#             self._ship_hit()

#         # Look for aliens hitting the bottom of the screen . 
#         self._check_aliens_bottom()

#     def _check_fleet_edges(self):
#         """Respond appropriately if any alien have reached an edge."""
#         for alien in self.aliens.sprites():
#             if alien.check_edges():
#                 self._change_fleet_direction()
#                 break
    
#     def _change_fleet_direction(self):
#         """Drop the entire fleet and change the fleet's direction."""
#         for alien in self.aliens.sprites():
#             alien.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1

#     def _check_aliens_bottom(self):
#         """Check if any aliens have reached the bottom of the screen."""
#         for alien in self.aliens.sprites():
#             if alien.rect.bottom >= self.settings.screen_height:
#                 # Treat this the same as if the ship got hit.
#                 self._ship_hit()
#                 break

#     def _ship_hit(self):
#         """Respond to the ship being hit by an alien."""
#         if self.stats.ships_left > 0:
#             # Decrement ships_left and update the score board.
#             self.stats.ships_left -= 1 
#             self.sb.prep_ships()

#             # Get rid of any remaining bullets and aliens 
#             self.bullets.empty()
#             self.aliens.empty()

#             # Create a new fleet and center the ship 
#             self._create_fleet()
#             self.ship.center_ship()

#             # pause
#             sleep(0.5)
#         else:
#             self.game_active = False
#             pygame.mouse.set_visible(True)

#     def _update_screen(self):
#         """Update images on the screen, and flip to the new screen."""
#         self.screen.fill(self.settings.bg_color)
#         for bullet in self.bullets.sprites():
#             bullet.draw_bullet()
#         self.ship.blitme()
#         self.aliens.draw(self.screen)

#         # Draw the score information
#         self.sb.show_score()

#         # Draw the play button if the game is inactive
#         if not self.game_active:
#             self.play_button.draw_button()

#         pygame.display.flip()

    
#     def _close_game(self):
#         """Restore the high score and close the game."""
#         saved_high_score = self.stats.get_saved_high_score()
#         if self.stats.high_score > saved_high_score:
#             path = Path('high_score.json')
#             contents = json.dumps(self.stats.high_score)
#             path.write_text(contents)
        
#         sys.exit()


# if __name__ == '__main__':
#     # Make a game instance, and run the game.
#     ai = AlienInvasion()
#     ai.run_game()

# -----------------------------------------------------------------------------

# That's all about the game!