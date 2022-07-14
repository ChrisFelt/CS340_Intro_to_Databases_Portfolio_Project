-- CS 340 Intro to Databases
-- Project Step 3 Draft: DML
-- Team Rock Bottom
-- Members: Robert Behring and Christopher Felt


-- -----------------------------------------------------
-- Users Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new User
INSERT INTO Users (name, address, specialization, bio)
    VALUES (:nameInput, : addressInput, :specializationInput, :bioInput)

-- READ
-- get all Users for the browse Users table
SELECT userID, name, address, specialization, bio
    FROM Users

-- UPDATE
-- update a User's data using form input data
-- first, get User
SELECT userID, name, address, specialization, bio
    FROM Users
    WHERE userID = :userID_selected_in_form -- pulled from onclick event when edit User link is clicked
-- then, update User
UPDATE Users
    SET name = :nameInput, address = :addressInput, specialization = :specializationInput, bio = :bioInput
    WHERE userID = :userID_selected_in_form


-- -----------------------------------------------------
-- Rocks Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new Rock
INSERT INTO Rocks (userID, name, geoOrigin, type, description, chemicalComp)
    VALUES (SELECT userID FROM Users WHERE name = :name_from_dropdown_input,　-- what about Users with same name?
    name = :nameInput, geoOrigin = :geoOriginInput, type = :typeInput, chemicalComp = :chemicalCompInput)

-- READ
-- get all Rocks for the browse Rocks table
SELECT rockID, SELECT name FROM Users INNER JOIN Rocks ON Users.userID = Rocks.userID,
    name, geoOrigin, type, description, chemicalComp
    FROM Rocks


-- -----------------------------------------------------
-- Reviews Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Shipments Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Shipments_has_Rocks Data Manipulation Queries
-- -----------------------------------------------------
