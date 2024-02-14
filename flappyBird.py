import pygame
import random
import os.path

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIPE_WIDTH = 70
PIPE_GAP = 150
GRAVITY = 0.25
FLAP_HEIGHT = -5

GREEN = (0, 255, 0)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.vel_y = 0
        self.image = pygame.image.load('bird.png').convert_alpha()
        self.width = 70
        self.height = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.angle = 0  
        self.mask = pygame.mask.from_surface(self.image)

    def flap(self):
        self.vel_y = FLAP_HEIGHT
        self.angle = 30 

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y
        if self.vel_y < 0:
            self.angle = 30  
        else:
            self.angle -= 3  
        self.angle = max(-30, min(self.angle, 90))

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_image, rotated_rect.topleft)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)
        self.passed = False

        self.color = random.choice([GREEN])
        self.image = pygame.image.load('pipe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, self.height))
        self.bottom_image = pygame.transform.scale(self.image, (PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP))

    def update(self):
        self.x -= 2
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.bottom_image, (self.x, self.height + PIPE_GAP))
        flipped_top_image = pygame.transform.flip(self.image, False, True)
        screen.blit(flipped_top_image, (self.x, 0))

def check_collision(bird, pipe):
    offset_x = int(pipe.x - bird.x)
    offset_y_top = int(0 - bird.y)
    offset_y_bottom = int(pipe.height + PIPE_GAP - bird.y)
    bird_mask = bird.mask
    top_pipe_mask = pygame.mask.from_surface(pipe.image)
    top_offset = (offset_x, offset_y_top)
    top_collision = bird_mask.overlap(top_pipe_mask, top_offset)

    bottom_pipe_mask = pygame.mask.from_surface(pipe.bottom_image)
    bottom_offset = (offset_x, offset_y_bottom)
    bottom_collision = bird_mask.overlap(bottom_pipe_mask, bottom_offset)

    return top_collision or bottom_collision

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()
    background = pygame.image.load('sky.png').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    highscore = 0
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            highscore_str = file.read()
            if highscore_str:
                highscore = int(highscore_str)

    running = True
    while running:
        bird = Bird()
        pipes = []
        score = 0

        game_over = False 
        while not game_over:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()

          
            bird.update()

            if pipes:
                if pipes[0].x < -PIPE_WIDTH:
                    pipes.pop(0)

            if not pipes or pipes[-1].x < SCREEN_WIDTH - 200:
                pipe = Pipe(SCREEN_WIDTH)
                pipes.append(pipe)

            for pipe in pipes:
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    score += 1

                if check_collision(bird, pipe):
                    game_over = True  
                    break

                pipe.update()

            highscore = max(highscore, score)
            if bird.y > SCREEN_HEIGHT:
                game_over = True
            
            if bird.y < 0:
                game_over = True

            screen.blit(background, (0, 0))  
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            font = pygame.font.Font(None, 36)
            text_score = font.render(f'Score: {score}', True, (0, 0, 0))
            text_highscore = font.render(f'Highscore: {highscore}', True, (0, 0, 0))
            screen.blit(text_score, (10, 10))
            
            highscore_rect = text_highscore.get_rect()
            highscore_rect.topright = (SCREEN_WIDTH - 10, 10)
            screen.blit(text_highscore, highscore_rect)

            pygame.display.flip()
            clock.tick(60)

        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

        
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
        play_again_text = font.render("Press R to Play Again or Q to Quit", True, (0, 0, 0))
        screen.blit(play_again_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_over = False  
                        break
                    elif event.key == pygame.K_q:
                        running = False
                        game_over = True 
            if not running or not game_over:  
                break

    pygame.quit()

if __name__ == "__main__":
    main()
