# Pygame Library Overview

## 1. Package/Library Selected
The selected package/library is Pygame.

## 2. What is Pygame?
Pygame is a pacage designed for writing video games. It provides functionality for handling graphics, sound, and user input, making it suitable for developing 2D games.

### Purpose
The purpose of Pygame is to simplify the process of game development in Python by providing a set of tools and functionalities for handling various aspects of game creation, such as graphics rendering, sound playback, event handling, and more. It is great for making 2D games and if you are new to game development its very easy to learn.

### How to Use Pygame
To use Pygame, you need to install it using pip:

pip install pygame


Once installed, you can import the Pygame modules into your Python scripts and use them to create games. Pygame provides functions and classes for managing game windows, drawing shapes and images, playing sounds, handling user input, and more.

### Example Code
```python
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()  [1]
```

## 3. Functionalities of pygame
Pygame offers various functionalities and is all you would need to make a 2D game in python, including:

- Creating and managing game windows
- Drawing shapes, images, and text on the screen
- Handling keyboard and mouse events
- Managing timing and frame rates
- Handling collisions and physics simulation
- Animations

## 4. When was it created?
Pygame was created in the year 2000 by Pete Shinners and is actively maintained by a community of active developers.

## 5. Why did I select Pygame?
I selected Pygame because it provides a straightforward and beginner-friendly way to create games in Python. I wanted to make a simple game for my sample program and searched if it was possible to make games on python and found pygame.

## 6. How did learning Pygame influence my understanding of Python?
Learning Pygame has profoundly impacted my understanding of Python, particularly in the realm of event-driven programming, and game development. Pygame has provided me with hands-on experience in implementing fundamental programming concepts in a practical and engaging manner.

-**Event-Driven Programming**: Pygame's event handling system has introduced me to the concept of event-driven programming, where actions are triggered by user input or system events. Understanding how to respond to events such as key presses, mouse clicks, and window events has been crucial in building interactive and responsive applications.

-**Game Development**: Pygame's game development framework has provided me with a structured approach to building games from scratch. From managing game loops and frame rates to implementing collision detection and physics simulation, Pygame has equipped me with essential tools and techniques for developing games of varying complexity.

-**Problem-Solving Skills**: Through the process of developing games and solving programming challenges, Pygame has honed my problem-solving skills. I've learned to break down complex problems into smaller, manageable tasks and apply algorithmic thinking to devise efficient solutions. Most importantly I know how to implement pixel collsion now. 


## 7. Overall Experience

My overall experience with Pygame has been positive. I would recommend Pygame to anyone interested in game development, especially beginners or those familiar with Python. 

#### Recommendations:
- **Learning game development:** Pygame provides a beginner-friendly environment for learning game development concepts and Python programming simultaneously. Its intuitive interface and extensive documentation make it accessible to users of all skill levels.

#### Future Usage:
I intend to continue using Pygame for personal projects and further exploration into game development. Its versatility and robust feature set make it suitable for a wide range of projects, from simple arcade games to more complex simulations and interactive experiences. I really want to test its limits when it comes to game development.

## Refrences:
   [1](https://www.pygame.org/docs/)
