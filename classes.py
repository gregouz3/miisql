import json
import requests
import mysql.connector
from config import *

class Data_food:

  def __init__(self):
    self.category_request = ""
    self.product_request = ""
    self.categories = list()
    self.product = list()
    self.read_config()
    self.update()

  def update(self):
    self.get_categories_data()
    self.get_products_data()
    self.insert_data()



  def read_config(self):
        connector = mysql.connector.connect(**config)
        cur = connector.cursor()
        f = open("config_datafood.json")
        data = json.load(f)
        self.category_request = data['category_list_request']
        self.product_request = data['products_request']

  def get_categories_data(self):
        r_cat = requests.get(self.category_request)
        data = r_cat.json()
        for dico in data['tags']:
          if len(dico['name']) < 100:
            category = { "name": dico['name'],"id": dico['id'] }
            self.categories.append(category)
          if len(self.categories) > 4:
            break

  def get_products_data(self):

        payload = self.product_request['parameters']
        for cat in self.product_request['categories']:
            payload['tag_0'] = cat['name']
        r_prods = requests.get(self.product_request['base_request'], params=payload)
        data = r_prods.json()
        for dicoo in data['products']:
          products = {
              "product_name": dicoo['product_name_fr'],
              "url": dicoo['url'],
              "ingredients": dicoo['ingredients_text_fr'],
              "stores": dicoo['stores'],
              "nutrition_grade": dicoo['nutrition_grades']
            }
          self.product.append(products)

  def insert_data(self):
          cnx = mysql.connector.connect(**config)
          cursor = cnx.cursor()
          i = 0
          for cat in self.categories:
            cate = cat['name'].replace("'","''")
            add_category = (f"INSERT INTO Food_category (category_name) VALUES ('{cate}')")
            print(add_category)
            cursor.execute(add_category)
            i += 1
            if i > 4:
              break

          for products in self.product:
            print("MMMMM")
            add_products = (f"INSERT INTO Food_product (product_name, categories, url, ingredients, stores, nutrition_grade) VALUES ('{products}')")
            print(add_products)
            cursor.execute(add_products)

          cnx.commit()
          cursor.close()

if __name__ == "__main__":
  Data_food()
