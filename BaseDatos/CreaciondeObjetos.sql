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
/*recuperar la informacion de la tabla 
select * from grupos */
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

/*Eliminar Registros
delete from grupos where codgrupo='G2'; */

/*Actualizar Registros 
update grupos set estado=False where codgrupo='G5'; */

create table alumnos
(codalu varchar(3) primary key,
nombre_alumno varchar(100),
apellido_alumno varchar(100),
edad_alumno int,
fechanac_alumno datetime,
ciudad varchar(100),
estado bool);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA1','Armando','Ruiz',42,'1975/01/19','Lima',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA2','Gilberto','Vicente',42,'1975/01/19','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA3','Rumina','De Leon',23,'1998/09/05','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA4','Favio','Raquec',29,'1992/03/24','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA5','Diego','Santizo',21,'2000/06/11','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA6','Alicia','Guerrero',28,'1994/05/12','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA7','Javier','Catalan',26,'1995/03/08','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA8','Lourdes','Catalán',25,'1997/02/22','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('CA9','Ana Gabriela','Pestaña','25','1996/05/07','Mexico', True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('C10','Fernanda','Tlapa',33,'1988/05/21','Mexico',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('C11','Nicolle','Santizo',17,'2004/09/27','Guatemala',True);

insert into alumnos(codalu,nombre_alumno,apellido_alumno,edad_alumno,
fechanac_alumno,ciudad,estado)
values('C12','ingrid','guerrero',25,'1996/02/9','guatemala',True);

/*Alter Table me permite modificar la estructura de la tabla */
Alter Table alumnos 
add codgrupo varchar(3);


/*Eliminar la Base de datos 
drop database bdcargamos; */

/*Clave Foranea es un campo dentro de la tabla cuyos valores hacen referencia
a claves primarias en otra tabla 
uno - muchos
uno -uno
muchos - muchos
*/

ALTER TABLE alumnos add constraint fk_grupo foreign key(codgrupo)
references grupos(codgrupo)













 

