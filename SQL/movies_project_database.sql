-- Ensure the database exists
CREATE DATABASE IF NOT EXISTS movies_project;

-- Use the created or existing database
USE movies_project;

-- Create the `movies` table if it doesn't exist
CREATE TABLE IF NOT EXISTS `movies`(
    `tconst` VARCHAR(255) NOT NULL,
    `titleType` VARCHAR(255) NOT NULL,
    `primaryTitle` VARCHAR(255) NOT NULL,
    `originalTitle` VARCHAR(255) NOT NULL,
    `startYear` YEAR NOT NULL,
    `runtimeMinutes` BIGINT NOT NULL,
    `movieGenres` VARCHAR(255) NOT NULL,
    `averageRating` FLOAT NULL, -- Allowing NULL
    `numVotes` BIGINT NULL, -- Allowing NULL
    PRIMARY KEY(`tconst`)
);

-- Create the `individuals` table if it doesn't exist
CREATE TABLE IF NOT EXISTS `individuals`(
    `nconst` VARCHAR(255) NOT NULL,
    `primaryName` VARCHAR(255) NOT NULL,
    `birthYear` VARCHAR(255) NULL,
    `deathYear` VARCHAR(255) NULL,
    `primaryProfession` VARCHAR(255) NULL,
    `knownForTitles` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`nconst`)
);

-- Create the `characters` table if it doesn't exist
CREATE TABLE IF NOT EXISTS `characters`(
    `ordering` BIGINT NOT NULL,
    `characters` VARCHAR(255) NOT NULL,
    `tconst` VARCHAR(255) NOT NULL,
    `nconst` VARCHAR(255) NOT NULL,
    `category` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`ordering`)
);

CREATE TABLE IF NOT EXISTS `crew`(
    `id` BIGINT NOT NULL,
    `tconst` VARCHAR(255) NOT NULL,
    `directors` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
);


ALTER TABLE
    `characters` ADD CONSTRAINT `characters_tconst_foreign` FOREIGN KEY(`tconst`) REFERENCES `movies`(`tconst`);
ALTER TABLE
    `characters` ADD CONSTRAINT `characters_nconst_foreign` FOREIGN KEY(`nconst`) REFERENCES `individuals`(`nconst`);
ALTER TABLE
    `crew` ADD CONSTRAINT `crew_directors_foreign` FOREIGN KEY(`directors`) REFERENCES `individuals`(`nconst`);
ALTER TABLE
    `crew` ADD CONSTRAINT `crew_tconst_foreign` FOREIGN KEY(`tconst`) REFERENCES `movies`(`tconst`);