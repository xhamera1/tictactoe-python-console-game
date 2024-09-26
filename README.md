# Tic Tac Toe Game
# CS50python final project

### My Details
- **Name**: Patryk Chamera
- **GitHub Username**: [xhamera1](https://github.com/xhamera1)
- **edX Username**: xhamera
- **City and Country**: Kraków or Stalowa Wola, Poland
- **Date of Video Recording**: 2024-09-26

### Video Demo
[Click here to view the video demo](https://youtu.be/a_qK1v_ciOU?si=mtOo-zX7brVXtkLT)

#### Description:
Welcome to the Tic Tac Toe project, a classic console-based game implemented in Python for two players. This project showcases fundamental programming concepts, including game logic, user input handling, and error management. The game allows two players to compete against each other by marking spots on a 3x3 grid, with the objective of placing three of their marks in a horizontal, vertical, or diagonal row before their opponent does.

## Features
1. **Two-Player Mode**: The game supports two players who can take turns marking their respective spots.
2. **Input Validation**: The program ensures that player inputs are valid, prompting users to re-enter their choices if they select an invalid spot or one that has already been occupied.
3. **Win and Draw Detection**: The game includes logic to check for wins and draws, announcing the result at the end of the game.
4. **User-Friendly Interface**: The game features a simple console interface that displays the current game board after each move, allowing players to visualize the game state.
5. **Dynamic Player Switching**: The game automatically switches between players after each valid move, ensuring a smooth gameplay experience.

## Project Files
- **project.py**: This is the main file that contains the core logic of the Tic Tac Toe game. It defines all the necessary functions to handle the game flow, including:
  - `main()`: The entry point of the game that initializes the game board, handles player inputs, and manages the game loop.
  - `print_game(game)`: A utility function that displays the current state of the game board.
  - `convert_slot(slot)`: Converts a user-friendly slot number (1-9) into corresponding 2D coordinates for easier manipulation of the game board.
  - `mark(player, slot, game)`: Marks a chosen spot with the current player’s symbol ('X' or 'O'), while also validating the move.
  - `check_win(game)`: Checks the current game state to determine if there is a winner.
  - `change_player(player)`: A simple function that switches the active player from 'X' to 'O' and vice versa.

- **test_project.py**: This file contains unit tests that ensure the functionality of the core components of the Tic Tac Toe game. It utilizes the `pytest` framework to validate the following functions:
  - `test_check_win()`: Tests various scenarios to confirm that the win detection logic works correctly.
  - `test_convert_slot()`: Verifies that the slot conversion from a user-friendly format to board coordinates is functioning properly.
  - `test_change_player()`: Confirms that the player-switching mechanism behaves as expected.
  - `test_mark()`: Ensures that marking a spot works correctly, including validation for invalid moves.

## Design Choices
While developing this project, several design choices were made to enhance functionality and user experience:

1. **Error Handling**: Custom exceptions and error messages improve user experience by providing clear feedback when invalid inputs are entered. This approach prevents the game from crashing and guides users to correct their mistakes.

2. **Game Logic**: The game logic is structured to separate concerns, with distinct functions for marking spots, checking for wins, and printing the game board. This modular design makes the code easier to read, maintain, and test.

3. **User Interaction**: The decision to implement a console-based interface was made to keep the project simple and focused on functionality. This allows players to quickly engage with the game without navigating complex GUI elements.

4. **Dynamic Gameplay**: The alternating turns between players create an engaging experience that mimics the traditional play style of Tic Tac Toe. Each turn updates the board and checks for a win or draw condition, keeping players invested in the game.

## Conclusion
This Tic Tac Toe project serves as a fundamental exercise in game development, highlighting the importance of clear logic, user interaction, and error management. Through continuous improvement and iteration, this project can evolve into a more comprehensive gaming experience. We invite players to enjoy the classic game of Tic Tac Toe and explore the code behind it to learn more about programming in Python.
