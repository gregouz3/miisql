CREATE DATABASE database_food CHARACTER SET 'utf8';
USE database_foo

CREATE TABLE Food_category (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(255) UNIQUE,

)ENGINE=INNODB;

CREATE TABLE Product_data (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(255) UNIQUE,
  url VARCHAR(2000),
  code BIGINT UNSIGNED NOT NULL UNIQUE,
  ingredients TEXT,
  stores TEXT,
  nutrition_grades VARCHAR(1),
  food_category_id INT UNSIGNED,
  food_substitute_id INT UNSIGNED,

  ADD CONSTRAINT 'fk_food_category'
    FOREIGN KEY ('food_category_id') REFERENCES Food_category(id) ON DELETE CASCADE,
  ADD CONSTRAINT 'fk_food_substitute_id'
    FOREIGN KEY (food_substitute_id) REFERENCES Product_data(id) ON DELETE SET NULL

)ENGINE=INNODB;

