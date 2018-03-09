INSERT INTO db_tadey.ft_table (login, `group`, creation_date)
SELECT last_name, 'other', birthdate FROM db_tadey.user_card
WHERE last_name LIKE '%a%' and char_length(last_name) < 9
ORDER BY last_name
LIMIT 10;
