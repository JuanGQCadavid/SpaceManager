-- MySQL Script generated by MySQL Workbench
-- 05/06/17 14:09:02
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema SpaceAdmind
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `SpaceAdmind` ;

-- -----------------------------------------------------
-- Schema SpaceAdmind
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SpaceAdmind` DEFAULT CHARACTER SET utf8 ;
USE `SpaceAdmind` ;

-- -----------------------------------------------------
-- Table `SpaceAdmind`.`RedesSociales`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`RedesSociales` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`RedesSociales` (
  `idRedesSociales` VARCHAR(91) NOT NULL,
  `FaceBook` VARCHAR(45) NULL,
  `Twitter` VARCHAR(45) NULL,
  `Linkedin` VARCHAR(45) NULL,
  `Instagram` VARCHAR(45) NULL,
  `Google` VARCHAR(45) NULL,
  PRIMARY KEY (`idRedesSociales`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`PrivacidadUsuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`PrivacidadUsuario` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`PrivacidadUsuario` (
  `idPrivacidadUsuario` VARCHAR(10) NOT NULL COMMENT 'Id = Mc + MorgP + MogrPer + MRedesS + MT\n\nID = GenericT = 11111\n     = GenericF = 00000',
  `MostrarCorreo` TINYINT(1) NOT NULL,
  `MostrarOrgPropias` TINYINT(1) NOT NULL,
  `MostrarOrgPertenece` TINYINT(1) NOT NULL,
  `MostrarRedesSociales` TINYINT(1) NOT NULL,
  `MostrarTelefono` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idPrivacidadUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Usuario` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Usuario` (
  `idUsuario` VARCHAR(45) NOT NULL COMMENT 'Probando Comentario = Joder',
  `claveUsuario` VARCHAR(25) NOT NULL,
  `nombreUsuario` VARCHAR(100) NOT NULL,
  `Descripcion` VARCHAR(230) NULL,
  `telefonoCelular` VARCHAR(25) NULL,
  `correoElectronico` VARCHAR(80) NOT NULL,
  `idRedesSociales` VARCHAR(45) NULL,
  `idPrivacidad` VARCHAR(10) NOT NULL,
  `estadoUsuario` TINYINT(1) NOT NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `idRedesSocialesUsuer_idx` (`idRedesSociales` ASC),
  INDEX `idPrivacidadU_idx` (`idPrivacidad` ASC),
  CONSTRAINT `idRedesSocialesUsuer`
    FOREIGN KEY (`idRedesSociales`)
    REFERENCES `SpaceAdmind`.`RedesSociales` (`idRedesSociales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPrivacidadU`
    FOREIGN KEY (`idPrivacidad`)
    REFERENCES `SpaceAdmind`.`PrivacidadUsuario` (`idPrivacidadUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Permisos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Permisos` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Permisos` (
  `idPermisos` VARCHAR(12) NOT NULL,
  `Boss` TINYINT(1) NOT NULL,
  `P_Reserva` TINYINT(1) NOT NULL,
  `P_Nivel` TINYINT(1) NOT NULL,
  `P_Bloque` TINYINT(1) NOT NULL,
  `P_Sede` TINYINT(1) NOT NULL,
  `P_Org` TINYINT(1) NOT NULL,
  `PC_B` TINYINT(1) NOT NULL,
  `PC_S` TINYINT(1) NOT NULL,
  `PC_N` TINYINT(1) NOT NULL,
  `PC_E` TINYINT(1) NOT NULL,
  `P_Encargado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idPermisos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Organizacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Organizacion` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Organizacion` (
  `idUsuarioCreador` VARCHAR(45) NOT NULL,
  `consecutivoOrg` INT(4) NOT NULL,
  `nombre_Org` VARCHAR(100) NOT NULL,
  `descripcion_Org` VARCHAR(140) NULL,
  `idPermisosEstandar` VARCHAR(45) NOT NULL,
  `idRedesSociales` VARCHAR(91) NULL,
  `TelefonoOrg` VARCHAR(45) NULL,
  `estadoOrg` TINYINT(1) NOT NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idUsuarioCreador`, `consecutivoOrg`),
  INDEX `idPermisosEstandar_idx` (`idPermisosEstandar` ASC),
  INDEX `IdRedesSociales_idx` (`idRedesSociales` ASC),
  CONSTRAINT `idPermisosEstandarOrg`
    FOREIGN KEY (`idPermisosEstandar`)
    REFERENCES `SpaceAdmind`.`Permisos` (`idPermisos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `IdRedesSociales`
    FOREIGN KEY (`idRedesSociales`)
    REFERENCES `SpaceAdmind`.`RedesSociales` (`idRedesSociales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCreadorUsuario`
    FOREIGN KEY (`idUsuarioCreador`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Pais`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Pais` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Pais` (
  `idPais` VARCHAR(45) NOT NULL,
  `nombreP` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPais`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Departamento` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Departamento` (
  `idDepartamento` VARCHAR(45) NOT NULL,
  `idPais` VARCHAR(45) NOT NULL,
  `nombreDep` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDepartamento`),
  INDEX `idPais_idx` (`idPais` ASC),
  CONSTRAINT `idPais`
    FOREIGN KEY (`idPais`)
    REFERENCES `SpaceAdmind`.`Pais` (`idPais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Ciudad`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Ciudad` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Ciudad` (
  `idCiudad` VARCHAR(45) NOT NULL,
  `idDepartamento` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCiudad`),
  INDEX `idDep_idx` (`idDepartamento` ASC),
  CONSTRAINT `idDep`
    FOREIGN KEY (`idDepartamento`)
    REFERENCES `SpaceAdmind`.`Departamento` (`idDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Direccion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Direccion` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Direccion` (
  `idDireccion` VARCHAR(45) NOT NULL,
  `idCiudad` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDireccion`),
  INDEX `idCiudad_idx` (`idCiudad` ASC),
  CONSTRAINT `idCiudad`
    FOREIGN KEY (`idCiudad`)
    REFERENCES `SpaceAdmind`.`Ciudad` (`idCiudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`OrgUsuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`OrgUsuario` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`OrgUsuario` (
  `idOrgUsuario` VARCHAR(97) NOT NULL COMMENT 'Pk = idOrgCreador + \'_$_ \' + idContador + \'@\' +idUsuario\n     =       45              +   3    +        3         +   1  +     45\n     =  97\n\nidContador  menor o igul 999',
  `idOrgUsuarioCreador` VARCHAR(45) NOT NULL,
  `idOrgContador` INT(4) NOT NULL,
  `idUsuario` VARCHAR(45) NOT NULL,
  `idPermisos` VARCHAR(12) NOT NULL,
  `nombrePilaUser` VARCHAR(45) NOT NULL,
  `estadoUsuario` VARCHAR(5) NOT NULL,
  `fechaEstado` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idOrgUsuario`),
  INDEX `idUsuario_idx` (`idUsuario` ASC),
  INDEX `idPermiso_idx` (`idPermisos` ASC),
  INDEX `idOrgOrgUsuario_idx` (`idOrgUsuarioCreador` ASC, `idOrgContador` ASC),
  CONSTRAINT `idUsuarioOrgUsuarioJoder`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idOrgGeneral`
    FOREIGN KEY (`idOrgUsuarioCreador` , `idOrgContador`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idUsuarioCreador` , `consecutivoOrg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPermisoOrgUsuarioJoder`
    FOREIGN KEY (`idPermisos`)
    REFERENCES `SpaceAdmind`.`Permisos` (`idPermisos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Sede`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Sede` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Sede` (
  `idSede` INT NOT NULL DEFAULT 0,
  `idOrgUsuarioCreador` VARCHAR(45) NOT NULL,
  `idOrgContador` INT NOT NULL DEFAULT 0,
  `idDireccionSede` VARCHAR(45) NULL,
  `idUsuarioEncargado` VARCHAR(97) NOT NULL,
  `nombreSede` VARCHAR(45) NOT NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idSede`, `idOrgUsuarioCreador`, `idOrgContador`),
  INDEX `idOrg_idx` (`idOrgUsuarioCreador` ASC, `idOrgContador` ASC),
  INDEX `idDireccion_idx` (`idDireccionSede` ASC),
  INDEX `idUsuarioEncargado_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idSedeOrgUsuarioCreador`
    FOREIGN KEY (`idOrgUsuarioCreador` , `idOrgContador`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idUsuarioCreador` , `consecutivoOrg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeDireccion`
    FOREIGN KEY (`idDireccionSede`)
    REFERENCES `SpaceAdmind`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idUsuarioEncargado`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Bloque`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Bloque` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Bloque` (
  `idBloque` INT NOT NULL DEFAULT 0,
  `idSede` INT NOT NULL DEFAULT 0,
  `idOrgCreador` VARCHAR(45) NOT NULL,
  `idOrgConsecutivo` INT NOT NULL DEFAULT 0,
  `nombreBloque` VARCHAR(45) NOT NULL,
  `idUsuarioEncargado` VARCHAR(97) NOT NULL,
  `descripcionBloqe` VARCHAR(140) NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idBloque`, `idSede`, `idOrgCreador`, `idOrgConsecutivo`),
  INDEX `idSede_idx` (`idSede` ASC, `idOrgCreador` ASC, `idOrgConsecutivo` ASC),
  INDEX `idBloqueUsuarioEncargado_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idBloqueSedeId`
    FOREIGN KEY (`idSede` , `idOrgCreador` , `idOrgConsecutivo`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede` , `idOrgUsuarioCreador` , `idOrgContador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idBloqueUsuarioEncargado`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`EspaciosPublicos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`EspaciosPublicos` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`EspaciosPublicos` (
  `idEspaciosPublcos` VARCHAR(4) NOT NULL,
  `tieneBanos` TINYINT(1) NOT NULL,
  `tieneCocineta` TINYINT(1) NOT NULL,
  `tieneSalaEstar` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idEspaciosPublcos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Nivel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Nivel` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Nivel` (
  `idNivel` INT NOT NULL,
  `idBloque` INT NOT NULL,
  `idSede` INT NOT NULL,
  `idOrgCreador` VARCHAR(45) NOT NULL,
  `idOrgConsecutivo` INT NOT NULL,
  `idUsuarioEncargado` VARCHAR(97) NOT NULL,
  `idEspacioPublico` VARCHAR(4) NOT NULL,
  `descripcionNivel` VARCHAR(140) NULL,
  `NumeroNivel` INT NOT NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idNivel`, `idBloque`, `idSede`, `idOrgCreador`, `idOrgConsecutivo`),
  INDEX `idBloque_idx` (`idBloque` ASC, `idSede` ASC, `idOrgCreador` ASC, `idOrgConsecutivo` ASC),
  INDEX `idEspaciosPublicos_idx` (`idEspacioPublico` ASC),
  INDEX `idUsuario_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idBloqueNivel`
    FOREIGN KEY (`idBloque` , `idSede` , `idOrgCreador` , `idOrgConsecutivo`)
    REFERENCES `SpaceAdmind`.`Bloque` (`idBloque` , `idSede` , `idOrgCreador` , `idOrgConsecutivo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idUsuarioNivel`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idEspaciosPublicosNivel`
    FOREIGN KEY (`idEspacioPublico`)
    REFERENCES `SpaceAdmind`.`EspaciosPublicos` (`idEspaciosPublcos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Espacio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Espacio` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Espacio` (
  `idEspacio` INT NOT NULL,
  `idNivel` INT NOT NULL,
  `idBloque` INT NOT NULL,
  `idSede` INT NOT NULL,
  `idOrgCreador` VARCHAR(45) NOT NULL,
  `idOrgContador` INT NOT NULL,
  `idPermiso` VARCHAR(12) NOT NULL,
  `capacidadEspacio` INT NOT NULL,
  `descripcionEspaco` VARCHAR(140) NULL,
  `NomenclaturaEspecal` VARCHAR(45) NULL,
  `fechaCreacion` TIMESTAMP NOT NULL,
  INDEX `idNivel_idx` (`idNivel` ASC, `idBloque` ASC, `idSede` ASC, `idOrgCreador` ASC, `idOrgContador` ASC),
  INDEX `idPermiso_idx` (`idPermiso` ASC),
  PRIMARY KEY (`idEspacio`, `idNivel`, `idBloque`, `idSede`, `idOrgCreador`, `idOrgContador`),
  CONSTRAINT `idNivelspacio`
    FOREIGN KEY (`idNivel` , `idBloque` , `idSede` , `idOrgCreador` , `idOrgContador`)
    REFERENCES `SpaceAdmind`.`Nivel` (`idNivel` , `idBloque` , `idSede` , `idOrgCreador` , `idOrgConsecutivo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPermisoEspacio`
    FOREIGN KEY (`idPermiso`)
    REFERENCES `SpaceAdmind`.`Permisos` (`idPermisos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`DiasHabiles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`DiasHabiles` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`DiasHabiles` (
  `idDiasHabiles` VARCHAR(8) NOT NULL,
  `lunes` TINYINT(1) NOT NULL,
  `martes` TINYINT(1) NOT NULL,
  `miercoles` TINYINT(1) NOT NULL,
  `jueves` TINYINT(1) NOT NULL,
  `viernes` TINYINT(1) NOT NULL,
  `sabado` TINYINT(1) NOT NULL,
  `domingo` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idDiasHabiles`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Reserva`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Reserva` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Reserva` (
  `idReserva` INT(8) NOT NULL,
  `idEspacio` INT NOT NULL,
  `idNivel` INT NOT NULL,
  `idBloque` INT NOT NULL,
  `idSede` INT NOT NULL,
  `idOrgCreador` VARCHAR(45) NOT NULL,
  `idOrgConsecutivo` INT(4) NOT NULL,
  `idUsuario` VARCHAR(97) NOT NULL,
  `idDiasReserva` VARCHAR(8) NOT NULL,
  `fechaInicio` DATE NOT NULL,
  `fechaFin` DATE NOT NULL,
  `horaInicio` TIME NOT NULL,
  `horaFin` TIME NOT NULL,
  `fechaReserva` TIMESTAMP NOT NULL,
  PRIMARY KEY (`idReserva`, `idEspacio`, `idNivel`, `idBloque`, `idSede`, `idOrgCreador`, `idOrgConsecutivo`, `idDiasReserva`, `fechaInicio`, `fechaFin`, `horaInicio`, `horaFin`),
  INDEX `idDiasHabiles_idx` (`idDiasReserva` ASC),
  INDEX `idUsuario_idx` (`idUsuario` ASC),
  INDEX `idEspaciosPk_idx` (`idEspacio` ASC, `idNivel` ASC, `idBloque` ASC, `idSede` ASC, `idOrgCreador` ASC, `idOrgConsecutivo` ASC),
  CONSTRAINT `idUsuarioReserva`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idDiasHabilesReserva`
    FOREIGN KEY (`idDiasReserva`)
    REFERENCES `SpaceAdmind`.`DiasHabiles` (`idDiasHabiles`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idEspaciosPk`
    FOREIGN KEY (`idEspacio` , `idNivel` , `idBloque` , `idSede` , `idOrgCreador` , `idOrgConsecutivo`)
    REFERENCES `SpaceAdmind`.`Espacio` (`idEspacio` , `idNivel` , `idBloque` , `idSede` , `idOrgCreador` , `idOrgContador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Modificacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Modificacion` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Modificacion` (
  `idModificacion` INT NOT NULL,
  `TipoModificacion` VARCHAR(45) NOT NULL,
  `ModOrg` VARCHAR(45) NULL,
  `ModSede` INT NULL,
  `ModBloque` INT NULL,
  `ModNivel` INT NULL,
  `ModEspacio` INT NULL,
  `ModUsuarioEnc` VARCHAR(45) NULL,
  `ModOrgCon` INT NULL,
  PRIMARY KEY (`idModificacion`),
  INDEX `ModUsuarioEn_idx` (`ModUsuarioEnc` ASC),
  INDEX `ModOrg_idx` (`ModOrg` ASC, `ModOrgCon` ASC),
  INDEX `ModSede_idx` (`ModSede` ASC),
  INDEX `ModBloque_idx` (`ModBloque` ASC),
  INDEX `ModNivel_idx` (`ModNivel` ASC),
  CONSTRAINT `ModUsuarioEn`
    FOREIGN KEY (`ModUsuarioEnc`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModOrg`
    FOREIGN KEY (`ModOrg` , `ModOrgCon`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idUsuarioCreador` , `consecutivoOrg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModSede`
    FOREIGN KEY (`ModSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModBloque`
    FOREIGN KEY (`ModBloque`)
    REFERENCES `SpaceAdmind`.`Bloque` (`idBloque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModNivel`
    FOREIGN KEY (`ModNivel`)
    REFERENCES `SpaceAdmind`.`Nivel` (`idNivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Logs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Logs` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Logs` (
  `idLogs` INT NOT NULL,
  `fechaLog` DATE NOT NULL,
  `usuarioLog` VARCHAR(45) NOT NULL,
  `IdModificacion` INT NOT NULL,
  PRIMARY KEY (`idLogs`),
  INDEX `UsuarioLog_idx` (`usuarioLog` ASC),
  INDEX `ModoficacionId_idx` (`IdModificacion` ASC),
  CONSTRAINT `UsuarioLog`
    FOREIGN KEY (`usuarioLog`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModoficacionId`
    FOREIGN KEY (`IdModificacion`)
    REFERENCES `SpaceAdmind`.`Modificacion` (`idModificacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Mensajes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Mensajes` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Mensajes` (
  `idMensajes` INT NOT NULL,
  `fechaMensaje` TIMESTAMP NOT NULL,
  `AsuntoMensaje` VARCHAR(45) NOT NULL,
  `DescripcionMensaje` VARCHAR(45) NOT NULL,
  `UsuarioAutor` VARCHAR(45) NOT NULL,
  `idOrgCreador` VARCHAR(45) NOT NULL,
  `idOrgContador` INT(4) NOT NULL,
  PRIMARY KEY (`idMensajes`),
  INDEX `OrgIdMensaje_idx` (`idOrgCreador` ASC, `idOrgContador` ASC),
  INDEX `AutorUsuarioId_idx` (`UsuarioAutor` ASC),
  CONSTRAINT `OrgIdMensaje`
    FOREIGN KEY (`idOrgCreador` , `idOrgContador`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idUsuarioCreador` , `consecutivoOrg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `AutorUsuarioId`
    FOREIGN KEY (`UsuarioAutor`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`HorarioSede`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`HorarioSede` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`HorarioSede` (
  `idDiasHabiles` VARCHAR(8) NOT NULL,
  `idSede` INT NOT NULL,
  `idOrgUsuarioCreador` VARCHAR(45) NOT NULL,
  `idOrgContador` INT NOT NULL,
  `HoraApertura` TIME NOT NULL,
  `HoraCierre` TIME NOT NULL,
  PRIMARY KEY (`idDiasHabiles`, `idSede`, `idOrgUsuarioCreador`, `idOrgContador`, `HoraApertura`, `HoraCierre`),
  INDEX `IdDiasHabilesSede_idx` (`idDiasHabiles` ASC),
  INDEX `idSedeHorario_idx` (`idSede` ASC, `idOrgUsuarioCreador` ASC, `idOrgContador` ASC),
  CONSTRAINT `IdDiasHabilesSede`
    FOREIGN KEY (`idDiasHabiles`)
    REFERENCES `SpaceAdmind`.`DiasHabiles` (`idDiasHabiles`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeHorario`
    FOREIGN KEY (`idSede` , `idOrgUsuarioCreador` , `idOrgContador`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede` , `idOrgUsuarioCreador` , `idOrgContador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `SpaceAdmind` ;

-- -----------------------------------------------------
-- Placeholder table for view `SpaceAdmind`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`view1` (`id` INT);

-- -----------------------------------------------------
-- procedure DataStart
-- -----------------------------------------------------

USE `SpaceAdmind`;
DROP procedure IF EXISTS `SpaceAdmind`.`DataStart`;

DELIMITER $$
USE `SpaceAdmind`$$
CREATE PROCEDURE `DataStart` ()
BEGIN

INSERT INTO PrivacidadUsuario VALUES ('GenericT',1,1,1,1,1);
INSERT INTO PrivacidadUsuario VALUES ('GenericF',0,0,0,0,0);
INSERT INTO RedesSociales VALUES ('GenericNull',null,null,null,null,null);
INSERT INTO Permisos VALUES ('theBoss',1,1,1,1,1,1,1,1,1,1,1);
INSERT INTO Permisos VALUES ('invitado',0,0,0,0,0,0,0,0,0,0,0);

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure orgsContador
-- -----------------------------------------------------

USE `SpaceAdmind`;
DROP procedure IF EXISTS `SpaceAdmind`.`orgsContador`;

DELIMITER $$
USE `SpaceAdmind`$$
CREATE PROCEDURE `orgsContador` (in userId varchar(45), inout times int)
BEGIN
	SELECT COUNT(*) INTO times
    FROM Organizacion
    WHERE Organizacion.idUsuarioCreador = userId;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- function obtenerConsecutivo
-- -----------------------------------------------------

USE `SpaceAdmind`;
DROP function IF EXISTS `SpaceAdmind`.`obtenerConsecutivo`;

DELIMITER $$
USE `SpaceAdmind`$$
CREATE FUNCTION `obtenerConsecutivo` (userId varchar(45))
RETURNS INT DETERMINISTIC
BEGIN
	set @result = 0;
	CALL orgsContador(userId,@result);
    RETURN @result;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- View `SpaceAdmind`.`view1`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `SpaceAdmind`.`view1` ;
DROP TABLE IF EXISTS `SpaceAdmind`.`view1`;
USE `SpaceAdmind`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
