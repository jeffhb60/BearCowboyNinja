
# Bear, Cowboy, Ninja Game

## Description
Bear, Cowboy, Ninja is an engaging and entertaining game crafted in Python using the Tkinter library. Players compete against the computer by selecting one of three characters: Bear, Cowboy, or Ninja. The game adjudicates the winner based on predefined rules and keeps a record of game statistics.

## Features
- Players can select from Bear, Cowboy, and Ninja.
- The computer randomly chooses an opposing character.
- The game decides the winner according to predefined outcomes.
- Displays the result of each round.
- Tracks user wins, CPU wins, and draws.
- Shows statistics, including win percentages.

## Requirements
- Python 3.x
- Tkinter library (usually included with Python)
- Pillow library for image processing

## Installation
1. **Clone the repository**:
   git clone https://github.com/jeffhb60/BearCowboyNinja.git
   cd BearCowboyNinja

2. **Install the required Python packages**:
   pip install pillow

3. **Ensure you have the following images in the \`images\` folder**:
   - \`background.png\` (Background wallpaper)
   - \`bear.png\` (Image of a bear)
   - \`cowboy.png\` (Image of a cowboy)
   - \`ninja.png\` (Image of a ninja)

## Usage
1. **Run the game**:
   python main.py

2. **Play the game**:
   - Select one of the characters by clicking on the corresponding button.
   - The game will display the result of the battle and update the statistics.
   - Continue playing as many rounds as you like.

## Game Rules
- **Bear vs Cowboy**: Bear wins.
- **Bear vs Ninja**: Ninja wins.
- **Cowboy vs Bear**: Cowboy wins.
- **Cowboy vs Ninja**: Ninja wins.
- **Ninja vs Bear**: Ninja wins.
- **Ninja vs Cowboy**: Ninja wins.
- If both characters are the same, it is a tie.

## Code Structure
- main.py: The main game launch file
- bear_cowboy_ninja.py\`: The BearCowboyNinja Class File, and game 
- images/: Folder containing the images used in the game.

## Complexity Analysis
### Time Complexity
- Each method in the game runs in constant time, so the overall time complexity is O(1).

### Space Complexity
- The program uses a constant amount of space for variables, images, and UI elements, resulting in a space complexity of O(1).

## Acknowledgements
- This game was inspired by the classic "Rock, Paper, Scissors" game.
