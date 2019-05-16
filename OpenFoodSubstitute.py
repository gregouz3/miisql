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


def choose_category_1(category_choose):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_cat_prod_1)
  print(select_cat_prod_1)
  for id_prod, product_name, nutriscore in cursor:
    print(id_prod, '|', product_name, ':', nutriscore)


def choose_category_2(category_choose):

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  cursor.execute(select_cat_prod_2)
  for id_prod, product_name, nutriscore in cursor:
    print(id_prod, '|', product_name, ':', nutriscore)

if __name__ == '__main__':

  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  display_category()
  category_choose = (int(input("Selectionnez la catégorie: ")))
  print(category_choose)
  if category_choose == 1:
    choose_category_1(1)

  if category_choose == 2:

    choose_category_2(2)

  cnx.commit()
  cursor.close()
