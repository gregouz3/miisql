#!/usr/bin/python3

# -*- coding: Utf-8 -*

'''
File contains 2 functions. One to fill the Food_product table, and one for the Food_category table
'''

import requests
import mysql.connector
from classes import Product
from constants import CONFIG, FILL_CAT

def read_config_prod(category, category_id):
    """Function that takes a category of Open Food Facts and its id in parameter
    and who loads the data for each page of the category"""

    url_cat = 'https://fr.openfoodfacts.org/categorie'
    nb_pages_url = 1
    url_json = 'json'
    # url syntaxe
    url = "{}/{}/{}.{}".format(url_cat, category, nb_pages_url, url_json)
    request_url = requests.get(url)
    products = request_url.json()
    # 20 products per page
    nb_pages = 3
    # Fill Food_product table
    while nb_pages > 0:
        # redefine url
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
    """Function that fills the Food_category table with the categories choice in constants.py"""

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(FILL_CAT)
    # Make sure to commit data to the database
    cnx.commit()

if __name__ == '__main__':

    CNX = mysql.connector.connect(**CONFIG)
    CUR = CNX.cursor()
    # Fill table Food_category
    read_config_cat_prod()
    # Fill table Food_product with datas
    read_config_prod("Volailles", 1)
    read_config_prod("Sandwichs", 2)
    read_config_prod("Compotes", 3)
    CNX.commit()
    # Close connexion
    CUR.close()
    CNX.close()
