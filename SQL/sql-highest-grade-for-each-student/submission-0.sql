-- Write your query below
-- DISTINCT obtem primeiro valor unico encontrado
SELECT DISTINCT ON (student_id)
    student_id,
    exam_id,
    score
FROM exam_results
-- score DESC coloca maior nota do estudante na primeira ocorrencia unica do id
ORDER BY student_id, score DESC, exam_id;