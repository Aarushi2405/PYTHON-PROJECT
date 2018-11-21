from dbconnect import connection

c, conn = connection()
c.execute("CREATE TABLE users (uid INT(10) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(15) UNIQUE, email VARCHAR(50), security_question VARCHAR(100), password VARCHAR(80), confirm_password VARCHAR(80))")