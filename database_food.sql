DROP DATABASE IF EXISTS database_food;
CREATE DATABASE database_food CHARACTER SET 'utf8';
USE database_food;
GRANT ALL PRIVILEGES ON database_food.* TO 'P5'@'localhost';

  CREATE TABLE Food_category (
    id_cat INT UNSIGNED AUTO_INCREMENT NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_cat)
  )ENGINE=INNODB;

  CREATE TABLE Food_product (
    id_prod INT UNSIGNED AUTO_INCREMENT,
    category_id INT UNSIGNED NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    nutriscore VARCHAR(1)  DEFAULT NULL,
    store VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (id_prod)
  )ENGINE=INNODB;

  CREATE TABLE Food_substitute (
    id_subs INT UNSIGNED AUTO_INCREMENT,
    category_id INT UNSIGNED NOT NULL,
    substitute_name VARCHAR(255) DEFAULT NULL,
    url VARCHAR(255) NOT NULL,
    nutriscore VARCHAR(1) DEFAULT NULL,
    store VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (id_subs)
  )ENGINE=INNODB;

  ALTER TABLE Food_product
  ADD CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES Food_category(id_cat);
  ALTER TABLE Food_substitute
  ADD CONSTRAINT fk_product_source_id FOREIGN KEY (category_id) REFERENCES Food_category(id_cat);
