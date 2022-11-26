#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:01:03 2022

@author: atsankova
"""
import sqlite3 as sq

class Pokemon:
    def __init__(self,name):
        self.name = name
        requete = "SELECT * FROM pokemon WHERE name = '{}'; ".format(name)
        connexion = sq.connect('Pokemon.db')
        liste = connexion.execute(requete)
        for tup in liste:
            if tup[0] != 'NULL':
                self.nom = tup[1]
        self.pv = tup[2]
        self.attaque = tup[3]
        self.defense = tup[4]
        self.attaque_speciale = tup[5]
        self.defense_speciale = tup[6]
        self.vitesse = tup[7]
        self.description = tup[8]
        self.id_img = tup[9]
        connexion.close()
        
    def get_name(self):
        return self.name
    def get_nom(self):
        return self.nom
    def get_pv(self):
        return self.pv
    def get_attaque(self):
        return self.attaque
    def get_defense(self):
        return self.defense
    def get_attaque_speciale(self):
        return self.attaque_speciale
    def get_defense_speciale(self):
        return self.defense_speciale
    def get_vitesse(self):
        return self.vitesse
    def get_description(self):
        return self.description
    def get_id_img(self):
        return self.id_img
    
    def __str__(self):
        return str(self.name)
    
    def ascendant(self):
        ma_requete = "SELECT asc_name FROM EvolutionDe WHERE desc_name ='{}';".format(self.name)
        connexion = sq.connect('Pokemon.db')
        reponse_curseur = connexion.execute(ma_requete)
        for tup in reponse_curseur:
            if tup != 'NULL':
                pokemon = Pokemon(tup[0])
                return pokemon
            else:
                return None
        connexion.close()
        
    def descendants(self):
        liste=[]
        ma_requete = "SELECT desc_name FROM EvolutionDe WHERE asc_name ='{}';".format(self)
        connexion = sq.connect('Pokemon.db')
        curseur = connexion.execute(ma_requete)
        for desc in curseur:
            pokemon = Pokemon(desc[0])
            liste.append(pokemon)
        return liste
        connexion.close()
        
    def types(self):
        reponse = []
        ma_requete = "SELECT type_name FROM estDeType WHERE  pokemon_name='{}';".format(self.name) 
        connexion = sq.connect('Pokemon.db')
        reponse_curseur = connexion.execute(ma_requete)
        for tup in reponse_curseur:
            reponse.append(tup[0])
        return reponse
        connexion.close()
    
    def pokemon_by_nom(nom : str):
        ma_requete = "SELECT name FROM pokemon WHERE name =(SELECT name from pokemon where nom ='{}');".format(nom)
        connexion = sq.connect('Pokemon.db')
        curseur = connexion.execute(ma_requete)
        reponse = list(curseur)
        name = reponse[0][0]
        pokemon = Pokemon(name)
        return pokemon
        connexion.close()
        
        
    def table_name():
        ma_requete = "SELECT name FROM pokemon ORDER BY name ASC;"
        connexion = sq.connect('Pokemon.db')
        reponse_curseur = connexion.execute(ma_requete)
        reponse2 = [tup[0] for tup in reponse_curseur]
        return reponse2
        connexion.close()
        
        
    def table_nom():
        ma_requete = "SELECT nom FROM pokemon ORDER BY nom ASC;"
        connexion = sq.connect('Pokemon.db')
        reponse_curseur = connexion.execute(ma_requete)
        reponse2 = [tup[0] for tup in reponse_curseur]
        return reponse2
        connexion.close()
        
    def effectif():
        ma_requete = "SELECT COUNT(*) FROM pokemon;"
        connexion = sq.connect('Pokemon.db')
        reponse_curseur = connexion.execute(ma_requete)
        return list(reponse_curseur)[0][0]
        connexion.close()
        
        
        