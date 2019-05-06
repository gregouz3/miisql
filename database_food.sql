DROP DATABASE IF EXISTS database_food;
CREATE DATABASE database_food CHARACTER SET 'utf8';
USE database_food;
GRANT ALL PRIVILEGES ON database_food.* TO 'P5'@'localhost';

  CREATE TABLE Food_category (
    id INT UNSIGNED AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
  )ENGINE=INNODB;

  CREATE TABLE Food_product (
    id INT UNSIGNED AUTO_INCREMENT,
    category VARCHAR(255) DEFAULT NULL,
    product_name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    nutriscore VARCHAR(1)  DEFAULT NULL,
    store VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (id)
  )ENGINE=INNODB;


  CREATE TABLE Food_substitute (
    id INT UNSIGNED AUTO_INCREMENT,
    substitute_name VARCHAR(255) DEFAULT NULL,
    substitute_id_cat INT UNSIGNED NULL,
    substitute_id_prod INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
  )ENGINE=INNODB;

  ALTER TABLE Food_substitute
  ADD CONSTRAINT fk_category_source_id FOREIGN KEY (substitute_id_cat) REFERENCES Food_category(id),
  ADD CONSTRAINT fk_product_source_id FOREIGN KEY (substitute_id_prod) REFERENCES Food_product(id);
