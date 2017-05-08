CREATE VIEW `reservas_Mias` AS

SELECT 

OrgU.idUsuario as 'Usuario ID',

(SELECT Organizacion.nombre_Org 
	FROM Organizacion 
	WHERE Organizacion.idUsuarioCreador = Re.idOrgCreador
			AND  Organizacion.consecutivoOrg = Re.idOrgConsecutivo) as Organizacion,

(SELECT Sede.nombreSede
	FROM Sede 
	WHERE Sede.idOrgUsuarioCreador = Re.idOrgCreador
			AND  Sede.idOrgConsecutivo = Re.idOrgConsecutivo
            AND  Sede.idSede = Re.idSede) as Sede,
     
(SELECT Bloque.nombreBloque
	FROM Bloque 
	WHERE Bloque.idOrgCreador = Re.idOrgCreador
			AND  Bloque.idOrgConsecutivo = Re.idOrgConsecutivo
            AND  Bloque.idSede = Re.idSede
            AND  Bloque.idBloque = Re.idBloque) as Bloque,
            
(SELECT CONCAT('Piso Numero '+ Nivel.numeroNivel)
	FROM Nivel 
	WHERE Nivel.idOrgCreador = Re.idOrgCreador
			AND  Nivel.idOrgConsecutivo = Re.idOrgConsecutivo
            AND  Nivel.idSede = Re.idSede
            AND  Nivel.idBloque = Re.idBloque
            AND  Nivel.idNivel = Re.idNivel) as Nivel,
            
(SELECT IF(Espacio.numeroNivel = Null, Espacio.numeroNivel, CONCAT(Espacio.numeroNivel + " Conocidco como: " + Espacio.nomenclaturaEspecial))
	FROM Espacio 
	WHERE Espacio.idOrgCreador = Re.idOrgCreador
			AND  Espacio.idOrgContador = Re.idOrgConsecutivo
            AND  Espacio.idSede = Re.idSede
            AND  Espacio.idBloque = Re.idBloque
            AND  Espacio.idNivel = Re.idNivel
            AND  Espacio.idEspacio = Re.idEspacio) as Espacio,

IF(Re.fechaFin >= NOW(),'Activo','Vencido') as Estado


FROM Reserva as Re INNER JOIN OrgUsuario as OrgU on ( Re.idUsuario = OrgU.idOrgUsuario)