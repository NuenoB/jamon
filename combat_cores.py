# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:48:00 2017

@author: enzoc
"""

#%%
class combat_core:
    
    def __init__(self,graphics):
        self.graphics=graphics
        
#    @staticmethod
#    def damage(damage, defence):
#        return max(damage-defence,0)
    
    def turn_combat_control(self,ataquer, defender):
        defender.get_hurt(ataquer.get_damage())
#        if defender.can_conter(): lo commente porque no tiene tests
#            ataquer.get_hurt(defender.get_damage())
#        