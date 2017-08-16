# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:49:05 2017

@author: enzoc
"""

import unittest
from combat_cores import combat_core
from dcc_graphics import null_graphics
from units import units
 #%%
class TestCombatCore(unittest.TestCase):
    def test_subtraction(self):
        #revisa que este restando
        graphics=null_graphics()
        cc=combat_core(graphics)
        first_unit=units(ataque=1,defence=1,hp=1)
        second_unit=units(ataque=0,defence=0,hp=1)
        cc.turn_combat_control(ataquer=first_unit,defender=second_unit)
        self.assertEqual(second_unit.hp,0)
        
    def test_min_0(self):
        #se acegura que la vida no baje de 0 (importante?)
        graphics=null_graphics()
        cc=combat_core(graphics)
        first_unit=units(ataque=1,defence=1,hp=1)
        second_unit=units(ataque=0,defence=0,hp=1)
        cc.turn_combat_control(ataquer=first_unit,defender=second_unit)
        self.assertEqual(second_unit.hp,0)
        


    def test_not_defence_heal(self):
        #revisa que la defenza no cure a la unidad
        graphics=null_graphics()
        cc=combat_core(graphics)
        first_unit=units(ataque=1,defence=1,hp=1)
        second_unit=units(ataque=0,defence=0,hp=1)
        cc.turn_combat_control(ataquer=first_unit,defender=second_unit)
        self.assertEqual(first_unit.hp,1)
    def test_control(self):
        graphics=null_graphics()
        cc=combat_core(graphics)
        first_unit=units(ataque=1,defence=1,hp=1)
        second_unit=units(ataque=0,defence=0,hp=1)
        
        cc.turn_combat_control(ataquer=first_unit,defender=second_unit)
        self.assertTrue(second_unit.is_dead())
#    def test_heal(self):
#        self.assertEqual(combat_core.heal(2,2))
#%%
class TestUnits(unittest.TestCase):
    def test_init(self):
        first_unit=units()
        self.assertEqual(first_unit.def_defence(),0)
        self.assertEqual(first_unit.get_damage(),0)
        self.assertTrue(first_unit.can_conter())
        
    def test_init_not_default(self):
        first_unit=units(1,1,1)
        self.assertEqual(first_unit.def_defence(),1)
        self.assertEqual(first_unit.get_damage(),1)
        self.assertTrue(first_unit.can_conter())
    
    def test_unit_get_hurt(self):
        first_unit=units()
        self.assertEqual(first_unit.get_hurt(1),-1)

    def test_unit_get_hurt_not_default(self):
        first_unit=units(1,1,1)
        first_unit.get_hurt(1)
        self.assertEqual(first_unit.hp,1)
#%%
if __name__ == '__main__':
    unittest.main()