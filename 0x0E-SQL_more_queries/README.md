### PRIMARY KEY 
Is a column or a set of columns in a database table that uniquely identifies each row in the table. 
It ensures that the values in the specified column(s) are unique and not null, which means no two rows can have the same primary key value. The primary key plays a crucial role in maintaining data integrity and facilitating efficient data retrieval.

For example, in a "users" table, you might have an "id" column as the primary key:
```
CREATE TABLE users (
   id INT PRIMARY KEY,
   name VARCHAR(50),
   email VARCHAR(100)
);
```
* In this case, the "id" column serves as the primary key, ensuring that each row has a unique "id" value.


### FOREIGN KEY 
Is a column or a set of columns in a database table that establishes a link between data in two related tables. 
It creates a relationship between the tables, enforcing referential integrity. The foreign key in one table refers to the primary key in another table, creating a link between the two.

For example, consider two tables, "orders" and "customers." The "customer_id" column in the "orders" table might be a foreign key that refers to the "id" column in the "customers" table. This establishes a relationship between orders and customers, ensuring that each order is associated with a valid customer:
```
CREATE TABLE customers (
   id INT PRIMARY KEY,
   name VARCHAR(50),
   email VARCHAR(100)
);

CREATE TABLE orders (
   order_id INT PRIMARY KEY,
   order_date DATE,
   customer_id INT,
   FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

## CONSTRAINTS
### NOT NULL Contraint
The NOT NULL constraint ensures that a column cannot have a NULL value, meaning it must contain a valid value. 
To apply the NOT NULL constraint to a column, include it during table creation or alter the table using the ALTER TABLE statement.
```
CREATE TABLE employees (
  emp_id INT NOT NULL,
  emp_name VARCHAR(50) NOT NULL,
  ...
);
```


### UNIQUE Constraint: 
The UNIQUE constraint ensures that each value in the specified column(s) is unique across all rows in the table. 
It allows a column to have unique values but still allows NULL values.
```
CREATE TABLE students (
  student_id INT UNIQUE,
  student_name VARCHAR(50),
  ...
);
```


### JOIN Statements
To retrieve data from multiple tables in a single query, you can use JOIN statements. 
A JOIN allows you to combine rows from two or more tables based on a related column between them. 
The most common types of JOINs are:
* INNER JOIN, 
* LEFT JOIN (or LEFT OUTER JOIN), 
* RIGHT JOIN (or RIGHT OUTER JOIN), and 
* FULL JOIN (or FULL OUTER JOIN).

Example of INNER JOIN
```
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
```


### UNION
UNION is used to combine the results of two or more SELECT queries into a single result set. The SELECT queries must have the same number of columns with compatible data types.

Example using UNION:
```
SELECT emp_name, 'Employee' AS type FROM employees
UNION
SELECT cust_name, 'Customer' AS type FROM customers;
```

In this example, we are combining the employee names from the "employees" table with the customer names from the "customers" table into a single result set with an additional column indicating the type of entity (Employee or Customer).
