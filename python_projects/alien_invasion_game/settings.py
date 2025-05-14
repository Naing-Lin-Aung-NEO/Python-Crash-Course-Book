# Creating a Setting Class 

# class Setting:
#     """A class to store all settings for Alien Invasion."""

#     def __init__(self):
#         """Initilize the game's setting."""
#         # Screen Settings 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

# -----------------------------------------------------------------------------

# Exercises 

# 12.1 Blue Sky / 12.2 Game Character

# class Setting2:
#     """A class to store all settings for Alien Invasion."""
        
#     def __init__(self):
#         """Initilize the game's setting."""
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (130, 200 , 229)

# -----------------------------------------------------------------------------

# Adjusting The ship's Speed 


# class Setting:
#     """A class to store all settings for Alien Invasion."""

#     def __init__(self):
#         """Initilize the game's setting."""
#         # Screen Settings 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Settings
#         self.ship_speed = 1.5

# -----------------------------------------------------------------------------

# Shooting Bulltet / Adding Bullet Settings  


# class Setting:
#     """A class to store all settings for Alien Invasion."""

#     def __init__(self):
#         """Initilize the game's setting."""
#         # Screen Settings 
#         self.screen_width = 1200
#         self.screen_height = 700
#         self.bg_color = (230, 230, 230)

#         # Ship Settings
#         self.ship_speed = 1.5

#         # Bullet Settings 
#         self.bullet_speed = 2.0
#         self.bullet_width = 3
#         self.bullet_height = 15
#         self.bullet_color = (60, 60, 60)

# -----------------------------------------------------------------------------

# Limiting the Number of Bullets 
class Setting:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initilize the game's setting."""
        # Screen Settings 
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5

        # Bullet Settings 
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3