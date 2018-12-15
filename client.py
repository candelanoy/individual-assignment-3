# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:21:38 2018

@author: owner
"""

#%%
import requests

def add_contact(name,phone):
    
    url = "http://127.0.0.1:5000/add_contact/" + name + "/" + phone
    
    response = requests.get(url)
    new_contact = response.json()
    
    
    return new_contact , " Added to phonebook."

add_contact("maria","11111")

#%%
import requests

def get_phone(name):
    
    url = "http://127.0.0.1:5000/get_phone/" + name
    
    response = requests.get(url)
    number = response.json()       
             
    return "The phone number of " + name + " is " + str(number)

get_phone("juan")

#%%
import requests

def update_phone(name, new_phone):
    
    url = "http://127.0.0.1:5000/update_phone/" + name + "/" + new_phone
    
    response = requests.get(url)
    new = response.json()
    
    return "New phone of " + name + ": "  +  new

update_phone("carmen",98765)

#%%
import requests

def delete_phone(name):
    
    url = "http://127.0.0.1:5000/delete_phone/" + name 
    
    response = requests.get(url)
    x = response.json()
    
    return x

delete_phone("francisco")

#%%
import requests

def home():
    
    url = "http://127.0.0.1:5000/home/" 
    
    response = requests.get(url)
    phonebook = response.json()
    
    return phonebook

home()

#%%