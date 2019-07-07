DELIMITER $$
CREATE PROCEDURE esdb.consultadenota (nota INT)
BEGIN
SELECT c.nome
FROM esdb.CURSO as c
INNER JOIN esdb.AVALIACAO AS a on c.idcurso = a.curso_idcurso
WHERE a.nota > nota;
END $$
call esdb.consultadenota(4);