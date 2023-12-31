

# Space Invaders Game Documentation

## Overview

Space Invaders is a classic arcade-style shooting game implemented in Python using the Pygame library. The game features a player-controlled spaceship, enemies that move downward on the screen, and the goal is to shoot down the enemies while avoiding collisions. The player has limited lives, and the game progresses through levels as enemies are defeated.

## Files

- `space_invaders.py`: The main script containing the game logic.
- `assets/`: Directory containing image assets used in the game.

## Dependencies

- Python 3.x
- Pygame library

## Installation

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install Pygame: `pip install pygame`

## How to Run

Execute the following command in the terminal:

```bash
python space_invaders.py
```

## Game Components

### Classes

1. **Laser:**
   - Represents a laser shot by the player or enemies.
   - Attributes:
     - `x`: X-coordinate of the laser.
     - `y`: Y-coordinate of the laser.
     - `img`: Image representing the laser.
     - `mask`: Collision mask for pixel-perfect collision detection.
   - Methods:
     - `draw(window)`: Draws the laser on the game window.
     - `move(vel)`: Moves the laser vertically.
     - `off_screen(height)`: Checks if the laser is off the screen.
     - `collision(obj)`: Checks if the laser collides with another game object.

2. **Ship:**
   - Represents a generic spaceship.
   - Attributes:
     - `x`: X-coordinate of the spaceship.
     - `y`: Y-coordinate of the spaceship.
     - `health`: Health points of the spaceship.
     - `ship_img`: Image representing the spaceship.
     - `laser_img`: Image representing the laser shot by the spaceship.
     - `lasers`: List of lasers shot by the spaceship.
     - `cool_down_counter`: Counter for shooting cooldown.
   - Methods:
     - `draw(window)`: Draws the spaceship and its lasers on the game window.
     - `move_lasers(vel, obj)`: Moves the lasers and checks for collisions.
     - `cooldown()`: Manages the shooting cooldown.
     - `shoot()`: Initiates shooting.
     - `get_width()`: Gets the width of the spaceship.
     - `get_height()`: Gets the height of the spaceship.

3. **Player(Ship):**
   - Represents the player-controlled spaceship.
   - Inherits from the Ship class.
   - Additional Methods:
     - `healthbar(window)`: Draws the player's health bar on the game window.

4. **Enemy(Ship):**
   - Represents an enemy spaceship.
   - Inherits from the Ship class.
   - Additional Methods:
     - `move(vel)`: Moves the enemy spaceship downward.
     - `shoot()`: Initiates shooting.

### Functions

1. **collide(obj1, obj2):**
   - Checks for collision between two game objects.
   - Parameters:
     - `obj1`: First game object.
     - `obj2`: Second game object.
   - Returns:
     - `True` if the objects collide, `False` otherwise.

2. **redraw_window():**
   - Redraws the game window with the current game state.

3. **main():**
   - Main game loop containing the core game logic.

4. **main_menu():**
   - Displays the main menu and starts the game on mouse button press.

5. **run_game():**
   - Main function encapsulating the game logic.
   - Called when the script is executed directly.

## Controls

- **W/A/S/D:** Move the player spaceship.
- **Space Bar:** Shoot lasers.

## Rules

- Defeat enemies to progress through levels.
- Avoid enemy lasers and collisions.
- Player loses lives on collisions and when enemies reach the bottom.
- The game ends when all lives are lost or the player quits.

## Future Improvements

- Add sound effects and background music.
- Implement a scoring system.
- Enhance graphics and add more enemy types.
- Add power-ups and additional player abilities.

