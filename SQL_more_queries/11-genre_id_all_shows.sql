-- lists all shows contained in the database hbtn_0d_tvshows
SELECT t.title, g.genre_id
FROM tv_shows.title AS t
LEFT JOIN tv_show_genres.genre_id AS g
ON t.id = g.show_id
ORDER BY t.title, g.genre_id;
