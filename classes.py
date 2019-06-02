#!/usr/bin/python3

# -*- coding: Utf-8 -*

import json
import requests
import mysql.connector
from constants import *

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
      cursor.execute(add_category)
      i += 1
      if i > 9:
        break
    cnx.commit()
    cursor.close()

class Product:

  def __init__(self):

    self.products_name = ""
    self.nutriscore_level = ""
    self.url = ""
    self.store = ""
    self.id_prod = 0
    self.category_id = 1



  def add_database(self, products_name, nutriscore_level, url, store, category_id):

      self.products_name = products_name
      self.nutriscore_level = nutriscore_level
      self.url = url
      self.store = store
      self.category_id = category_id

      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      data_products = (self.products_name, self.nutriscore_level,self.url, self.store, self.category_id)

      cursor.execute(add_product, data_products)

      cnx.commit()
      cursor.close()

  def product_selected(self, p_id):

      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      cursor.execute(select_prod, p_id)

      for id_prod, category_id, product_name, nutriscore, store, url in cursor:
          self.id_prod = id_prod
          self.category_id = category_id
          self.products_name = product_name
          self.nutriscore_level = nutriscore
          self.url = url
          self.store = store

  def display_product(self):

      print("\n Vous avez sélectionné : {} de la categorie n° {}, son nutriscore est de : {}.\n Ce produit est en vente à {} .\n Le lien OpenFoodFact : {} \n".format(self.products_name, self.category_id, self.nutriscore_level, self.store, self.url))
if __name__ == '__main__':
  Category()
  Product()
