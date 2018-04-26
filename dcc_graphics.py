# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:03:28 2017

@author: enzoc
"""
import pygame

class null_graphics():
    pass
    
class text_graphics():
    pass

class proto_graphics():
    def __init__(self,width_set=800,height_set=800):
        self.screen_width=width_set
        self.screen_height=height_set
        self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])
        
        pass
    def import_image(self, path_image):
        return pygame.image.load(path_image).convert()
    
    def draw_grid(self):
        thick=3
        offset=-2
        black = (0,0,0)
        square_width=self.background_image.get_width()/self.background_grid_width
        square_height=self.background_image.get_height()/self.background_grid_height
        
        for x in range(self.background_grid_height+1):
            pygame.draw.line(self.screen, black,(0,x*square_height+offset),(self.background_image.get_width(),x*square_height+offset),thick)
 
        for x in range(self.background_grid_width+1):
            pygame.draw.line(self.screen, black,(x*square_width+offset,0),(x*square_width+offset,self.background_image.get_height()),thick)

    def load_background(self, path_image,grid_width,grid_height,scale=2):
        self.background_grid_width=grid_width
        self.background_grid_height=grid_height
        self.background_image=self.import_image(path_image)
        height=self.background_image.get_height()
        width=self.background_image.get_width()
        self.background_image=pygame.transform.scale(self.background_image,(int(width*scale),int(height*scale)))
        
    def draw_background(self):
        self.screen.blit(self.background_image,[0,0])
    
    def draw(self):
        self.draw_background()
        self.draw_grid()
        pygame.display.flip()
