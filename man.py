import sys, os
from settings import *
from state import SplashScreen

class Game:
    def __init__(self):
      pygame.init()
      self.clock = pygame.time.Clock()
      self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
      pygame.display.set_caption(TITLE)
      self.font = pygame.font.Font(FONT, TITLESIZE)
      self.running = True
      # state machine
      self.states = []
      self.splash_screen = SplashScreen(self)
      self.states.append(self.splash_screen)
           
    def custom_cursor(self):
        pygame.mouse.set_visible(False)
        curs_image = pygame.image.load('./assets/images/crosshair182.png').convert_alpha()
        curs_image = pygame.transform.scale(curs_image,(32,32))
        curs_rect = curs_image.get_frect(center=pygame.mouse.get_pos())
        curs_image.set_alpha(150)
        self.screen.blit(curs_image, curs_rect)        
          
    def render_text(self, text, color, font, pos, centrilised=True):
        surf = font.render(str(text), False, color)
        rect = None 
        if centrilised:
            rect = surf.get_rect(center = pos)
        else:
            rect = surf.get_rect(topleft = pos)
        self.screen.blit(surf, rect)
    
    def get_images(self, path):
        images = []
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            img = pygame.image.load(full_path).convert_alpha()
            images.append(img)
        return images
    
    def get_animatinos(self, path):
        animation = {}
        for file_name in os.listdir(path):
            animation.update({file_name:[]})
        return animation
    
    def reset_inputs(self):
        for key in INPUTS:
            INPUTS[key] = False
    
    def get_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    INPUTS['escape'] = True
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    INPUTS['space'] = True
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS['left'] = True
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS['right'] = True
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS['up'] = True
                elif event.key in (pygame.K_DOWN, pygame.K_x):
                    INPUTS['down'] = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    INPUTS['space'] = False
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    INPUTS['left'] = False
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    INPUTS['right'] = False
                elif event.key in (pygame.K_UP, pygame.K_w):
                    INPUTS['up'] = False
                elif event.key in (pygame.K_DOWN, pygame.K_x):
                    INPUTS['down'] = False
      
    def loop(self):
        while self.running:
            dt = self.clock.tick(FPS)/1000
            self.get_inputs()
            # state machine
            # update
            self.states[-1].update(dt)
            # draw
            self.states[-1].draw(self.screen)
           
            #
            # self.custom_cursor() 
            #
            pygame.display.flip()


if __name__ == "__main__":
    Game().loop()