/*Creando la Base de datos*/
Create schema bdcargamos;
use bdcargamos;
/*Creando las Tablas */
/*Una clave Primaria es un campo cuyos valores identifican de forma
unica cada registro dentro de la tabla.este campo tiene la clausula
primary key */
create table grupos(
codgrupo varchar(3) primary key,
nombre_grupo varchar(50),
estado bool);
/*recuperar la informacion de la tabla */
select * from grupos;
/*insertar registros a la tabla */
insert into grupos(codgrupo,nombre_grupo,estado)
values('G1','ECO INDUSTRIA',True);

insert into grupos(codgrupo,nombre_grupo,estado)
values('G2','ATRAYENDO TALENTO',True);

insert into grupos(codgrupo,nombre_grupo,estado)
values('G3','TECHINNOVATION',True);

insert into grupos(codgrupo,nombre_grupo,estado)
values('G4','YOURLIFEWITHUS',True);

insert into grupos(codgrupo,nombre_grupo,estado)
values('G5','SINGRUPO',True);

/*Eliminar Registros*/
delete from grupos where codgrupo='G2';

/*Actualizar Registros */
update grupos set estado=False where codgrupo='G5';


create table alumnos
(codalu varchar(3) primary key,
nombre_alumno varchar(100),
apellido_alumno varchar(100),
edad_alumno int,
fechanac_alumno datetime,
ciudad varchar(100),
estado bool);

select * from alumnos;

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA1','Armando','Ruiz',42,'1975/01/19','Lima',True)

 

