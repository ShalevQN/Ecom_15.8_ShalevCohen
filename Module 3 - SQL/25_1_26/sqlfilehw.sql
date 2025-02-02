--1
CREATE TABLE countries (
country_id INTEGER PRIMARY KEY AUTOINCREMENT,
country_name TEXT UNIQUE NOT NULL,
country_language TEXT NOT NULL,
country_capital TEXT NOT NULL);


CREATE TABLE songs (
song_id INTEGER PRIMARY KEY AUTOINCREMENT,
song_name TEXT UNIQUE NOT NULL,
song_language TEXT NOT NULL,
singer TEXT NOT NULL);


CREATE TABLE competitions (
competition_year INTEGER PRIMARY KEY,
hosting_country_id INTEGER NOT NULL,
FOREIGN KEY (hosting_country_id) REFERENCES countries(country_id));


CREATE TABLE winners (
competition_year INTEGER,
winning_country_id INTEGER NOT NULL,
song_id INTEGER NOT NULL,
PRIMARY KEY (competition_year),
FOREIGN KEY (competition_year) REFERENCES competitions(competition_year),
FOREIGN KEY (winning_country_id) REFERENCES countries(country_id),
FOREIGN KEY (song_id) REFERENCES songs(song_id));

--2
INSERT INTO countries (country_name, country_language, country_capital) VALUES
('Sweden', 'Swedish', 'Stockholm'),
('Switzerland', 'German', 'Bern'),
('United Kingdom', 'English', 'London'),
('Ukraine', 'Ukrainian', 'Kyiv'),
('Italy', 'Italian', 'Rome'),
('Netherlands', 'Dutch', 'Amsterdam'),
('Israel', 'Hebrew', 'Jerusalem'),
('Portugal', 'Portuguese', 'Lisbon'),
('Austria', 'German', 'Vienna'),
('Denmark', 'Danish', 'Copenhagen'),
('Azerbaijan', 'Azerbaijani', 'Baku');


INSERT INTO songs (song_name, song_language, singer) VALUES
('The Code', 'English', 'Nemo'),
('Tattoo', 'English', 'Loreen'),
('Stefania', 'Ukrainian', 'Kalush Orchestra'),
('Zitti e buoni', 'Italian', 'Måneskin'),
('Arcade', 'English', 'Duncan Laurence'),
('Toy', 'English', 'Netta'),
('Amar pelos dois', 'Portuguese', 'Salvador Sobral'),
('1944', 'English/Ukrainian', 'Jamala'),
('Heroes', 'English', 'Måns Zelmerlöw'),
('Rise Like a Phoenix', 'English', 'Conchita Wurst'),
('Only Teardrops', 'English', 'Emmelie de Forest'),
('Euphoria', 'English', 'Loreen');


INSERT INTO competitions (competition_year, hosting_country_id) VALUES
(2024, (SELECT country_id FROM countries WHERE country_name = 'Sweden')),
(2023, (SELECT country_id FROM countries WHERE country_name = 'United Kingdom')),
(2022, (SELECT country_id FROM countries WHERE country_name = 'Italy')),
(2021, (SELECT country_id FROM countries WHERE country_name = 'Netherlands')),
(2019, (SELECT country_id FROM countries WHERE country_name = 'Israel')),
(2018, (SELECT country_id FROM countries WHERE country_name = 'Portugal')),
(2017, (SELECT country_id FROM countries WHERE country_name = 'Ukraine')),
(2016, (SELECT country_id FROM countries WHERE country_name = 'Sweden')),
(2015, (SELECT country_id FROM countries WHERE country_name = 'Austria')),
(2014, (SELECT country_id FROM countries WHERE country_name = 'Denmark')),
(2013, (SELECT country_id FROM countries WHERE country_name = 'Sweden')),
(2012, (SELECT country_id FROM countries WHERE country_name = 'Azerbaijan'));


INSERT INTO winners (competition_year, winning_country_id, song_id) VALUES
(2024, (SELECT country_id FROM countries WHERE country_name = 'Switzerland'), (SELECT song_id FROM songs WHERE song_name = 'The Code')),
(2023, (SELECT country_id FROM countries WHERE country_name = 'Sweden'), (SELECT song_id FROM songs WHERE song_name = 'Tattoo')),
(2022, (SELECT country_id FROM countries WHERE country_name = 'Ukraine'), (SELECT song_id FROM songs WHERE song_name = 'Stefania')),
(2021, (SELECT country_id FROM countries WHERE country_name = 'Italy'), (SELECT song_id FROM songs WHERE song_name = 'Zitti e buoni')),
(2019, (SELECT country_id FROM countries WHERE country_name = 'Netherlands'), (SELECT song_id FROM songs WHERE song_name = 'Arcade')),
(2018, (SELECT country_id FROM countries WHERE country_name = 'Israel'), (SELECT song_id FROM songs WHERE song_name = 'Toy')),
(2017, (SELECT country_id FROM countries WHERE country_name = 'Portugal'), (SELECT song_id FROM songs WHERE song_name = 'Amar pelos dois')),
(2016, (SELECT country_id FROM countries WHERE country_name = 'Ukraine'), (SELECT song_id FROM songs WHERE song_name = '1944')),
(2015, (SELECT country_id FROM countries WHERE country_name = 'Sweden'), (SELECT song_id FROM songs WHERE song_name = 'Heroes')),
(2014, (SELECT country_id FROM countries WHERE country_name = 'Austria'), (SELECT song_id FROM songs WHERE song_name = 'Rise Like a Phoenix')),
(2013, (SELECT country_id FROM countries WHERE country_name = 'Denmark'), (SELECT song_id FROM songs WHERE song_name = 'Only Teardrops')),
(2012, (SELECT country_id FROM countries WHERE country_name = 'Sweden'), (SELECT song_id FROM songs WHERE song_name = 'Euphoria'));

--3
SELECT c.competition_year, h.country_name AS hosting_country, w.country_name AS winning_country, w.country_language, s.song_name, s.song_language, w.country_capital, s.singer
FROM competitions c
JOIN winners win ON c.competition_year = win.competition_year
JOIN countries h ON c.hosting_country_id = h.country_id
JOIN countries w ON win.winning_country_id = w.country_id
JOIN songs s ON win.song_id = s.song_id;
