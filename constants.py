import mysql.connector

config = {
  'user' : 'P5',
  'password':'password',
  'host': 'localhost',
  'database': 'database_food'
}

add_product = ("""INSERT INTO Food_product(product_name, nutriscore, url, store, category_id) VALUES (%s, %s, %s, %s, %s)""")

fill_cat = ("""INSERT INTO Food_category (category_name) VALUES ("Volailles"), ("Sandwichs"), ("Compotes") """)

select_cat = ("""SELECT * FROM Food_category""")

select_cat_prod = ("""SELECT id_prod, product_name, nutriscore FROM Food_product INNER JOIN Food_category ON Food_product.category_id = Food_category.id_cat WHERE Food_category.id_cat = %s""")

select_prod = ("""SELECT Food_product.id_prod, Food_product.category_id, Food_product.product_name, Food_product.nutriscore, Food_product.store, Food_product.url FROM Food_product WHERE  Food_product.id_prod = %s""")

fill_substitute = ("""INSERT INTO Food_substitute(category_id, product_id, substitute_name, nutriscore, store, url) VALUES (%s, %s, %s, %s, %s, %s)""")

select_sub_store = ("""SELECT category_id, id_prod, product_name, nutriscore, store, url FROM Food_product WHERE category_id = %s AND nutriscore = 'a' AND store <> '' """)

select_subs = ("""SELECT id_subs, category_id, product_id, substitute_name, nutriscore, store, url FROM Food_substitute """)

