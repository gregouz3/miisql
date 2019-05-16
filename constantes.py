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

add_product = ("""INSERT INTO Food_product(product_name, nutriscore, url, store, category_id) VALUES (%s, %s, %s, %s, %s)""")

fill_cat = ("""INSERT INTO Food_category (category_name) VALUES ("Viandes"), ("Boissons")""")

select_cat = ("""SELECT * FROM Food_category""")
select_cat_prod_1 = ("""SELECT Food_product.id_prod, Food_product.product_name, Food_product.nutriscore FROM Food_product WHERE id_prod < 101""")
select_cat_prod_2 = ("""SELECT Food_product.id_prod, Food_product.product_name, Food_product.nutriscore FROM Food_product WHERE id_prod > 100""")
