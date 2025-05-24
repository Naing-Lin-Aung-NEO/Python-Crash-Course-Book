# Responding to Alien-Ship Collisions 

# class GameStats:
#     """Track statistics for alien Invasion."""

#     def __init__(self, ai_game):
#         """Initialize statistics."""
#         self.settings = ai_game.settings
#         self.reset_stats()
    
#     def reset_stats(self):
#         """Initialize statistics that can change during the game."""
#         self.ships_left = self.settings.ship_limit



# Scoring 

# Displaying the Level 

# class GameStats:
#     """Track statistics for alien Invasion."""

#     def __init__(self, ai_game):
#         """Initialize statistics."""
#         self.settings = ai_game.settings
#         self.reset_stats()
#         # Hight score should never be reset 
#         self.high_score = 0
    
#     def reset_stats(self):
#         """Initialize statistics that can change during the game."""
#         self.ships_left = self.settings.ship_limit
#         self.score = 0 
#         self.level = 1 
        


# All-time High score 

import pygame
import json
from pathlib import Path 
class GameStats:
    """Track statistics for alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Hight score should never be reset 
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """Get saved the high score."""
        path = Path('high_score.json')
        try:
            content = path.read_text()
            high_score = json.loads(content)
            return high_score
        except FileNotFoundError:
            return 0
        
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0 
        self.level = 1 