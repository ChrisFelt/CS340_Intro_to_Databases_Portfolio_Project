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
), (
    'Rick McFarley',
    '101 Sedimentary Way, New York City, NY 10001'
), (
    'Bobby James',
    '6000 Metamorphic Drive, Rock City, NM 87311 USA',
    'Gem Cutter'
), (
    'Alice Liddel',
    '1 Igneous Court, Sydney, NSW 2000 Australia',
    'Amateur Rockhound'
), (
    'Jimothy Riley',
    'Riley Castle Way, London, W1D 3AF United Kingdom',
    'Mineral Photographer',
    "I've spent the last 23 years photographing priceless rocks all across the UK and US."
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
    'Quartz, Iron, Magnesium'
), (
    3,
    'The One Rock',
    'Mt. Ruapehu, New Zealand',
    'Igneous',
    'Vastly superior to rocks that suffer from any form of plurality.',
    'KALSi3O8'
), (
    4,
    'Old Man of the Mountain',
    'White Mountains, USA',
    'Igneous',
    'Shard from the OG.',
    'SiO2'
), (
    1,
    'Scarlet',
    'Wah Wah Mountains, USA',
    'Metamorphic',
    'Uncut red beryl in original rhyolite matrix. So shiny.',
    'Be3Al2Si6O18 + Mn'
), (
    1,
    'Rocky',
    'K2, Pakistan',
    'Igneous',
    'My little blue buddy',
    'SiO2 + Cu3(CO3)2(OH)2'
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
), (
    2,
    4,
    'not so good rock',
    "too shiny, didn't like it. ",
    2
), (
    2,
    2,
    'WOW THAT CRYSTAL STRUCTURE THO',
    'I cut it and ground it down into a thin section just so I could see the FANTASTIC twinning structure of the K-spar crystals under a microscope - THREE DAYS OF ROCK GRINDING WELL SPENT.',
    5
), (
    3,
    4,
    'meh',
    "Kind of your average, middle of the road rock. Honestly I'm not sure what the individual who sent this in was thinking. Clearly the caliber of his or her upbringing is questionable.",
    3
), (
    4,
    5,
    'Nope',
    'Not nearly as good as my rock, which is the best rock.',
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
), (
    4,
    '6000 Metamorphic Drive, Rock City, NM 87311 USA',
    '1 Igneous Court, Sydney, NSW 2000 Australia',
    2022-11-08,
    'VIP, HANDLE WITH CARE'
), (
    5,
    '101 Sedimentary Way, New York City, NY 10001',
    'Riley Castle Way, London, W1D 3AF United Kingdom',
    2023-07-07,
    'Special delivery instructions by Mr. Riley - leave at portcullis #2.'
), (
    3,
    'Riley Castle Way, London, W1D 3AF United Kingdom',
    '6000 Metamorphic Drive, Rock City, NM 87311 USA',
    2023-04-10,
    'User has requested the rock be rolled to its destination'
), (
    2,
    '1 Igneous Court, Sydney, NSW 2000 Australia',
    '101 Sedimentary Way',
    2022-12-24
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
), (
    2,
    4
), (
    3,
    3
), (
    4,
    5
), (
    5,
    2
);
