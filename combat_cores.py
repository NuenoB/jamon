# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:48:00 2017

@author: enzoc
"""

#%%
class combat_core:
    
    def __init__(self,graphics):
        self.graphics=graphics
        
    @staticmethod
    def damage(damage, defence):
        return max(damage-defence,0)
    
    def control_turn(graphics,ataquer, defencer):
        defencer.get_rack(combat_core.damage(ataquer.get_damage(),defencer.get_defence()))
        if defencer.can_conter():
            ataquer.get_rack(combat_core.damage(defencer.get_damage(),ataquer.get_defence()))
        