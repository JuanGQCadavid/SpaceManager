-- MySQL Script generated by MySQL Workbench
-- Mon Apr 24 17:16:48 2017
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
  `idRedesSociales` VARCHAR(45) NOT NULL,
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
  `idPrivacidadUsuario` VARCHAR(45) NOT NULL,
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
  `idUsuario` VARCHAR(45) NOT NULL,
  `claveUsuario` VARCHAR(25) NOT NULL,
  `nombreUsuario` VARCHAR(100) NOT NULL,
  `Descripcion` VARCHAR(230) NULL,
  `telefonoCelular` VARCHAR(25) NULL,
  `correoElectronico` VARCHAR(80) NOT NULL,
  `idRedesSociales` VARCHAR(45) NULL,
  `idPrivacidad` VARCHAR(45) NOT NULL,
  `estadoUsuario` TINYINT(1) NOT NULL,
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
  `idPermisos` VARCHAR(45) NOT NULL,
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
-- Table `SpaceAdmind`.`OrgUsuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`OrgUsuario` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`OrgUsuario` (
  `idOrgUsuario` VARCHAR(90) NOT NULL,
  `idUsuario` VARCHAR(45) NOT NULL,
  `idOrg` VARCHAR(45) NOT NULL,
  `idPermisos` VARCHAR(45) NOT NULL,
  `nombrePilaUser` VARCHAR(45) NOT NULL,
  `estadoUsuario` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idOrgUsuario`),
  INDEX `idUsuario_idx` (`idUsuario` ASC),
  INDEX `idOrg_idx` (`idOrg` ASC),
  INDEX `idPermiso_idx` (`idPermisos` ASC),
  CONSTRAINT `idUsuarioOrgU`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idOrgOrgU`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPermisoOrgU`
    FOREIGN KEY (`idPermisos`)
    REFERENCES `SpaceAdmind`.`Permisos` (`idPermisos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Organizacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Organizacion` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Organizacion` (
  `idOrganizacion` VARCHAR(45) NOT NULL,
  `idUsuarioEncargado` VARCHAR(90) NOT NULL,
  `nombre_Org` VARCHAR(100) NOT NULL,
  `numero_Sedes` INT NOT NULL DEFAULT 0,
  `descripcion_Org` VARCHAR(140) NULL,
  `idPermisosEstandar` VARCHAR(45) NOT NULL,
  `idRedesSociales` VARCHAR(45) NULL,
  `TelefonoOrg` VARCHAR(45) NULL,
  PRIMARY KEY (`idOrganizacion`),
  INDEX `idPermisosEstandar_idx` (`idPermisosEstandar` ASC),
  INDEX `IdRedesSociales_idx` (`idRedesSociales` ASC),
  CONSTRAINT `idUsuarioEncargadoOrg`
    FOREIGN KEY (`idOrganizacion`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPermisosEstandarOrg`
    FOREIGN KEY (`idPermisosEstandar`)
    REFERENCES `SpaceAdmind`.`Permisos` (`idPermisos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `IdRedesSociales`
    FOREIGN KEY (`idRedesSociales`)
    REFERENCES `SpaceAdmind`.`RedesSociales` (`idRedesSociales`)
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
-- Table `SpaceAdmind`.`Sede`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Sede` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Sede` (
  `idSede` VARCHAR(45) NOT NULL,
  `idOrg` VARCHAR(45) NOT NULL,
  `idDireccionSede` VARCHAR(45) NULL,
  `idUsuarioEncargado` VARCHAR(90) NOT NULL,
  `nombreSede` VARCHAR(45) NOT NULL,
  `numero_Bloques` INT NOT NULL,
  PRIMARY KEY (`idSede`, `idOrg`),
  INDEX `idOrg_idx` (`idOrg` ASC),
  INDEX `idDireccion_idx` (`idDireccionSede` ASC),
  INDEX `idEncargado_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idO`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idEc`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idD`
    FOREIGN KEY (`idDireccionSede`)
    REFERENCES `SpaceAdmind`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Bloque`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Bloque` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Bloque` (
  `idBloque` VARCHAR(45) NOT NULL,
  `idSede` VARCHAR(45) NOT NULL,
  `idOrg` VARCHAR(45) NOT NULL,
  `idUsuarioEncargado` VARCHAR(90) NOT NULL,
  `descripcionBloqe` VARCHAR(140) NULL,
  `numeroNiveles` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idBloque`, `idOrg`, `idSede`),
  INDEX `idOrg_idx` (`idOrg` ASC),
  INDEX `idSede_idx` (`idSede` ASC),
  INDEX `idUser_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idirBloqueFK`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeBloqueFK`
    FOREIGN KEY (`idSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idUserBloqueFK`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`espaciosPublicos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`espaciosPublicos` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`espaciosPublicos` (
  `idEspaciosPublcos` VARCHAR(45) NOT NULL,
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
  `idNivel` VARCHAR(45) NOT NULL,
  `idBloque` VARCHAR(45) NOT NULL,
  `idSede` VARCHAR(45) NOT NULL,
  `idOrg` VARCHAR(45) NOT NULL,
  `idUsuarioEncargado` VARCHAR(90) NOT NULL,
  `idEspacioPublico` VARCHAR(45) NOT NULL,
  `descripcionNivel` VARCHAR(140) NULL,
  `numeroEspacios` INT NOT NULL DEFAULT 0,
  `NumeroNivel` INT NULL,
  PRIMARY KEY (`idNivel`, `idBloque`, `idSede`, `idOrg`),
  INDEX `idBloque_idx` (`idBloque` ASC),
  INDEX `idSede_idx` (`idSede` ASC),
  INDEX `idOrg_idx` (`idOrg` ASC),
  INDEX `idEspaciosPublicos_idx` (`idEspacioPublico` ASC),
  INDEX `idUsuario_idx` (`idUsuarioEncargado` ASC),
  CONSTRAINT `idBloqueNivel`
    FOREIGN KEY (`idBloque`)
    REFERENCES `SpaceAdmind`.`Bloque` (`idBloque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeNivel`
    FOREIGN KEY (`idSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idOrgNivel`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idUsuarioNivel`
    FOREIGN KEY (`idUsuarioEncargado`)
    REFERENCES `SpaceAdmind`.`OrgUsuario` (`idOrgUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idEspaciosPublicosNivel`
    FOREIGN KEY (`idEspacioPublico`)
    REFERENCES `SpaceAdmind`.`espaciosPublicos` (`idEspaciosPublcos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SpaceAdmind`.`Espacio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `SpaceAdmind`.`Espacio` ;

CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`Espacio` (
  `idEspacio` VARCHAR(45) NOT NULL,
  `idNivel` VARCHAR(45) NOT NULL,
  `idBloque` VARCHAR(45) NOT NULL,
  `idSede` VARCHAR(45) NOT NULL,
  `idOrg` VARCHAR(45) NOT NULL,
  `idPermiso` VARCHAR(45) NOT NULL,
  `capacidadEspacio` INT NOT NULL,
  `descripcionEspaco` VARCHAR(140) NULL,
  INDEX `idNivel_idx` (`idNivel` ASC),
  INDEX `idBloque_idx` (`idBloque` ASC),
  INDEX `idSede_idx` (`idSede` ASC),
  INDEX `idOrg_idx` (`idOrg` ASC),
  INDEX `idPermiso_idx` (`idPermiso` ASC),
  PRIMARY KEY (`idEspacio`, `idNivel`, `idBloque`, `idSede`, `idOrg`),
  CONSTRAINT `idNivelspacio`
    FOREIGN KEY (`idNivel`)
    REFERENCES `SpaceAdmind`.`Nivel` (`idNivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idBloqueEspacio`
    FOREIGN KEY (`idBloque`)
    REFERENCES `SpaceAdmind`.`Bloque` (`idBloque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeEspacio`
    FOREIGN KEY (`idSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idOrgEspacio`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
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
  `idDiasHabiles` VARCHAR(140) NOT NULL,
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
  `idReserva` VARCHAR(45) NOT NULL,
  `idUsuario` VARCHAR(90) NOT NULL,
  `idDiasReserva` VARCHAR(45) NOT NULL,
  `fechaInicio` VARCHAR(45) NOT NULL,
  `fechaFin` VARCHAR(45) NOT NULL,
  `horaInicio` VARCHAR(45) NOT NULL,
  `horaFin` VARCHAR(45) NOT NULL,
  `idEspacio` VARCHAR(45) NULL,
  `idNivel` VARCHAR(45) NULL,
  `idBloque` VARCHAR(45) NULL,
  `idSede` VARCHAR(45) NULL,
  `idOrg` VARCHAR(45) NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `idDiasHabiles_idx` (`idDiasReserva` ASC),
  INDEX `idUsuario_idx` (`idUsuario` ASC),
  INDEX `idEspacioReserva_idx` (`idEspacio` ASC),
  INDEX `idNivelReserva_idx` (`idNivel` ASC),
  INDEX `idBloque_idx` (`idBloque` ASC),
  INDEX `idSedeReserva_idx` (`idSede` ASC),
  INDEX `idOrgReserva_idx` (`idOrg` ASC),
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
  CONSTRAINT `idEspacioReserva`
    FOREIGN KEY (`idEspacio`)
    REFERENCES `SpaceAdmind`.`Espacio` (`idEspacio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idNivelReserva`
    FOREIGN KEY (`idNivel`)
    REFERENCES `SpaceAdmind`.`Nivel` (`idNivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idBloqueReserva`
    FOREIGN KEY (`idBloque`)
    REFERENCES `SpaceAdmind`.`Bloque` (`idBloque`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeReserva`
    FOREIGN KEY (`idSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idOrgReserva`
    FOREIGN KEY (`idOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
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
  `ModSede` VARCHAR(45) NULL,
  `ModBloque` VARCHAR(45) NULL,
  `ModNivel` VARCHAR(45) NULL,
  `ModEspacio` VARCHAR(225) NULL,
  `ModUsuarioEnc` VARCHAR(45) NULL,
  PRIMARY KEY (`idModificacion`),
  INDEX `ModUsuarioEn_idx` (`ModUsuarioEnc` ASC),
  INDEX `ModOrg_idx` (`ModOrg` ASC),
  INDEX `ModSede_idx` (`ModSede` ASC),
  INDEX `ModBloque_idx` (`ModBloque` ASC),
  INDEX `ModNivel_idx` (`ModNivel` ASC),
  CONSTRAINT `ModUsuarioEn`
    FOREIGN KEY (`ModUsuarioEnc`)
    REFERENCES `SpaceAdmind`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ModOrg`
    FOREIGN KEY (`ModOrg`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
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
  `fechaMensaje` TIME NOT NULL,
  `TipoMensaje` VARCHAR(45) NOT NULL,
  `AsuntoMensaje` VARCHAR(45) NOT NULL,
  `DescripcionMensaje` VARCHAR(45) NOT NULL,
  `UsuarioAutor` VARCHAR(45) NOT NULL,
  `OrgId` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMensajes`),
  INDEX `OrgIdMensaje_idx` (`OrgId` ASC),
  INDEX `AutorUsuarioId_idx` (`UsuarioAutor` ASC),
  CONSTRAINT `OrgIdMensaje`
    FOREIGN KEY (`OrgId`)
    REFERENCES `SpaceAdmind`.`Organizacion` (`idOrganizacion`)
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
  `idHorarioSede` INT NOT NULL,
  `idDiasHabiles` VARCHAR(140) NOT NULL,
  `idSede` VARCHAR(45) NOT NULL,
  `HoraApertura` TIME NOT NULL,
  `HoraCierre` TIME NOT NULL,
  PRIMARY KEY (`idHorarioSede`, `idDiasHabiles`, `idSede`),
  INDEX `IdDiasHabilesSede_idx` (`idDiasHabiles` ASC),
  INDEX `idSedeHorario_idx` (`idSede` ASC),
  CONSTRAINT `IdDiasHabilesSede`
    FOREIGN KEY (`idDiasHabiles`)
    REFERENCES `SpaceAdmind`.`DiasHabiles` (`idDiasHabiles`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idSedeHorario`
    FOREIGN KEY (`idSede`)
    REFERENCES `SpaceAdmind`.`Sede` (`idSede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `SpaceAdmind` ;

-- -----------------------------------------------------
-- Placeholder table for view `SpaceAdmind`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SpaceAdmind`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `SpaceAdmind`.`view1`
-- -----------------------------------------------------
DROP VIEW IF EXISTS `SpaceAdmind`.`view1` ;
DROP TABLE IF EXISTS `SpaceAdmind`.`view1`;
USE `SpaceAdmind`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
