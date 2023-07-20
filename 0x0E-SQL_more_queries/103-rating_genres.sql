-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- use only one SELECT statement
SELECT g.name, SUM(r.rate) AS rating
	FROM tv_genres g
	INNER JOIN tv_show_genres s ON s.genre_id = g.id
	INNER JOIN tv_show_ratings r ON r.show_id = s.show_id
	GROUP BY g.name
	ORDER BY rating DESC;
