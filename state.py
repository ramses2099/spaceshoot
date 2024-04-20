import pygame, sys
from settings import *
from objects import Player

class State():
    def __init__(self, game):
      self.game = game
      self.prev_state = None
    
    def enter_state(self):
        if len(self.game.states) > 1:
            self.prev_state = self.game.states[-1]
        self.game.states.append(self)
    
    def exit_state(self):
        self.game.states.pop()      
      
    def update(self, dt):
        pass
    
    def draw(self, screen):
        pass


class SplashScreen(State):
    def __init__(self, game):
      State.__init__(self, game)
      
    def update(self, dt):
        if INPUTS['space']:
            Scene(self.game).enter_state()
            self.game.reset_inputs()
        
    def draw(self, screen):
        screen.blit(BG,(0, 0))
        self.game.render_text("Splash Screen, press space", COLORS['white'],
                              self.game.font, (WIDTH/2, HEIGHT/2))
    

class Scene(State):
    def __init__(self, game):
      State.__init__(self, game)
      self.level = 1
      self.lives = 5
      self.update_sprites = pygame.sprite.Group()
      self.drawn_sprites = pygame.sprite.Group() 
      
      self.player = Player(self.game, self, [self.update_sprites, self.drawn_sprites],(WIDTH/2, HEIGHT- 64))     
                 
    def debugger(self, debug_list):
        for idx, name in enumerate(debug_list):
            self.game.render_text(name, COLORS['white'], self.game.font, (10, 15 * idx), False)
      
    def show_info_game(self, list_info):
        for idx, name in enumerate(list_info):
            self.game.render_text(name, COLORS['white'], self.game.font, (WIDTH-100, 15 * idx), False)
        
    def update(self, dt):
        self.update_sprites.update(dt)
        
    def draw(self, screen):
        screen.blit(BG,(0, 0))
        self.drawn_sprites.draw(screen)
        self.debugger([
            str(f'FPS: {round(self.game.clock.get_fps(), 2)}')            
        ])
        self.show_info_game([
            str(f'Level: {self.level}'),
            str(f'Lives: {self.lives}'),            
        ])
    