-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gelato_store_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gelato_store_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gelato_store_project` DEFAULT CHARACTER SET utf8 ;
USE `gelato_store_project` ;

-- -----------------------------------------------------
-- Table `gelato_store_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`ice_creams_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`ice_creams_types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_name` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`ice_creams_sizes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`ice_creams_sizes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `size_name` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`ice_creams_deliveries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`ice_creams_deliveries` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `delivery_type` VARCHAR(255) NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`ice_creams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`ice_creams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` INT NULL,
  `ice_cream_type_id` INT NOT NULL,
  `ice_cream_size_id` INT NOT NULL,
  `ice_cream_delivery_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ice_creams_ice_creams_types1_idx` (`ice_cream_type_id` ASC) VISIBLE,
  INDEX `fk_ice_creams_ice_creams_sizes1_idx` (`ice_cream_size_id` ASC) VISIBLE,
  INDEX `fk_ice_creams_ice_creams_deliveries1_idx` (`ice_cream_delivery_id` ASC) VISIBLE,
  CONSTRAINT `fk_ice_creams_ice_creams_types1`
    FOREIGN KEY (`ice_cream_type_id`)
    REFERENCES `gelato_store_project`.`ice_creams_types` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ice_creams_ice_creams_sizes1`
    FOREIGN KEY (`ice_cream_size_id`)
    REFERENCES `gelato_store_project`.`ice_creams_sizes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ice_creams_ice_creams_deliveries1`
    FOREIGN KEY (`ice_cream_delivery_id`)
    REFERENCES `gelato_store_project`.`ice_creams_deliveries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `ice_cream_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orders_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_orders_ice_creams1_idx` (`ice_cream_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `gelato_store_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_ice_creams1`
    FOREIGN KEY (`ice_cream_id`)
    REFERENCES `gelato_store_project`.`ice_creams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`toppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`toppings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `topping_name` VARCHAR(150) NULL,
  `price` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`ice_creams_has_toppings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`ice_creams_has_toppings` (
  `ice_cream_id` INT NOT NULL,
  `topping_id` INT NOT NULL,
  PRIMARY KEY (`ice_cream_id`, `topping_id`),
  INDEX `fk_ice_creams_has_toppings_toppings1_idx` (`topping_id` ASC) VISIBLE,
  INDEX `fk_ice_creams_has_toppings_ice_creams1_idx` (`ice_cream_id` ASC) VISIBLE,
  CONSTRAINT `fk_ice_creams_has_toppings_ice_creams1`
    FOREIGN KEY (`ice_cream_id`)
    REFERENCES `gelato_store_project`.`ice_creams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ice_creams_has_toppings_toppings1`
    FOREIGN KEY (`topping_id`)
    REFERENCES `gelato_store_project`.`toppings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gelato_store_project`.`pasts_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gelato_store_project`.`pasts_orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `favorite` TINYINT NULL,
  `user_id` INT NOT NULL,
  `ice_cream_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pasts_orders_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_pasts_orders_ice_creams1_idx` (`ice_cream_id` ASC) VISIBLE,
  CONSTRAINT `fk_pasts_orders_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `gelato_store_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pasts_orders_ice_creams1`
    FOREIGN KEY (`ice_cream_id`)
    REFERENCES `gelato_store_project`.`ice_creams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
