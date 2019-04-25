#!/usr/bin/python3

# -*- coding: Utf-8 -*

import json
import requests
import mysql.connector
from constantes import *



class Category:

  def __init__(self):

    self.request_category = ""
    self.category = list()

    self.read_config_cat()
    self.get_category_data()
    self.insert_category_data()

  def read_config_cat(self):

    connector = mysql.connector.connect(**config)
    cur = connector.cursor()
    json_file = open("config_datafood.json")
    data_category = json.load(json_file)
    self.request_category = data_category['list_category']

  def get_category_data(self):

    get_category = requests.get(self.request_category)
    data = get_category.json()
    for dico_cat in data['tags']:
      if len(dico_cat['name']) < 100:
        categories = {"name": dico_cat['name'], "id": dico_cat['id'] }
        self.category.append(categories)

  def insert_category_data(self):

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    i = 0
    for cat in self.category:
      cat_replace = cat['name'].replace("'","''")
      add_category = (f"INSERT INTO Food_category (category_name) VALUES ('{cat_replace}')")
      print(add_category)
      cursor.execute(add_category)
      i += 1
      if i > 5:
        break

    cnx.commit()
    cursor.close()

class Product:

  def __init__(self):


    self.products_name = ""
    self.nutriscore_level = ""
    self.categories_names = ""
    self.url = ""


  def add_database(self, products_name, nutriscore_level, categories_names, url):

      self.products_name = products_name
      self.nutriscore_level = nutriscore_level
      self.categories_names = categories_names
      self.url = url
      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      data_products = (self.products_name, self.nutriscore_level, self.categories_names, self.url)
      add_product = ("""INSERT INTO Food_product(product_name, nutriscore, category, url) VALUES (%s, %s, %s, %s)""")
      print(add_product, data_products)
      cursor.execute(add_product, data_products)

      cnx.commit()
      cursor.close()

if __name__ == '__main__':
  Category()
  Product()

