--- SQL Part Begins here

-- SELECT count(*) from hr.EMPLOYEES;
-- select * from hr.EMPLOYEES where DEPARTMENT_ID in(10, 20) and salary > 3000;
-- select * from hr.EMPLOYEES where salary > 5000 order by salary asc;
-- select DEPARTMENT_ID, COUNT(DEPARTMENT_ID) as totals, sum(salary) from hr.EMPLOYEES group by DEPARTMENT_ID;
-- select FIRST_NAME,reverse(FIRST_NAME), LAST_NAME, to_char(HIRE_DATE, 'dd/mon/yyyy') from hr.EMPLOYEES where to_char(HIRE_DATE, 'yyyy') = '2018';
-- select FIRST_NAME, FIRST_NAME||' '||LAST_NAME as fullname, salary, SALARY*12 as annually from hr.EMPLOYEES;

select * from hr.EMPLOYEES where SALARY < 2500;

-- my sql pracs
--SELECT first_name, reverse(first_name) FROM Customers;
select * from Customers;

--insert into Customers values (6,'Jane','Doe',24,'USA'), (7,'Kevin','Roy',27,'UAE');
--select * from Customers where country = 'USA' or last_name = 'Doe';
--insert into Customers values (7,'Kevin','Roy',27,'UAE');
--select ascii('A') from dual; -- 65
--select ascii('a') from dual; --97

select * from Customers;
--SELECT first_name, age, reverse(first_name) as revi, age*2 as twiceAge, lower(country), upper(country) FROM Customers;
--insert into Customers values (6, 'Mike', 'Tyson', 29, 'NZ'), (7, 'Piano', 'Khalid', 30, 'UAE'), (8, 'Ginger', 'Cruise', 23, 'UK'), (9, 'Billie', 'Swift', 24, 'NZ');
--select * from Customers where age >= 30 and country = 'USA';
--select * from Customers where age >= 30 or country = 'USA';
--select * from Customers where first_name like 'J%' and country = 'UK';
--select * from Customers where first_name like 'J%' or country = 'UK';
--select * from Customers where age in(23, 26, 29);
--select * from Customers where age between 23 and 29; -- order by age;
--select * from Customers where age >= 23 and age <= 29;
--update Customers set first_name = 'Pioneer' where customer_id=7;
--alter table Customers rename customer_id to cust_id;
--update Customers set first_name = 'Peony' where cust_id = 7;

  SELECT * FROM Customers;
--update Customers set first_name = 'Anarthick' where first_name = 'Johnny';

--alter table Customers add column occupation varchar(50);
--update Customers set occupation = 'Engineer';
--update Customers set occupation = 'Actor' where first_name = 'Anarthick';
--update Customers set occupation = 'Doctor' where customer_id = 5;
--alter table Customers rename customer_id to c_id;
--insert into Customers values(6, 'Georgey', 'Tom', 27, 'UAE', 'Student');
--alter table Customers drop column country;
delete from Customers where first_name = 'Tom';
--SELECT max(age), country FROM Customers group by country;
--SELECT max(age), country FROM Customers group by country order by age;
--SELECT * FROM Customers where age = (SELECT max(age) FROM Customers);
--SELECT last_name FROM Customers where last_name like 'R%';
--SELECT * FROM Customers where last_name like (SELECT last_name FROM Customers where last_name like 'R%');
SELECT * FROM Customers WHERE last_name LIKE 'R%';
--  SELECT * FROM Customers c right join Orders o on c.customer_id = o.customer_id;
SELECT * FROM Customers c left join Orders o on c.customer_id = o.customer_id;
--SELECT * FROM Customers where first_name like 'J%' or age = 22;
--SELECT * FROM Customers where first_name like 'J%' and age = 22;
SELECT * FROM Customers where first_name like 'J%' and age < 30;
--select * from Orders where amount > 500;
select * from Orders where amount < 500;
select * from Shippings where status like 'D%';
select * from Shippings where status not like 'D%';
select * from Shippings where customer = shipping_id;
select * from Shippings where customer = shipping_id*2;
select * from Orders where item like 'M%';
select * from Orders where lower(item) like 'm%';
select * from Orders where upper(item) like 'M%';
select max(customer) from Shippings;
select * from Orders where amount = (select max(amount) from Orders);
--SELECT max(age), country FROM Customers group by country;
select max(amount),item from Orders group by item;
--insert into Orders values(6, 'Mousepad', 400, 5);

