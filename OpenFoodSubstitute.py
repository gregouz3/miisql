#!/usr/bin/python3

# -*- coding: Utf-8 -*
import mysql.connector
import random
from classes import *
from constants import *


substitute_food = list()

def display_category():

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_cat)
  for id_cat, category_name in cursor:
    print(id_cat, ':', category_name)

def display_products(category_choose):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_cat_prod, category_choose)
  for id_prod, product_name, nutriscore in cursor:
      print(id_prod, ':', product_name, ', nutriscore : ', nutriscore)



def substitute(id_product):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor(buffered=True)
  cursor.execute(select_sub_store, category_choose)

  for  category_id, id_prod, product_name, nutriscore, store, url in cursor:
      print("\n Voici un substitut : {}, de la categorie n° {}. \n Son nutriscore est de : {}. Ce produit est en vente à {} .\n Le lien OpenFoodFact : {} \n".format(product_name, category_id, nutriscore, store, url))
      add_substitute = (category_id, id_prod, product_name, nutriscore, store, url)
      substitute_food.append(add_substitute)

      try:
        record_subs = (int(input("\nVoulez-vous enregistré ce substitut ?\n 1-Oui  2-Non ")))
      except ValueError:
        print("Vous n'avez pas sélectionné 1 ou 2")
        record_subs = (int(input("\n Voulez-vous enregistré ce substitut ?\n 1-Oui  2-Non ")))

      if record_subs == 1:
          cursor.execute(fill_substitute, add_substitute)
          cnx.commit()
      else:
        break


if __name__ == '__main__':

  loop = True
  while loop:
      cnx = mysql.connector.connect(**config)
      cursor = cnx.cursor()
      try:
          proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? \n2- Retrouver mes aliments substitués.\n3- Exit \n -OpenFoodSubstitute-\n"))
      except  ValueError:
          print("Vous n'avez pas sélectionné 1, 2 ou 3")
          proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? \n2- Retrouver mes aliments substitués.\n3- Exit \n -OpenFoodSubstitute-\n"))

      while proposals not in (1, 2, 3):
          print("\n Sélectionnez 1 ou 2 pour utiliser -OpenFoodSubstitute- , ou 3 pour quitter le programme ")
          try:
              proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? \n2- Retrouver mes aliments substitués.\n3- Exit \n -OpenFoodSubstitute-\n"))

          except  ValueError:
              print("Vous n'avez pas sélectionné 1, 2 ou 3")
              proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? \n2- Retrouver mes aliments substitués.\n3- Exit \n -OpenFoodSubstitute-\n"))


      if proposals == 3:
        loop = False

      if proposals == 1:
          display_category()
          try:
            category_choose = (int(input("Selectionnez la catégorie : ")),)
          except ValueError:
            print("Vous n'avez pas sélectionné un chiffre correspondant")
            category_choose = (int(input("Selectionnez la catégorie : ")),)
          display_products(category_choose)
          try:
            id_product = (int(input("Selectionnez un aliment: ")),)
          except ValueError:
            print("Vous n'avez pas sélectionné un nombre correspondant")
            id_product = (int(input("Selectionnez un aliment: ")),)

          p_select = Product()
          p_select.product_selected(id_product)
          p_select.display_product()
          substitute(id_product)

      if proposals == 2:
        cursor.execute(select_subs)
        for id_subs, category_id, product_id, substitute_name, nutriscore, store, url in cursor:
          print('\n', id_subs, ':', substitute_name, ', nutriscore : ', nutriscore, ', Magasin :', store,'\n id categorie : ', category_id, ', id produit :', product_id,  '\n Lien vers OpenFoodFact: ', url)

  cnx.commit()
  cursor.close()
