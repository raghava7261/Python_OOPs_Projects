Dice Game in Python
This is a simple console-based Dice Game implemented in Python using object-oriented programming principles.

How the Game Works
Two players roll dice against each other: you (human) and the computer.

Each player starts with 5 points.

In each round:

Both roll a die.

The player with the higher value wins the round.

The winner gains 1 point, and the loser loses 1 point.

The game continues until one player reaches 0 points. Then the other player wins the game.

Project Structure
DiceGame.py - Main Python source code
README.md - Project description

Requirements
Python 3.x

No external packages required (random module is built-in)

How to Run
Clone or download this project.

Open DiceGame.py in PyCharm or any Python IDE.

Run the script:

python DiceGame.py

Follow the on-screen prompts to roll the dice.

Features
Object-Oriented Design

Randomized dice rolls

Console-based interaction

Simple game logic with win/lose conditions

Classes Used
Class: Die
Description: Handles dice rolling and stores current value

Class: Player
Description: Represents a player with a die and score counter

Class: DieGame
Description: Controls game flow, handles rounds, and determines winner

Sample Output
Welcome to game!
--------enter a new round:-----------
please press a key to roll dice:
player value: 4
computer value: 2
You win round!
computer score: 4
Your score: 6

License
This project is open-source and free to use under the MIT License.

