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
  for id_prod, product_name, nutriscore in cursor:
    print(id_prod, ':', product_name, ' : ( nutriscore : ', nutriscore, ')')


def choose_product(id_prod):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_prod, id_prod)
  for id_prod, product_name, nutriscore, store, url in cursor:
    pass

def substitute_product():

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor(buffered = True)
  cursor.execute(select_prod_subs, category_choose)

  for product_name, nutriscore, store, url, category_id in cursor:
      print('\n Voici un substitut : ', product_name,', son nutriscore est de : ', nutriscore, ', vous pouvez acheter ce produit à ', store, ',\n Lien vers OpenFoodFact :', url)
      add_substitute = (product_name, nutriscore, store, url, category_id)
      cursor.execute(fill_substitute, add_substitute)
      print(fill_substitute, add_substitute)
      cnx.commit()
      break


def display_substitute():

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_subs)

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
        substitute_product()
        record_subs = (int(input("\nVoulez-vous enregistré ce substitut ?\n 1-Oui  2-Non ")))
        if record_subs == 1:
          pass
        if  record_subs == 2:
          cursor.execute(delet_subs)
          cnx.commit()

      if proposals == 2:
        cursor.execute(select_subs)
        for id_subs, substitute_name, nutriscore, store, url in cursor:
          print('\n',id_subs, ':', substitute_name, ',nutriscore : ',nutriscore, ', Magasin :', store,'\nLien vers OpenFoodFact: ',url)


  cnx.commit()
  cursor.close()
