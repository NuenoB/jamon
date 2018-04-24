# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:28:05 2017

@author: enzoc
"""
import random
from combat_cores import combat_core
from dcc_graphics import null_graphics
from units import units
class ai:
    
    def __init__(self,base=1.0/4,margin_base=1.0/2):
        
        self.u_hp_w=base
        self.u_damage_w=base
        self.e_hp_w=base
        self.e_damage_w=base
        self.margin=margin_base
    def mutate(self,rate=5.0/100):
        self.u_hp_w=self.u_hp_w+(rate*random.randint(-1, 1))
        self.u_damage_w=self.u_damage_w+(rate*random.randint(-1, 1))
        self.e_hp_w=self.e_hp_w+(rate*random.randint(-1, 1))
        self.e_damage_w=self.e_damage_w+(rate*random.randint(-1, 1))
        self.margin=self.margin+(rate*random.randint(-1, 1))
    def rewriten(self,other_ai):
        other_ai.u_hp_w=self.u_hp_w
        other_ai.u_damage_w=self.u_damage_w
        other_ai.e_hp_w=self.e_hp_w
        other_ai.e_damage_w=self.e_damage_w
        other_ai.margin=self.margin
    def decide_attack(self,attacker, defender):
        a=attacker.hp*self.u_hp_w+attacker.ataque*self.u_damage_w
        b=defender.hp*self.e_hp_w+defender.ataque*self.e_damage_w
        return a+b<self.margin
    def to_dict(self):
        d=dict()
        d["u_hp_w"]     =self.u_hp_w
        d["u_damage_w"] =self.u_damage_w
        d["e_hp_w"]     =self.e_hp_w
        d["e_damage_w"] =self.e_damage_w
        d["margin"]     =self.margin
        return d
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
def recompenza(my_unit, enemy_unit):
    return my_unit.hp-enemy_unit.hp
        
#%%
if __name__ == '__main__':
    ais=list()
    for i in range(10):
        ais.append(ai())
        ais[i].mutate()
        print(ais[i].to_dict())
        
    graphics=null_graphics()
    cc=combat_core(graphics)
    print("Iniciando generaciones")
    for j in range(1000):
        max_recompenza=-10
        index=0
        for i in ais:
            first_unit=units(ataque=random.randint(0, 5),defence=0,hp=random.randint(0, 5))
            second_unit=units(ataque=random.randint(0, 5),defence=0,hp=random.randint(0, 5))        
            if i.decide_attack(first_unit,second_unit):
                cc.turn_combat_control(ataquer=first_unit,defender=second_unit)
            if max_recompenza<recompenza(first_unit,second_unit):
                index=i
                max_recompenza=recompenza(first_unit,second_unit)
        for i in ais:
            if not i==index:
                index.rewriten(i)
                i.mutate()
        if j%1== 0:
            print(i.to_dict())
            