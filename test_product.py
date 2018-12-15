# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:48:27 2018

@author: owner
"""

from product_class import recalculate_quality, Product

def test_recalculate_potato():
    potato = Product("potato",5)
    recalculate_quality(potato)
    assert potato.quality == 4.5
    
def test_recalculate_cheese():
    cheese = Product("cheese",5)
    recalculate_quality(cheese)
    assert cheese.quality == 3

def test_recalculate_olives():
    olives = Product("olives",9)
    recalculate_quality(olives)
    assert olives.quality == 9

def test_recalculate_ham():
    ham = Product("ham",10)
    recalculate_quality(ham)
    assert ham.quality == 10

def test_recalculate_bread():
    bread = Product("bread",3)
    recalculate_quality(bread)
    assert bread.quality == 0
    
def test_recalculate_milk():
    milk = Product("milk",2)
    recalculate_quality(milk)
    assert milk.quality == -1
    
def test_recalculate_maria():
    maria = Product("maria",1)
    recalculate_quality(maria)
    assert maria.quality == -2