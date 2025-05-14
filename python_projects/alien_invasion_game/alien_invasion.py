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


from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color 
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self.ship.update()
            self._update_bullets()            
            self._update_screen()
            self.clock.tick(50)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respont to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respont to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positons.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left 
        # Spacing between aliens is one alien width  
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x)
            current_x += 2 * alien_width

    def _create_alien(self, x_position):
        # Create a alien and place it in the row.
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()