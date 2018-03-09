SELECT title, summary FROM db_tadey.film
WHERE LOWER(summary) LIKE LOWER("%Vincent%")
ORDER BY id_film;
