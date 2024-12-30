--15
SELECT Employees.name, Departments.department_id, Departments.name, Departments.building from Employees
inner join Departments on Employees.department_id = Departments.department_id;

--16
SELECT Employees.employee_id, Employees.name, Departments.department_id, Departments.name, Departments.building from Employees
left join Departments on Employees.department_id = Departments.department_id;

--17
SELECT Employees.employee_id, Employees.name, Departments.department_id, Departments.name, Departments.building from Employees
left join Departments on Employees.department_id = Departments.department_id
where Employees.department_id is NULL;

--18
SELECT Departments.name, count(*) as employee_count from Employees
join Departments on Employees.department_id = Departments.department_id
group by Departments.name;

--19
SELECT Departments.name, avg(salary) as avg_salary from Employees
join Departments on Employees.department_id = Departments.department_id
group by Departments.name;

--20
SELECT Employees.name, max(salary), Departments.name from Employees
inner join Departments ON Employees.department_id = Departments.department_id
group by Departments.name, Employees.name
having Employees.salary = (SELECT max(salary) from Employees as max_salary where max_salary.department_id = Employees.department_id);

--21
SELECT Employees.name, Employees.seniority, Departments.department_id, Departments.name, Departments.building from Employees
inner join Departments on Employees.department_id = Departments.department_id
order by Employees.seniority;

--22
SELECT Employees.seniority, avg(Employees.salary) as avg_salary from Employees
group by seniority;

--23
--alef
ALTER TABLE Departments
add employees_num INT;

ALTER TABLE Departments
add avg_salary decimal(10, 2);

ALTER TABLE Departments
add max_salary decimal(10, 2);

ALTER TABLE Departments
add avg_seniority decimal(5, 2);

--bet
UPDATE Departments
set employees_num = (SELECT COUNT(*) from Employees where Employees.department_id = Departments.department_id),
avg_salary = (SELECT avg(salary) from Employees where Employees.department_id = Departments.department_id),
max_salary = (SELECT max(salary) from Employees where Employees.department_id = Departments.department_id),
avg_seniority = (SELECT avg(seniority) from Employees where Employees.department_id = Departments.department_id);
