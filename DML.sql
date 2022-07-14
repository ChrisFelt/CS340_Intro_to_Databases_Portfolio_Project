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
SELECT rockID, Users.name AS owner, name, geoOrigin, type, description, chemicalComp
    FROM Rocks
        INNER JOIN Users
            ON Rocks.userID = Users.userID -- get name of User owner


-- -----------------------------------------------------
-- Reviews Data Manipulation Queries
-- -----------------------------------------------------

-- CREATE
-- add a new Review
INSERT INTO Reviews (userID, rockID, title, body, rating)
    VALUES (SELECT userID FROM Users WHERE name = :name_from_dropdown_input,
    SELECT rockID FROM Rocks WHERE name = :name_from_dropdown_input,
    title = :titleInput, body = :bodyInput, rating = :rating_from_dropdown_input)

-- READ
-- get all Reviews for the browse Reviews table
SELECT reviewID, Users.name AS reviewer, Rocks.name AS rock, title, body, rating
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
    SET reviewer = :userID_from_dropdown_input, rock = :rockID_from_rock_input, title = :titleInput,
    body = :bodyInput, rating = :ratingInput
    WHERE reviewID = :reviewID_selected_in_form


-- -----------------------------------------------------
-- Shipments Data Manipulation Queries
-- -----------------------------------------------------



-- -----------------------------------------------------
-- Shipments_has_Rocks Data Manipulation Queries
-- -----------------------------------------------------
