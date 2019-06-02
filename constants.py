#!/usr/bin/python3

# -*- coding: Utf-8 -*

"""
File containing constants and queries
"""

# Connection configuration to the database
CONFIG = {
    'user' : 'P5', 'password' : 'password', 'host' : 'localhost', 'database' : 'database_food'
}

ADD_PRODUCT = ("""INSERT INTO Food_product
               (product_name, nutriscore, url, store, category_id)
                VALUES (%s, %s, %s, %s, %s)""")

FILL_CAT = ("""INSERT INTO Food_category
            (category_name) VALUES ("Volailles"), ("Sandwichs"), ("Compotes")""")

SELECT_CAT = ("""SELECT * FROM Food_category""")

# Query which return a list of the product according to the category chosen
SELECT_CAT_PROD = ("""SELECT id_prod, product_name, nutriscore FROM Food_product
                   INNER JOIN Food_category
                   ON Food_product.category_id = Food_category.id_cat
                   WHERE Food_category.id_cat = %s""")

SELECT_PROD = ("""SELECT Food_product.id_prod, Food_product.category_id, Food_product.product_name,
               Food_product.nutriscore, Food_product.store, Food_product.url FROM Food_product
               WHERE  Food_product.id_prod = %s""")

FILL_SUBSTITUTE = ("""INSERT INTO Food_substitute
                   (category_id, product_id, substitute_name, nutriscore, store, url)
                   VALUES (%s, %s, %s, %s, %s, %s)""")

# Query which return a substitute with a store
SELECT_SUB_STORE = ("""SELECT category_id, id_prod, product_name, nutriscore, store, url
                    FROM Food_product WHERE category_id = %s
                    AND nutriscore = 'a' AND store <> '' LIMIT 1""")

SELECT_SUBS = ("""SELECT id_subs, category_id, product_id, substitute_name, nutriscore, store, url
               FROM Food_substitute """)
