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
    print('\n substitutuion en cours lol : ')


def substitute_product(id_prod):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_prod_subs, fill_substitute, id_prod)
  for substitute_name, nutriscore, store, url in cursor:
    print('\n Voici un substitut, un aliment plus sein pour votre santé ! : ', substitute_name, ',son nutriscore est de : ', nutriscore, ', vous pouvez acheter ce produit à ', store, ',\n Lien vers OpenFoodFact :', url)



if __name__ == '__main__':

  loop = True
  while loop:
      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? \n2- Retrouver mes aliments substitués.\n3- Exit \n -OpenFoodSubstitute-\n"))
      if proposals == 3:
        loop = False

      if proposals == 1:
        display_category()
        category_choose = (int(input("Selectionnez la catégorie : ")),)
        choose_category(category_choose)
        id_prod = (int(input("Selectionnez un aliment: ")),)
        choose_product(id_prod)
        loop = False
      cnx.commit()
      cursor.close()
