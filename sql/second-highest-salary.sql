# Write your MySQL query statement below
/*
select t2.Salary as SecondHighestSalary from 
(select distinct Salary as top2 from Employee
order by Salary desc 
limit 2) t2
join (select distinct Salary as top1 from Employee
order by Salary desc 
limit 1) t1
on t1.Salary <> t2.Salary
;
*/
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1

/*
176. Second Highest Salary
Easy

595

316

Favorite

Share
SQL Schema
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/
