# asura22nov.pythonanywhere.com

Testing simple web app in pythonanywhere.com 

Tried both in ubuntu 16 && pythonanywhere.com environment

####################################################

Credits & Reading Reference:

https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
https://codehandbook.org/python-flask-jquery-ajax-post/
https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
https://flask-mysql.readthedocs.io/en/latest/

#####################################################

Requirements:

1. Account in pythonanywhere.com (its's free)
2. Creating python+Flask+Mysql App inside pythonanywhere.com
3. get familiar with  Dashboard / Consoles / Files /   Web /  Tasks /  Databases
4. Open your Bash console and start creating the project files
5. once done open your database console and start writing the sql procedure
6. Tech's : python-flash / mysql / ngnix / gunicorn / jquery / html / css

#####################################################
Bash - python - requirements

touch flask_app.py
mkdir templates
mkdir static
pip install flask
pip install mysql-connector
pip install jquery 
#if you get error with above command try below the following
sudo apt install npm
npm install -g jquery
pip install flask-mysql
pip install gunicorn
sudo apt-get install python-pip python-dev libmysqlclient-dev
sudo apt-get install python-mysql.connector

##########################################################
Database SQL PROCEDURE


CREATE TABLE BucketList.tbl_user(
user_id BIGINT NOT NULL AUTO_INCREMENT,
user_name VARCHAR(255) NULL,
user_email VARCHAR(255) NULL,
user_password VARCHAR(255) NULL,
PRIMARY KEY (user_id));

##if your are getting any error try the following
GRANT ALL ON BucketList.* TO 'username'@'localhost';

GRANT ALL ON BucketList.* TO 'username'@'%'

###PROCEDURE

DELIMITER $$
CREATE DEFINER=`username`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    if ( select exists (select 1 from BucketList.tbl_user where user_name = p_name) ) THEN
        select 'Username Exists !!';    
    ELSE
             insert into tbl_user
        (
            user_name,
            user_email,
            user_password
        )
        values
        (
            p_name,
            p_email,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;

#checking the PROCEDURE
SHOW PROCEDURE STATUS WHERE db = 'BucketList';
SHOW CREATE PROCEDURE sp_createUser;
DROP PROCEDURE sp_createUser;

##########################################################
