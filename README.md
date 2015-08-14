# postcard
Gmail basics
==============

1. Create the database named postcard:
	`create database postcard character set utf8;`
2. Add a user
	`create user 'postcard'@'localhost' identified by 'postcard';`
3. Set Permissions
	`grant all on postcard.* to 'postcard'@'localhost';`