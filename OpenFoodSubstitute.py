#!/usr/bin/python3

# -*- coding: Utf-8 -*
import mysql.connector
from classes import *
from constantes import *

def display_category():

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_cat)
  for id_cat, category_name in cursor:
    print(id_cat, ':', category_name)


def choose_category(category_choose):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()

  cursor.execute(select_cat_prod, category_choose)
  print(select_cat_prod)
  for id_prod, product_name, nutriscore in cursor:
    print(id_prod, ':', product_name, ' : ( nutriscore : ', nutriscore, ')')


def choose_product(id_prod):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_prod, id_prod)
  for id_prod, product_name, nutriscore, store, url in cursor:
    print('\n Vous avez choisi : ' ,product_name, ', son nutriscore est de ', nutriscore, ', vous pouvez trouver ce produit ici --> ', store, ',\n et voici son url pour plus dinfo :', url)



if __name__ == '__main__':

  loop = True
  while loop:
      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      proposals = int(input("1- Looking for a product to substitute? \n"
                            "2-  \n"
                            "3- Exit -OpenFoodSubstitute-\n"
                            "Select a proposal :  "))
      if proposals == 3:
        loop = False

      if proposals == 1:
        display_category()
        category_choose = (int(input("Select a category: ")),)
        choose_category(category_choose)
        id_prod = (int(input("Select a product: ")),)
        choose_product(id_prod)
        loop = False
      cnx.commit()
      cursor.close()
