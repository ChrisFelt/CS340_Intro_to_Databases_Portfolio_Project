-- CS 340 Intro to Databases
-- Project Step 2 Draft: DDL
-- Team Rock Bottom
-- Members: Robert Behring and Christopher Felt
-- Modified from MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Table Users
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Users (
  userID INT NOT NULL AUTO_INCREMENT UNIQUE,
  name VARCHAR(75) NOT NULL,
  address VARCHAR(155) NOT NULL,
  specialization VARCHAR(155) NULL,
  bio VARCHAR(3000) NULL,
  PRIMARY KEY (userID));


-- -----------------------------------------------------
-- Table Rocks
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Rocks (
  rockID INT NOT NULL AUTO_INCREMENT UNIQUE,
  userID INT NOT NULL,
  name VARCHAR(75) NOT NULL,
  geoOrigin VARCHAR(155) NOT NULL,
  type VARCHAR(75) NOT NULL,
  description VARCHAR(255) NOT NULL,
  chemicalComp VARCHAR(155) NOT NULL,
  reviewAvg DECIMAL(3,2) UNSIGNED NOT NULL,
  PRIMARY KEY (rockID),
  CONSTRAINT fk_Rocks_Users1
    FOREIGN KEY (userID)
    REFERENCES Users (userID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table Reviews
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Reviews (
  reviewID INT NOT NULL AUTO_INCREMENT UNIQUE,
  userID INT NOT NULL,
  rockID INT NOT NULL,
  title VARCHAR(75) NOT NULL,
  body VARCHAR(3000) NOT NULL,
  rating TINYINT(1) UNSIGNED NOT NULL,
  PRIMARY KEY (reviewID),
  CONSTRAINT fk_Reviews_Users1
    FOREIGN KEY (userID)
    REFERENCES Users (userID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Reviews_Rocks1
    FOREIGN KEY (rockID)
    REFERENCES Rocks (rockID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table Shipments
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Shipments (
  shipmentID INT NOT NULL AUTO_INCREMENT UNIQUE,
  userID INT NOT NULL,
  shipOrigin VARCHAR(255) NOT NULL,
  shipDest VARCHAR(255) NOT NULL,
  shipDate DATE NOT NULL,
  miscNote VARCHAR(3000) NULL,
  PRIMARY KEY (shipmentID),
  CONSTRAINT fk_Shipments_Users1
    FOREIGN KEY (userID)
    REFERENCES Users (userID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table Shipments_has_Rocks
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Shipments_has_Rocks (
  shipmentHasRockID INT NOT NULL AUTO_INCREMENT UNIQUE,
  shipmentID INT NOT NULL,
  rockID INT NOT NULL,
  PRIMARY KEY (shipmentHasRockID),
  CONSTRAINT fk_Shipments_has_Rocks_Shipments1
    FOREIGN KEY (shipmentID)
    REFERENCES Shipments (shipmentID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Shipments_has_Rocks_Rocks1
    FOREIGN KEY (rockID)
    REFERENCES Rocks (rockID)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
