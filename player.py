# -*- coding: utf-8 -*-

import pygame

spritesheet = "player.png"

class Character(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        self.sheet = pygame.image.load(spritesheet)
        #width = self.sheet.get_rect().width
        #height = self.sheet.get_rect().height
        #self.sheet = pygame.transform.scale(self.sheet, (int(width*0.5), int(height*0.5)))
        
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(205, 1, 180, 205))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        #position image in the screen surface
        self.rect.topleft = position
        
        #variable for looping the frame sequence
        self.frame = 0
        
        self.rectWidth = 180
        self.rectHeight = 205
          
        self.left_states = { 0: (20, 136, self.rectWidth,  self.rectHeight), 1: (150, 136, self.rectWidth,  self.rectHeight), 2: (280, 136, self.rectWidth,  self.rectHeight),3: (400, 136, self.rectWidth,  self.rectHeight) }

    def get_frame(self, frame_set):
        #looping the sprite sequences.
        self.frame += 1
        
        #if loop index is higher that the size of the frame return to the first frame 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        #print(frame_set[self.frame])
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.update('up')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.update('right')
