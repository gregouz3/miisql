DROP DATABASE IF EXISTS database_food;
DROP TABLE Food_category;
CREATE DATABASE database_food CHARACTER SET 'utf8';
USE database_food;
GRANT ALL PRIVILEGES ON database_food.* TO 'P5'@'localhost';

  CREATE TABLE Food_category (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE

  )ENGINE=INNODB;

  CREATE TABLE Food_product (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_id INT UNSIGNED NOT NULL,
    category VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    ingredients TEXT,
    store TEXT,
    nutriscore VARCHAR(1) NOT NULL

  )ENGINE=INNODB;

  CREATE TABLE Food_substitute (
    product_source_id INT UNSIGNED NOT NULL,
    substitute_id INT UNSIGNED NOT NULL

  )ENGINE=INNODB;

  ALTER TABLE Food_product
  ADD CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES Food_category(id);
  ALTER TABLE Food_substitute
  ADD CONSTRAINT fk_product_source_id FOREIGN KEY (product_source_id) REFERENCES Food_product(id),
  ADD CONSTRAINT fk_substitute_id FOREIGN KEY (substitute_id) REFERENCES Food_product(id);
