-- SQL-команды для создания таблиц

CREATE TABLE employees (
   employee_id serial PRIMARY KEY,
   first_name varchar(50),
   last_name varchar(50),
   title varchar(50),
   birth_date date,
   notes text
);


CREATE TABLE customers (
    customer_id varchar(100) UNIQUE,
    company_name varchar(100),
    contact_name varchar(100)
);


CREATE TABLE orders (
  order_id int,
  customer_id varchar(100) REFERENCES customers (customer_id),
  employee_id int REFERENCES employees (employee_id),
  order_date date,
  ship_city VARCHAR(100)
)



