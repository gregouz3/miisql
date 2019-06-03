#!/usr/bin/python3

# -*- coding: Utf-8 -*

"""
File containing the classes Category and Product
"""

import json
import requests
import mysql.connector
from constants import CONFIG, ADD_PRODUCT, SELECT_PROD


class Category():
    '''The class category. Recover OpenFoodFact categories'''

    def __init__(self):

        self.request_category = ""
        self.category = list()
        self.read_config_cat()
        self.get_category_data()
        self.insert_category_data()

    def read_config_cat(self):
        '''Read config json'''
        json_file = open("config_datafood.json")
        data_category = json.load(json_file)
        self.request_category = data_category['list_category']

    def get_category_data(self):
        '''get categories json and fill the list category'''
        get_category = requests.get(self.request_category)
        data = get_category.json()
        for dico_cat in data['tags']:
            if len(dico_cat['name']) < 100:
                categories = {"name": dico_cat['name'], "id": dico_cat['id']}
                self.category.append(categories)

    def insert_category_data(self):
        '''Insert category in the table Food_category'''
        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()
        nb_cat = 0
        for cat in self.category:
            cat_replace = cat['name'].replace("'", "''")
            add_category = (f"INSERT INTO Food_category (category_name) VALUES ('{cat_replace}')")
            cursor.execute(add_category)
            print(add_category)
            nb_cat += 1
            # For 10 categories
            if nb_cat > 9:
                break
        cnx.commit()
        cursor.close()


class Product():
    '''The class Product . For the filling a table Food_product
     and create the product object chosen by the user'''

    def __init__(self):
        '''The constructor is empty'''
        self.products_name = ""
        self.nutriscore_level = ""
        self.url = ""
        self.store = ""
        self.id_prod = 0
        self.category_id = 1

    def add_database(self, products_name, nutriscore_level, url, store, category_id):
        '''Function used to fill the table Food_product, used in  fill_database.py program'''
        self.products_name = products_name
        self.nutriscore_level = nutriscore_level
        self.url = url
        self.store = store
        self.category_id = category_id

        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()
        data_products = (self.products_name, self.nutriscore_level, self.url, self.store,
                         self.category_id)

        cursor.execute(ADD_PRODUCT, data_products)

        cnx.commit()
        cursor.close()

    def product_selected(self, id_product):
        '''Create a object with data to the id_product selected by the user'''
        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()
        cursor.execute(SELECT_PROD, id_product)

        for id_prod, category_id, product_name, nutriscore, store, url in cursor:
            self.id_prod = id_prod
            self.category_id = category_id
            self.products_name = product_name
            self.nutriscore_level = nutriscore
            self.url = url
            self.store = store

    def display_product(self):
        '''Display data belong to product'''
        print("\n Vous avez sélectionné : {} de la categorie n° {}"
              ", son nutriscore est de : {}.\n"
              " Ce produit est en vente à {} .\n"
              "Le lien OpenFoodFact : {}\n"
              .format(self.products_name, self.category_id, self.nutriscore_level, self.store,
                      self.url))

if __name__ == '__main__':
    Category()
