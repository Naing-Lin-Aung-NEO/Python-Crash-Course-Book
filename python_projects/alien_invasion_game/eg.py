class Setting:
    """Make setting for the game rocket."""
    
    def __init__(self):
        """Initialize game settings."""
        # Screen Setting 
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (5, 10, 30)

        # Ship Setting 
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings 
        self.bullet_speed = 2.0

        # Alien settings 
        self.alien_speed = 1.5
        self.alien_frequency = 0.008
        self.fleet_drop_speed = 10
        # fleet direction of 1 represent bottom; -1 represent top 
        self.fleet_direction = 1

        # How quickly the game speeds up 
        self.speed_scale = 1.3

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game.
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.5

        # Fleet direction of 1 represent botton, -1 represent top 

    def change_speed(self, speed_sacle):
        """Change the speed for medium, difficult mode."""
        self.alien_speed *= int(speed_sacle)
        self.ship_speed *= int(speed_sacle)
        self.bullet_speed *= int(speed_sacle)

    def increase_speed(self):
        """Increase speed setting."""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale

class GameStats:
    """Track statistics for rocke game."""

    def __init__(self, rc_game):
        """Initialize statistics."""
        self.setting = rc_game.setting
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.setting.ship_limit





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
