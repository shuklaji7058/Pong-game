#Pong Game with Python Turtle Graphics

This repository contains the source code for a classic Pong game implemented using Python's Turtle graphics module. The game includes a ball, paddles, and a scoreboard to keep track of points. The project is divided into several modules for better organization and maintainability.

#Files in this Repository 

ball.py
This module defines the Ball class, which handles the creation, movement, and collision detection of the ball in the game. It includes methods for initializing the ball, updating its position, and resetting it after scoring.

main.py
The main script to run the game. This file sets up the game window, initializes the game objects (ball, paddles, scoreboard), and contains the main game loop. It also handles user inputs to control the paddles.

paddle.py
This module defines the Paddle class, which represents the paddles controlled by the players. It includes methods for moving the paddles up and down and for detecting collisions with the ball.

scoreboard.py
This module defines the Scoreboard class, which is responsible for keeping and displaying the score. It updates the score when a player scores a point and resets it when the game restarts.

#Game Controls
Player 1 (left paddle): Use the W key to move up and the S key to move down.
Player 2 (right paddle): Use the Up Arrow key to move up and the Down Arrow key to move down.

#Features
Realistic ball movement with collision detection.
Simple and intuitive controls.
Scorekeeping to track the points for both players.
