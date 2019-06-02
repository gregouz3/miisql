#!/usr/bin/python3

# -*- coding: Utf-8 -*

"""
File
"""

import json
import requests
import mysql.connector
from classes import *
from constants import *

def read_config_prod(category, category_id):

    url_cat = 'https://fr.openfoodfacts.org/categorie'
    nb_pages_url = 1
    url_json = 'json'
    url = "{}/{}/{}.{}".format(url_cat, category, nb_pages_url, url_json)
    request_url = requests.get(url)
    products = request_url.json()

    nb_pages = 3
    while nb_pages > 0:

        url = "{}/{}/{}.{}".format(url_cat, category, nb_pages_url, url_json)
        request_url = requests.get(url)
        products = request_url.json()
        products_name = ""
        nutriscore_level = ""
        store = ""
        product = Product()
        for prods in products["products"]:

            products_name = prods.get("product_name_fr", prods.get("product_name"))
            nutriscore_level = prods.get("nutrition_grades", None)
            url = prods["url"]
            store = prods.get("stores", None)
            product.add_database(products_name, nutriscore_level, url, store, category_id)

        nb_pages_url += 1
        nb_pages -= 1

def read_config_cat_prod():

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(FILL_CAT)
    cnx.commit()
    cursor.close()

if __name__ == '__main__':

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    read_config_cat_prod()
    read_config_prod("Volailles", 1)
    read_config_prod("Sandwichs", 2)
    read_config_prod("Compotes", 3)
    cnx.commit()
    cursor.close()
    cnx.close()
