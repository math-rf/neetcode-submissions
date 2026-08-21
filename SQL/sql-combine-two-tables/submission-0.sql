-- Write your query below
SELECT
    p.first_name,
    p.last_name,
    a.city,
    a.state
-- LEFT JOIN garante retorno de toda tabela a esquerda (person) com null onde nao ha correspondencia
FROM person p LEFT JOIN address a ON (p.person_id = a.person_id)