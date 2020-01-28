CREATE TABLE users(
    id serial primary key,
    username varchar(50) UNIQUE,
    email varchar(50) UNIQUE,
    password varchar(50)
);