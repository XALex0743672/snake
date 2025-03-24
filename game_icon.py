import pygame
import os

def create_icon():
    """Create a simple icon for the game"""
    # Initialize pygame
    pygame.init()
    
    # Create a small surface for the icon
    icon_size = 32
    icon = pygame.Surface((icon_size, icon_size))
    
    # Fill with black background
    icon.fill((0, 0, 0))
    
    # Draw a green snake shape
    pygame.draw.rect(icon, (0, 255, 0), (8, 8, 16, 16))
    pygame.draw.rect(icon, (0, 255, 0), (8, 16, 8, 8))
    
    # Draw red eyes
    pygame.draw.rect(icon, (255, 0, 0), (12, 12, 2, 2))
    pygame.draw.rect(icon, (255, 0, 0), (18, 12, 2, 2))
    
    # Save the icon
    pygame.image.save(icon, "snake_icon.png")
    print("Icon created: snake_icon.png")

if __name__ == "__main__":
    create_icon()