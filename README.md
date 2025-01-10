Bee Game - Pygame
This is a simple game built using the Pygame library where a player (represented by a bee character) collects honey from a fractal-like honeycomb grid. The game includes movement, zoom controls, and changing the fractal's color using keyboard keys.
Features
Movement: Control the bee character with arrow keys.
Fractal Honeycomb: The game includes a dynamic Sierpinski hexagon fractal, which grows and changes shape as you interact with it.
Zoom: Zoom in and out of the fractal using a slider.
Collectibles: Collect honey (represented as honey images) scattered within the hexagonal grid.
Scoring: Collect honey to increase your score.
Color Change: Press number keys to change the color scheme of the fractal.
Background Image: A customizable background image is used in the game.
Requirements
To run the game, you'll need to have Python 3.x installed on your machine along with the Pygame library.

To install Pygame, you can use the following command:

bash
Copy code
pip install pygame
Additionally, the game uses images that should be placed in an Assets folder:

bal.jpg for the background image
BEE_char.png for the character (bee)
HONEY.png for the collectible items (honey)
Game Instructions
Move the Player: Use the arrow keys (Up, Down, Left, Right) to move the bee.
Zoom: Use the slider at the bottom-right of the screen to zoom in and out of the fractal.
Change Colors: Press the following keys to change the color scheme of the fractal:
0 - Default colors (orange to yellow)
1 - Blue to light blue
2 - Red to pink
3 - Dark green to green
Collect Honey: Move the bee over the honey icons to collect them. The game ends once all honey has been collected.
How to Run the Game
To run the game, execute the following command:

bashLicense
This project is licensed under the MIT License - see the LICENSE file for details.
Copy code
python game.py
This will start the game window, where you can interact with the game.
Customization
Assets: Replace the images in the Assets folder with your custom images for the background, character, and collectibles.
Fractal Settings: Modify the max_depth, base_radius, and other parameters to adjust the appearance of the Sierpinski hexagon fractal.
Zoom and Slider: Adjust the MAX_ZOOM and MIN_ZOOM to control how much zooming in and out is allowed.
Troubleshooting
If you encounter issues with pygame or the game not displaying correctly, ensure you have the correct version of Pygame installed and that the images in the Assets folder are in the correct format.

Credits
This game is built using the Pygame library.
Custom assets and images are required to make the game visually appealing.
