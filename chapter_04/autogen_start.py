import asyncio
import os

from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


async def main():

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )


    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message="You are a helpful AI assistant.",
    )


    team = RoundRobinGroupChat(
        participants=[assistant],
        max_turns=5,
    )

    await Console(
        team.run_stream(
            task="Write a snake game using pygame."
        )
    )

    # Cleanup
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())


"""
---------- TextMessage (assistant) ----------
Creating a simple Snake game using Pygame is a fun project. Below is an example of how to implement this game. Before you run the code, make sure you have Pygame installed. You can install it using pip:

```bash
pip install pygame
```

Then, you can use the following code to create a simple Snake game:

```python
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display dimensions
WIDTH = 600
HEIGHT = 400

# Create display
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game by OpenAI')

# Set clock and snake attributes
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    game_display.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, BLACK, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(BLUE)
            message("You Lost! Press C-Continue or Q-Quit", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(BLUE)
        pygame.draw.rect(game_display, GREEN, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Start the game
game_loop()
```

### Instructions to Run the Game:

1. Copy the above code into a Python file, for example, `snake_game.py`.
2. Run the file:
   ```bash
   python snake_game.py
   ```
3. Use the arrow keys to control the snake.
4. Eat the green food to grow the snake and increase your score.
5. Avoid hitting the walls or running into yourself.
6. Press 'C' to continue after losing or 'Q' to quit.

This is a simple implementation of the Snake game, and you can expand upon it by adding features such as levels, increasing difficulty, or saving high scores. Have fun coding!
---------- TextMessage (assistant) ----------
Creating a simple Snake game using Pygame is a fun project. Below is an example of how to implement this game. Before you run the code, make sure you have Pygame installed. You can install it using pip:

```bash
pip install pygame
```

Then, you can use the following code to create a simple Snake game:

```python
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display dimensions
WIDTH = 600
HEIGHT = 400

# Create display
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set clock and snake attributes
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    game_display.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(BLUE)
            message("You Lost! Press C-Continue or Q-Quit", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(BLUE)
        pygame.draw.rect(game_display, GREEN, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
```

### Instructions to Run the Game:

1. Copy the above code into a Python file, for example, `snake_game.py`.
2. Run the file:
   ```bash
   python snake_game.py
   ```
3. Use the arrow keys to control the snake.
4. Eat the green food to grow the snake and increase your score.
5. Avoid hitting the walls or running into yourself.
6. Press 'C' to continue after losing or 'Q' to quit.

This is a simple implementation of the Snake game, and you can expand upon it by adding features such as levels, increasing difficulty, or saving high scores. Have fun coding!
"""