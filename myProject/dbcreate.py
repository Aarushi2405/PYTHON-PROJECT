from dbconnect import connection

c, conn = connection()
c.execute("CREATE TABLE users (uid INT(10) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(15) UNIQUE, email VARCHAR(50), security_question VARCHAR(100), password VARCHAR(80), confirm_password VARCHAR(80))")
c.execute("CREATE TABLE quiz1 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz2 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz3 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz4 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
