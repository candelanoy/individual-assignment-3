# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:48:03 2018

@author: owner
"""

from flask import Flask, jsonify

server = Flask("phonebook")
        
phonebook = [{"name":"juan", "phone": 111},
             {"name":"carmen", "phone": 222},
             {"name":"francisco", "phone": 333}]

@server.route("/home")
def home():   
    return jsonify(phonebook)

@server.route("/add_contact/<name>/<phone>")
def add_contact(name,phone):   
    new_contact = {"name":name, "phone":phone}
    phonebook.append(new_contact)
            
    return jsonify(new_contact + " has been added to the phonebook")

@server.route("/get_phone/<name>")
def get_phone(name):   
    for contact in phonebook:
        if contact["name"] == name:
            number = contact["phone"]
    return jsonify(number)

@server.route("/delete_contact/<name>")
def delete_contact(name):
    index = next(index for index, dictionary in enumerate(phonebook) if dictionary['name'] == name)
    del phonebook[index]
    return jsonify(name + " has been deleted.")

@server.route("/update_phone/<name>/<new_phone>")
def update_phone(name, new_phone):

    for contact in phonebook:
        if contact["name"] == name:
            contact["phone"] = new_phone

    return jsonify("The phone number of " + name + " is now: " + new_phone)
    
server.run()