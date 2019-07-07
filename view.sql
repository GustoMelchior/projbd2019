CREATE OR REPLACE VIEW
      esdb.projetos_extensao_curso
    AS
select c.nome as curso, p.nome as projeto from esdb.CURSO as c
    left join esdb.DEPARTAMENTO as d on d.idDEPARTAMENTO = c.DEPARTAMENTO_idDEPARTAMENTO
    inner join esdb.PROJETOS as p on p.DEPARTAMENTO_idDEPARTAMENTO = d.idDEPARTAMENTO;

select * from esdb.projetos_extensao_curso