### Database
- A database is an organized collection of structured information or data stored and accessed electronically. 
- It is designed to efficiently store, manage, and retrieve data for various purposes.

### Relational Database
- A relational database is a type of database that organizes data into tables with predefined relationships between them. 
It uses a relational model to represent data and supports the manipulation and querying of data using a language called Structured Query Language (SQL).

### SQL

- SQL stands for Structured Query Language. It is a programming language used to communicate with and manipulate relational databases.
 SQL allows users to create, retrieve, update, and delete data in a database, as well as define and manage the database structure.

- MySQL is a popular open-source relational database management system (RDBMS) based on the SQL language. It is widely used for building web applications and powering dynamic websites. MySQL is known for its scalability, reliability, and ease of use.

To create a database in MySQL, you can follow these general steps:

* **Install MySQL**: Download and install MySQL server on your computer or use an existing installation.

* **Start MySQL Server**: Start the MySQL server service or daemon.

* **Access MySQL**: Use a MySQL client application such as the MySQL command-line tool or a graphical interface like phpMyAdmin to connect to the MySQL server.

* **Create a Database**: Once connected, you can execute SQL commands to create a database. For example, to create a database named "mydatabase," you can use the following command:

```
CREATE DATABASE mydatabase;
```

This command creates a new database named "mydatabase."

* **Verify Database Creation**: You can check if the database is created successfully by listing the available databases. You can use the following command:

```
SHOW DATABASES;
```

This command will display a list of databases, including the one you created.


## DDL
- Stands for Data Definition Language
- DDL is a subset of SQL that deals with defining and modifying the structure of a database schema. 
It includes commands such as **CREATE**, **ALTER**, and **DROP**, which are used to create, modify, and delete database objects like tables, views, indexes, and constraints.


## DML
- Stands for Data Manipulation Language

- DML focuses on manipulating the data within the database. 
It includes commands such as **SELECT**, **INSERT**, **UPDATE**, and **DELETE**, which are used to retrieve, insert, update, and delete data from database tables.

### Install MySQL on Ubuntu
```
$ sudo apt install mysql-server
```

```
$ mysql --version
```
- checks version of MySQL


### Connect to your MySQL server
```
$ sudo mysql
```