--create table hello(
  -- a int, b int );

-- insert into hello values (1,2), (3,4),(5,6);
--insert into hello values (7,8);
 --begin;  rollback;
-- select * from hello;
--savepoint;
-- insert into hello values(9,10),(11,12);
--rollback;
--alter table hello create column c varchar(20); -- Error: near "create": syntax error
--alter table hello add column c varchar(20);
--update  hello set c='Hey';
--update hello set c = 'Salaam' where b = '%2';
update hello set c = 'Salon' where b = 2;

-- select * from hr.employees;
-- select * from hr.employees where salary > 15000;
SELECT department_name from HR.DEPARTMENTS;
SELECT JOB_TITLE from HR.JOBS;
SELECT FIRST_NAME, LAST_NAME, HIRE_DATE from HR.EMPLOYEES;
SELECT EMPLOYEE_ID, PHONE_NUMBER,HIRE_DATE,SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID from HR.EMPLOYEES;
SELECT EMPLOYEE_ID, DEPARTMENT_ID from HR.EMPLOYEES;
SELECT * from HR.EMPLOYEES where MANAGER_ID is NULL;
SELECT JOB_ID FROM HR.EMPLOYEES group by JOB_ID;
SELECT EMPLOYEE_ID, FIRST_NAME, EMAIL FROM HR.EMPLOYEES;

--SELECT * FROM Customers where age < (SELECT max(age) FROM Customers);
--SELECT max(age) FROM Customers where age < (SELECT max(age) FROM Customers);
--SELECT * FROM Customers where age < (SELECT max(age) FROM Customers)  order by age limit 1;
--SELECT * FROM Customers where age < (SELECT max(age) FROM Customers) order by age;
--SELECT * FROM Employees WHERE Salary = (SELECT MAX(Salary) FROM Employees WHERE Salary < (SELECT MAX(Salary) FROM Employees) );
--select * from Customers where age = ( SELECT max(age) FROM Customers where age < (SELECT max(age) FROM Customers) );

// update user set names = "hey there" and salaar=35000 where id=123;
// my sql update query
//  ctrl + K ==> clear in mongo shell

// some SQL from leetcodes 

# Write your MySQL query statement below
https://leetcode.com/problems/combine-two-tables/
-- select p.firstName, p.lastName, a.city, a.state from Person p inner join Address a where p.personId = a.addressId;
-- select p.firstName, p.lastName, a.city, a.state from Person p left join Address a where p.personId = a.addressId;
-- select p.firstName, p.lastName, a.city, a.state from Person p left join Address a on p.personId = a.addressId;
select p.firstName, p.lastName, a.city, a.state from Person p left join Address a on p.personId = a.personId;

https://leetcode.com/problems/second-highest-salary/
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee);
-- select max(salary) from Employee;

https://leetcode.com/problems/rank-scores/
select score, dense_rank() over (order by score desc) as "rank" from Scores;

https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- select max(salary) from Employee where managerId is not null;
-- select * from Employee where managerId is not null and salary > (select min(salary) from Employee);
-- select * from Employee e1 inner join Employee e2 on e1.id = e2.managerId;
-- select * from Employee e1 inner join Employee e2 on e1.id = e2.managerId where e1.salary < e2.salary;
-- select e1.name as Employee from Employee e1 inner join Employee e2 on e1.id = e2.managerId where e1.salary < e2.salary;
select e2.name as Employee from Employee e1 inner join Employee e2 on e1.id = e2.managerId where e1.salary < e2.salary;

https://leetcode.com/problems/department-highest-salary/description/

https://leetcode.com/problems/nth-highest-salary/description/
-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--       # Write your MySQL query statement below.
-- select max(salary), id from Employee
-- --  where salary
--   );
-- END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END

https://leetcode.com/problems/customers-who-never-order/
-- # Write your MySQL query statement below  customerId
-- select * from Customers c inner join Orders o where c.id = o.id;
-- select * from Customers c inner join Orders o where c.id = o.customerId;
select c.name as Customers from Customers c left join Orders o on c.id = o.customerId where o.customerId is null;

