-- script that lists all shows without the genre Comedy in the
-- database hbtn_0d_tvshows
-- The tv_genres table contains only one record where
-- name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command
-- list all shows without the genre Comedy
SELECT DISTINCT title 
FROM tv_shows 
WHERE tv_shows.id 
NOT IN 
    (SELECT show_id 
     FROM tv_show_genres 
     INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
     WHERE tv_genres.name = 'Comedy') 
ORDER BY title ASC;
