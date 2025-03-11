CREATE TABLE `movies`(
    `tconst` VARCHAR(255) NOT NULL,
    `titleType` VARCHAR(255) NOT NULL,
    `primaryTitle` VARCHAR(255) NOT NULL,
    `originalTitle` VARCHAR(255) NOT NULL,
    `isAdult` BOOLEAN NOT NULL,
    `startYear` YEAR NOT NULL,
    `runtimeMinutes` BIGINT NOT NULL,
    `movieGenres` VARCHAR(255) NOT NULL,
    `directors` BIGINT NOT NULL,
    `writers` BIGINT NOT NULL,
    `averageRating` FLOAT(53) NOT NULL,
    `numVotes` BIGINT NOT NULL,
    PRIMARY KEY(`tconst`)
);
CREATE TABLE `individuals`(
    `nconst` VARCHAR(255) NOT NULL,
    `primaryName` VARCHAR(255) NOT NULL,
    `birthYear` VARCHAR(255) NOT NULL,
    `deathYear` VARCHAR(255) NOT NULL,
    `primaryProfession` VARCHAR(255) NULL,
    `knownForTitles` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`nconst`)
);
CREATE TABLE `characters`(
    `ordering` BIGINT NOT NULL,
    `characters` VARCHAR(255) NOT NULL,
    `tconst` VARCHAR(255) NOT NULL,
    `nconst` VARCHAR(255) NOT NULL,
    `category` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`ordering`)
);
ALTER TABLE
    `movies` ADD CONSTRAINT `movies_writers_foreign` FOREIGN KEY(`writers`) REFERENCES `individuals`(`nconst`);
ALTER TABLE
    `characters` ADD CONSTRAINT `characters_tconst_foreign` FOREIGN KEY(`tconst`) REFERENCES `movies`(`tconst`);
ALTER TABLE
    `characters` ADD CONSTRAINT `characters_nconst_foreign` FOREIGN KEY(`nconst`) REFERENCES `individuals`(`nconst`);
ALTER TABLE
    `movies` ADD CONSTRAINT `movies_directors_foreign` FOREIGN KEY(`directors`) REFERENCES `individuals`(`nconst`);