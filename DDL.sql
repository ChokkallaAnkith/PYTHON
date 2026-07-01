-- 1.  Create employee table with 2 columns(emp_name,location) 
create table employee (emp_name char(30),location varchar(20));

--  add column at last address of employee(add_emp) 
alter table employee add column add_emp char(30) ;

--  add column at first emp_id. 
alter table employee add column emp_id int first;

--  add column at specific position email(25) 
alter table employee add column email varchar(10) after emp_id;

--  modify empName char to varchar. 
alter table employee modify empName varchar(20);

--  add sid and department at a time. 
alter table employee add column sid int,add column department varchar(20);

-- rename emp_name to employeeName. 
alter table employee rename column emp_Name to employeeName ;

-- drop sid column 
alter table employee drop column sid;