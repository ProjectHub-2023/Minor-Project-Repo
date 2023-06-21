-- SQLite
-- create table Employee_Info(Employee_ID INTEGER PRIMARY KEY ,Employee_Name varchar(10),Employee_Age int(2),Employee_Gender varchar(6),Employee_Field varchar(10),username varchar(10),Access_Key varchar(10));
-- create view Operator_Info as select Employee_ID ,Employee_Name as Operator_Name,Employee_Age as Operator_Age,Employee_Gender as Operator_Gender,username as Operator_Login,Access_Key as Operator_Key,Employee_Field From Employee_Info where Employee_Field = "Operator" OR Employee_Field = "Manager" ;
-- create table Operation_log (Serial_No int(6) PRIMARY KEY,Employee_ID varchar(10),Current_status varchar(10),Product_ID varchar(10),time_stamp Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);

-- DROP Table Employee_Info;
-- DROP View Operator_Info;
-- DROP Table Operation_log;

-- DElete FROM Employee_Info;

-- insert into Employee_Info(Employee_ID,Employee_Name,Employee_Age,Employee_Gender,Employee_Field,username,Access_Key) VALUES(10001,"Nakul","21","Male","Manager","nakul","1234");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,username,Access_Key) VALUES("Pavan","21","Male","Operator","pavan","1234");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,username,Access_Key) VALUES("Patanjali","22","Male","Operator","patanjali","1234");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,username,Access_Key) VALUES("Shrinivas","21","Male","Operator","shrinivas","1234");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,username,Access_Key) VALUES("Sunil","21","Male","Operator","sunil","1234");

select *from Employee_Info;
select *from Operator_Info;
select *from Operation_log;