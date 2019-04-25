#!/usr/bin/python3

# -*- coding: Utf-8 -*

import mysql.connector

config = {
  'user' : 'P5',
  'password':'password',
  'host': 'localhost',
  'database': 'database_food',
  'raise_on_warnings': True
}

add_category = (f"INSERT INTO Food_category (category_name) VALUES ('{cat_replace}')")

add_product = ("""INSERT INTO Food_product(product_name, nutriscore, category, url) VALUES (%s, %s, %s, %s)""")

