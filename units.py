# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:51:49 2017

@author: enzoc
"""

class units:
    """
    clase que contiene las estadisticas  funciones de una unidad
    """

    def __init__(self,ataque=0,defence=0,hp=0):
        self.ataque=ataque
        self.defence=defence
        self.hp=hp
    def can_conter(self):
        return True
    def get_damage(self):
        return self.ataque
    def def_defence(self):
        return self.defence
    def get_hurt(self,damage_deal):
        self.hp=self.hp-max((damage_deal-self.defence),0)#not a bug that can heal a unit
        return self.hp
    def is_dead(self):
        return self.hp<=0#ha gracias test develomet cosa