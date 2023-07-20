-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
SELECT DISTINCT g.name
	FROM tv_genres g
	INNER JOIN tv_show_genres s ON g.id = s.genre_id
	INNER JOIN tv_shows t ON s.show_id = t.id
	WHERE g.name NOT IN (
SELECT DISTINCT g2.name
	FROM tv_genres g2
	INNER JOIN tv_show_genres s2 ON g2.id = s2.genre_id
	INNER JOIN tv_shows t2 ON s2.show_id = t2.id
	WHERE t2.title = 'Dexter'
	)
ORDER BY g.name ASC;
