import pygame
from settings import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, game, scene, groups, pos, image, health = 100):
      super().__init__(groups)
      
      self.game = game
      self.scene = scene      
      self.image = image          
      self.rect = self.image.get_frect(topleft = pos)
      self.health = health
      self.laser = []
      self.count_down_counter = 0
      self.speed = 60
      self.force = 2000
      self.acc = vec()
      self.vel = vec()
      self.fric = -15     
           
    def physics(self, dt):
        # direcction x
        self.acc.x += self.vel.x * self.fric
        self.vel.x += self.acc.x * dt
        self.rect.centerx += self.vel.x * dt + (self.vel.x/2) * dt
        
        # direcction y
        self.acc.y += self.vel.y * self.fric
        self.vel.y += self.acc.y * dt
        self.rect.centery += self.vel.y * dt + (self.vel.y/2) * dt
        
        if self.vel.magnitude() >= self.speed:
            self.vel = self.vel.normalize() * self.speed

    def update(self, dt):
        self.physics()
       
class Player(NPC):
     def __init__(self, game, scene, groups, pos, health = 100):
      super().__init__(game, scene, groups, pos, PLAYER)
      self.max_health = health
    
     def movement(self):
         if INPUTS['left']:
             if(self.rect.x - OFFSET > 0):
                 self.acc.x =-self.force
         elif INPUTS['right']:
             if(self.rect.x + self.rect.width < WIDTH - OFFSET):
                 self.acc.x = self.force
         else:
             self.acc.x = 0
        
         if INPUTS['up']:
             if(self.rect.y - OFFSET > 0):
                 self.acc.y =-self.force
         elif INPUTS['down']:
             if(self.rect.y + self.rect.height < HEIGHT- OFFSET):
                 self.acc.y = self.force
         else:
             self.acc.y = 0
             
     def update(self, dt):
         self.physics(dt)
         self.movement()

class Enemy(NPC):
    def __init__(self, game, scene, groups, pos, image, health = 100):
      super().__init__(game, scene, groups, pos, image)