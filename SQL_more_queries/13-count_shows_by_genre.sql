-- From database hbtn_0d_tvshows
-- List all genres from hbtn_0d_tvshows and display nuumber of shows linked to each
-- TV SHOW GENRE -> Num of shows
SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY COUNT(*) DESC;
