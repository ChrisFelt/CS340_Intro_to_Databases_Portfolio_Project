-- CS 340 Intro to Databases
-- Project Step 3 Draft: DML
-- Team Rock Bottom
-- Members: Robert Behring and Christopher Felt


-- -----------------------------------------------------
-- Users Data Manipulation Queries
-- -----------------------------------------------------

-- get all Users for the browse Users table
SELECT userID, name, address, specialization, bio
    FROM Users

-- add a new User
INSERT INTO Users (name, address, specialization, bio)
    VALUES (:nameInput, : addressInput, :specializationInput, :bioInput)

-- update a User's data using form input data
-- first, get User
SELECT userID, name, address, specialization, bio
    FROM Users
    WHERE userID = :userID_selected_in_form -- pulled from onclick event when edit link is clicked
-- then, update User
UPDATE Users
    SET name = :nameInput, address = :addressInput, specialization = :specializationInput, bio = :bioInput
    WHERE userID = :userID_selected_in_form


-- -----------------------------------------------------
-- Rocks Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Reviews Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Shipments Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Shipments_has_Rocks Data Manipulation Queries
-- -----------------------------------------------------
