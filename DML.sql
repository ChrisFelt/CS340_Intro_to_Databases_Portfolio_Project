-- CS 340 Intro to Databases
-- Project Step 3 Draft: DML
-- Team Rock Bottom
-- Members: Robert Behring and Christopher Felt


-- -----------------------------------------------------
-- Users Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new User
INSERT INTO Users (firstName, lastName, address, specialization, bio)
    VALUES (:firstNameInput,
    :lastNameInput,
    :addressInput,
    :specializationInput,
    :bioInput)

-- READ
-- get all Users for the browse Users table
SELECT userID, firstName, lastName, address, specialization, bio
    FROM Users

-- UPDATE
-- update a User's data using form input data
-- first, get User
SELECT userID, firstName, lastName, address, specialization, bio
    FROM Users
    WHERE userID = :userID_selected_in_form -- pulled from onclick event when edit User link is clicked
-- then, update User
UPDATE Users
    SET firstNme = :firstNameInput,
    lastName = :lastNameInput,
    address = :addressInput,
    specialization = :specializationInput,
    bio = :bioInput
    WHERE userID = :userID_selected_in_form


-- -----------------------------------------------------
-- Rocks Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new Rock
INSERT INTO Rocks (userID, name, geoOrigin, type, description, chemicalComp)
    VALUES (SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = :name_from_dropdown_input,　
    name = :nameInput,
    geoOrigin = :geoOriginInput,
    type = :typeInput,
    chemicalComp = :chemicalCompInput)

-- READ
-- get all Rocks for the browse Rocks table
SELECT rockID, CONCAT(Users.firstName, ' ', Users.lastName) AS owner, name, geoOrigin, type, description, chemicalComp
    FROM Rocks
        INNER JOIN Users
            ON Rocks.userID = Users.userID -- get name of User owner


-- -----------------------------------------------------
-- Reviews Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new Review
INSERT INTO Reviews (userID, rockID, title, body, rating)
    VALUES (SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = :name_from_dropdown_input,
    SELECT rockID FROM Rocks WHERE name = :name_from_dropdown_input,
    title = :titleInput,
    body = :bodyInput,
    rating = :rating_from_dropdown_input)

-- READ
-- get all Reviews for the browse Reviews table
SELECT reviewID, CONCAT(Users.firstName, ' ', Users.lastName) AS reviewer, Rocks.name AS rock, title, body, rating
    FROM Reviews
        INNER JOIN Users
            ON Reviews.userID = Users.userID -- User doing Review
        INNER JOIN Rocks
            ON Reviews.rockID = Rocks.rockID -- name of Rock for Review

-- UPDATE
-- update Review data using form input data
-- first, get Review
SELECT reviewID, reviewer, rock, title, body, rating
    FROM Reviews
    WHERE reviewID = :reviewID_selected_in_form -- pulled from onclick event when edit Review link is clicked
-- then, update Review
UPDATE Reviewers
    SET reviewer = :userID_from_dropdown_input,
    rock = :rockID_from_rock_input,
    title = :titleInput,
    body = :bodyInput,
    rating = :ratingInput
    WHERE reviewID = :reviewID_selected_in_form


-- -----------------------------------------------------
-- Shipments Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- SHIP -FROM- USER
-- Part I: insert new row in Shipments
INSERT INTO Shipments (userID, shipOrigin, shipDest, shipDate, miscNote)
    VALUES (SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = :name_from_dropdown_input,
    SELECT address FROM Users WHERE CONCAT(firstName, ' ', lastName) = :auto_populates_from_name_dropdown_input,
    shipDest = :shipDestInput,
    shipDate = :shipDateInput,
    miscNote = :miscNoteInput)
-- Part II: insert new row in Shipments_has_Rocks intersection table
INSERT INTO Shipments_has_Rocks (shipmentID, rockID)
    VALUES (SELECT shipmentID FROM Shipments WHERE shipOrigin = :auto_populates AND shipDest = :auto_populates AND
    shipDate = :auto_populates,
    SELECT rockID FROM Rocks WHERE name = :name_from_dropdown_input)

-- CREATE
-- SHIP -TO- USER
-- Part I: insert new row in Shipments
INSERT INTO Shipments (userID, shipOrigin, shipDest, shipDate, miscNote)
    VALUES (SELECT address FROM Users WHERE CONCAT(firstName, ' ', lastName) = :auto_populates_from_name_dropdown_input,
    SELECT userID FROM Users WHERE CONCAT(firstName, ' ', lastName) = :name_from_dropdown_input,
    shipDest = :shipDestInput,
    shipDate = :shipDateInput,
    miscNote = :miscNoteInput)
-- Part II: insert new row in Shipments_has_Rocks intersection table
INSERT INTO Shipments_has_Rocks (shipmentID, rockID)
    VALUES (SELECT shipmentID FROM Shipments WHERE shipOrigin = :auto_populates AND shipDest = :auto_populates AND
    shipDate = :auto_populates,
    SELECT rockID FROM Rocks WHERE name = :name_from_dropdown_input)



-- -----------------------------------------------------
-- Shipments_has_Rocks Data Manipulation Queries
-- -----------------------------------------------------
