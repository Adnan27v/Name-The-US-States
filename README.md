# US States Game 🗺️

A fun and educational Python game that helps users learn and memorize the 50 states of the United States through an interactive quiz format.

## 🎮 Features

- Interactive graphical interface with a blank US map
- Real-time state name input and validation
- Visual feedback showing correctly guessed states on the map
- 10-minute time limit for added challenge
- Score tracking showing progress (X/50 states)
- Case-insensitive input for user convenience
- Ability to exit the game at any time by typing "exit" or clicking cancel
- End-game summary showing missed states

## 📁 Project Structure

- **main.py**: The main game script containing the game logic and interface
- **50_states.csv**: Contains state names and their coordinates for map placement
- **blank_states_img.gif**: The blank US map used as the game background
- **requirements.txt**: Lists the required Python packages
- **Not_Guessed.csv**: Generated file containing states you missed (created after game ends)

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic knowledge of using the command line/terminal

### Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory in your terminal
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

1. Open your terminal in the project directory
2. Run the game using:
   ```bash
   python main.py
   ```
3. A window will open with a blank US map
4. Type state names when prompted
5. Try to name all 50 states within the 10-minute time limit!

## 🎯 How to Play

1. The game starts with a blank US map
2. A prompt will appear asking for state names
3. Type a state name and press Enter
4. If correct:
   - The state name will appear on the map at its correct location
   - Your score will increase
5. If incorrect:
   - The guess will be ignored
   - You can try again
6. You can exit the game at any time by:
   - Typing "exit" in the input prompt
   - Clicking the cancel button
7. The game ends when you either:
   - Name all 50 states correctly
   - The 10-minute timer runs out
   - Choose to exit the game
8. After the game ends:
   - Your final score will be displayed
   - A list of missed states will be shown
   - A CSV file (Not_Guessed.csv) will be generated with the missed states

## 📦 Dependencies

- `turtle`: For creating the graphical interface
- `pandas`: For handling the state data and generating the missed states CSV
- `time`: For implementing the game timer

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📊 Game Statistics

- Total states to guess: 50
- Time limit: 10 minutes
- Score format: X/50 states correct
- Exit options: Type "exit" or click cancel
- Learning aid: Automatic generation of missed states list