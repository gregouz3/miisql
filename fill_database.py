import json
import requests
import mysql.connector
from classes import *


def read_config_cat_prod(category):

    url_cat = 'https://fr.openfoodfacts.org/categorie'
    nb_page = 1
    url_json = 'json'
    url = "{}/{}/{}.{}".format(url_cat, category, nb_page, url_json)
    request_url = requests.get(url)
    products = request_url.json()

    nb_pages = 3
    while nb_pages > 0:

      url = "{}/{}/{}.{}".format(url_cat, category, nb_page, url_json)
      request_url = requests.get(url)
      products = request_url.json()
      print(url)
      products_name = ""
      nutriscore_level = ""
      categories_names = ""
      product = Product()
      for prods in products["products"]:

        products_name = prods["product_name_fr"]
        nutriscore_level = prods["nutrition_grades"]
        categories_names = prods["pnns_groups_2"]
        url = prods["url"]
        product.add_database(products_name, nutriscore_level, categories_names, url)
      nb_page += 1
      nb_pages -= 1


if __name__ == '__main__':

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()

  read_config_cat_prod("Sandwichs")
  read_config_cat_prod("Viandes")

  cnx.commit()
  cursor.close()
  cnx.close()



