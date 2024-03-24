-- a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
LEFT JOIN tv_show_genres
ON genre_id = 
