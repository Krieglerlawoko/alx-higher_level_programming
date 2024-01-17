-- database hbtn_0d_2 and the user user_0d_2 created
-- database created
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- user created
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- privileges select granted to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
