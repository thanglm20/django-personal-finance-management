


create table tbl_students(
id_std varchar(255) not null,
name_std varchar(255),	
sex varchar(20),
class_id varchar(255),	
hometown varchar(255),
birthday date,
primary key(id_std)
)


INSERT INTO tbl_students (id_std, name_std, sex, class_id, hometown, birthday)
VALUES ('123', 'John', 'Male', 'TDH', 'Hanoi, Viet Nam', '1997-04-30');


INSERT INTO tbl_students (id_std, name_std, sex, class_id, hometown, birthday)
VALUES ('132', 'Alice', 'Female', 'CNTT', 'Hanoi, Viet Nam', '1997-03-15');



INSERT INTO tbl_students (id_std, name_std, sex, class_id, hometown, birthday)
VALUES ('321', 'Bob', 'Male', 'CNTT', 'Hanoi, Viet Nam', '1997-03-27');

select  * from tbl_students;


CREATE VIEW view_students AS
SELECT * from tbl_students;


REFRESH MATERIALIZED VIEW CONCURRENTLY view_students;


select * from view_students;
        
