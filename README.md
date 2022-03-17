# Snake
A Python implementation of the Snake game, playable in the console.

## Usage
The user can change the game settings before launching the game (e.g., choosing the size of the game-space and the number of apples that show up). This can be done by modifying the ```settings.properties``` file. The default settings are the following:
```
[DEFAULT]
DIM = 7
apple_count = 10
```
The ```DIM``` can be any number greater than 2, and it represents the number of cells on each side of the board.  
The snake is composed of a ```*``` sign representing its head, and a multitude of ```+``` signs representing its body. The ```.``` signs represent the apples. The snake can be controlled by inputing the command ```move [step-count]```, which moves the snake ```step-count``` spaces in the direction it is headed (one if the step-count is omitted), or the commands ```up```, ```down```, ```left``` and ```right``` to change its direction. The snake cannot do a 180-degree turn.  
When the snake gets on top of an apple, the apple is consumed and replaced on the board (if there is enough available space), and the snake grows in size one space.  
The game is over when the snake exits the game board or collides with itself.

## Features
1. Console User Interface
2. Layered Architecture
3. Documentations for most functions