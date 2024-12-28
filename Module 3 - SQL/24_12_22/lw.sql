-- 1. use join- find all employees without branch
-- select * from Employee
-- left join Branch on Employee.branch_id = Branch.branch_id
-- where Employee.branch_id is NULL;

-- 1.5. use join- find all employees with and without branch
-- SELECT Employee.*
-- FROM Branch
-- RIGHT JOIN Employee ON Branch.branch_id = Employee.branch_id
-- ORDER by emp_id;

-- 2. use join- find all branches without employees
-- SELECT * from Employee
-- RIGHT JOIN Branch ON Employee.branch_id = Branch.branch_id
-- where Employee.branch_id is NULL;

-- 2.5. use join- find all branches without and without employees
-- SELECT Branch.branch_id, Branch.branch_name -- DISTINCT to show with no duplicates
-- FROM Branch
-- LEFT JOIN Employee on Branch.branch_id = Employee.branch_id;

-- 3. use join- find all employees and all branches
-- SELECT Branch.branch_id, Branch.branch_name, Employee.emp_id, Employee.first_name as employee_name
-- from Branch
-- FULL JOIN Employee on Branch.branch_id = Employee.branch_id;

-- 4. use join- show only  employees who have branches
-- select * from Employee
-- left join Branch on Employee.branch_id = Branch.branch_id
-- where Employee.branch_id is not NULL;

-- 5. use join - show all employees that dont have branch and branches that dont have employees
SELECT * FROM Employee
LEFT JOIN Branch ON Employee.branch_id = Branch.branch_id
where Branch.branch_id is NULL

UNION

SELECT * FROM Branch
LEFT join Employee on Employee.branch_id = Branch.branch_id
where Employee.emp_id is NULL;