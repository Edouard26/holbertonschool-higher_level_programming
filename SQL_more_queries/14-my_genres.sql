-- From database hbtn_0d_tvshows
-- List all genres from hbtn_0d_tvshows and display nuumber of shows linked to each
-- TV SHOW GENRE -> Num of shows
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.id;
