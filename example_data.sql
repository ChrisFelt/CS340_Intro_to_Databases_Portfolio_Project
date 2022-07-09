-- CS 340 Intro to Databases
-- Project Step 2 Draft: example_data for DDL.sql
-- Team Rock Bottom
-- Members: Robert Behring and Christopher Felt
-- INSERT INTO queries will be tested here before merging
--   with DDL.sql file

-- -----------------------------------------------------
-- Table Users
-- -----------------------------------------------------
INSERT INTO Users ( 
    name,
    address,
    specialization,
    bio
)
VALUES (
    'Ricky',
    '123 Rocky Road',
    'Rolling Rocks',
    'Ricky has spent most of his life rolling rocks, aiming to be the very best there ever was'
);

-- -----------------------------------------------------
-- Table Rocks
-- -----------------------------------------------------
INSERT INTO Rocks (
    userID,
    name,
    geoOrigin,
    type,
    description,
    chemicalComp,
    reviewAvg
)
VALUES (
    1,
    'Mossy Rock',
    'Appalachia',
    'Igneous',
    'A rock for rolling, has moss growing on it',
    'Quartz, Iron, Magnesium',
    5.00
);

-- -----------------------------------------------------
-- Table Reviews
-- -----------------------------------------------------
INSERT INTO Reviews (
    userID,
    rockID,
    title,
    body,
    rating
)
VALUES (
    1,
    1,
    'BEST ROCK EVER',
    'The original rolling stone, why would anyone ever want another?',
    5
);

-- -----------------------------------------------------
-- Table Shipments
-- -----------------------------------------------------
INSERT INTO Shipments (
    userID,
    shipOrigin,
    shipDest,
    shipDate,
    miscNote
)
VALUES (
    1,
    'Rocklohoma',
    '123 Rocky Road',
    2022-02-02,
    'User has requested the rock be rolled to its destination'
);

-- -----------------------------------------------------
-- Table Shipments_has_Rocks
-- -----------------------------------------------------
INSERT INTO Shipments_has_Rocks (
    shipmentID,
    rockID
)
VALUES (
    1,
    1
);
