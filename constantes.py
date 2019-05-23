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

fill_cat = ("""INSERT INTO Food_category (category_name) VALUES ("Sandwichs"), ("Snacks"), ("Boissons sans alcool"), ("Viandes"), ("Snacks sucrés")""")

select_cat = ("""SELECT * FROM Food_category""")

select_cat_prod = ("SELECT id_prod, product_name, nutriscore FROM Food_product INNER JOIN Food_category ON Food_product.category_id = Food_category.id_cat WHERE Food_category.id_cat = %s")

select_prod = ("""SELECT id_prod, product_name, nutriscore, store, url FROM Food_product WHERE  Food_product.id_prod = %s""")

select_prod_subs = ("""SELECT product_name, nutriscore, store, url, category_id FROM Food_product WHERE  nutriscore < 'b' AND category_id = %s""")

fill_substitute = ("""INSERT INTO Food_substitute(substitute_name, nutriscore, store, url, category_id) VALUES (%s, %s, %s, %s, %s)""")

select_subs = ("""SELECT id_subs, substitute_name, nutriscore, store, url FROM Food_substitute """)

delet_subs = ("""DELETE FROM Food_substitute WHERE category_id = %s""")
