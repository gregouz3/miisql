#!/usr/bin/python3

# -*- coding: Utf-8 -*

'''
Main program of the application that displays a selected product and a substitute product.
User can save to database and view registered product.
'''
import mysql.connector
from classes import *
from constants import *

# Create a list for the substitutes
substitute_food = list()

def display_category():
    """Function which display the categories choice in constants.py"""

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(SELECT_CAT)
    # Display the categories
    for id_cat, category_name in cursor:
        print(id_cat, ':', category_name)

def display_products(category_choose):
    """Function which display the products according with category chosen"""

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(SELECT_CAT_PROD, category_choose)
    # Display the products with their name and nutriscore
    for id_prod, product_name, nutriscore in cursor:
        print(id_prod, ':', product_name, ', nutriscore : ', nutriscore)


def substitute(id_product):
    """Function which find and display and save a substitut product"""

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(SELECT_SUB_STORE, category_choose)
    # Display a substitute product description
    for  category_id, id_prod, product_name, nutriscore, store, url in cursor:
        print("\n Voici un substitut : {}, de la categorie n° {}."
              "\n Son nutriscore est de : {}. Ce produit est en vente à {} ."
              "\n Le lien OpenFoodFact : {} \n"
              .format(product_name, category_id, nutriscore, store, url))
        add_substitute = (category_id, id_prod, product_name, nutriscore, store, url)
        substitute_food.append(add_substitute)
        # Suggest to save the substitute products
        try:
            record_subs = (int(input("\nVoulez-vous enregistré ce substitut ?\n 1-Oui  2-Non ")))
        except ValueError:
            print("Vous n'avez pas sélectionné 1 ou 2")
            record_subs = (int(input("\n Voulez-vous enregistré ce substitut ?\n 1-Oui  2-Non ")))
        # Fill Food_substitute table with the list substitute_food
        if record_subs == 1:
            cursor.execute(FILL_SUBSTITUTE, add_substitute)
            cnx.commit()
        else:
            break

def save_product():
    """Function wich display the substitutes products in the database"""

    cnx = mysql.connector.connect(**CONFIG)
    cursor = cnx.cursor()
    cursor.execute(SELECT_SUBS)
    # Display the substitute products saving
    for id_subs, category_id, product_id, substitute_name, nutriscore, store, url in cursor:
        print('\n', id_subs, ':', substitute_name, ', \n Nutriscore : ', nutriscore,
              '\n Magasin : ', store, '\n id category : ', category_id,
              '\n id product : ', product_id, '\n Lien OpenFoodFact : ', url)
    cnx.commit()

if __name__ == '__main__':

    loop = True
    while loop:
        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()
        try:
            proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ?"
                                  "\n2- Retrouver mes aliments substitués.\n3- Exit "
                                  "\n -OpenFoodSubstitute-\n"))
        except  ValueError:
            print("Vous n'avez pas sélectionné 1, 2 ou 3")
            proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ? "
                                  "\n2- Retrouver mes aliments substitués."
                                  "\n3- Exit \n -OpenFoodSubstitute-\n"))

        while proposals not in (1, 2, 3):
            print("\n Sélectionnez 1 ou 2 pour utiliser -OpenFoodSubstitute- , "
                  "ou 3 pour quitter le programme ")
            try:
                proposals = int(input(("\n1- Quel aliment souhaitez-vous remplacer ?"
                                  "\n2- Retrouver mes aliments substitués.\n3- Exit "
                                  "\n -OpenFoodSubstitute-\n")))
            except  ValueError:
                print("Vous n'avez pas sélectionné 1, 2 ou 3")
                proposals = int(input("\n1- Quel aliment souhaitez-vous remplacer ?"
                                  "\n2- Retrouver mes aliments substitués.\n3- Exit "
                                  "\n -OpenFoodSubstitute-\n"))
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
            # Create a product selected
            p_select = Product()
            p_select.product_selected(id_product)
            # Display the description product selected
            p_select.display_product()
            substitute(id_product)

        if proposals == 2:
            # Display the substitute product save
            save_product()

    cnx.commit()
    cursor.close()
