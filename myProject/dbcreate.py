from dbconnect import connection

c, conn = connection()
c.execute("CREATE TABLE users (uid INT(10) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(15) UNIQUE, email VARCHAR(50), security_question VARCHAR(100), password VARCHAR(80), confirm_password VARCHAR(80))")
c.execute("CREATE TABLE quiz1 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz2 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz3 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz4 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Which is the first Doreamon film?\', \'Nobita''s Dorabian Nights\', \'Nobita''s Little Space War\', \'Nobita''s Dinosaur\', \'Nobita''s Great Adventure in South Seas\', \'Nobita''s Dinosaur\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Suneo has a cat. What is it called and is it male or female?\', \'Midori/Female\',\'Mii Chan/Female\', \'Ria Chan/Female\', \'Chiruchiru/Male\', \'Chiruchiru/Male\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Gian always picks on Nobita. Who helps him to do this?\', \'Doreamon', \'Suneo', \'Dekisugi', \'Sewashi', 'Suneo')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'What is Nobita''s special skill?\', \'His handwriting skills\', \'His sleeping skills and comic book knowledge\', \'His fighting skills\', \'His ability to run fast\', \'His sleeping skills and comic book knowledge\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'What is the name of Nobita''s mom?\', \'Tamao\', \'Nobi\', \'Tamaco\', \'Roboko\', \'Tamaco\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES (\'What is the vegetable that Shinchan hates to eat?\', \'Beans\', \'Garlic\', \'Capsicum\', \'Carrot\', \'Capsicum\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES (\'Whom does Shinchan''s teacher Yoshinaga marry?\', \'Suzuki\', \'Ishida Junichi\', \'Kazama\', \'Hiroshi\', \'Ishida Junichi\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Where does shinchan lives ?\', \'Tokyo\', \'Katsukabe\', \'Osaka\', \'Hiroshima\', \'Katsukabe\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Who is the teacher of the rose group?\', \'Yoshinaga\', \'Matsuzaka\', \'Midsi\', \'Nohara\', \'Yoshinaga\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Who has crush on Shinchan\', \'Nanako\', \'Nenechan\', \'Aichan\', \'Nohara\', \'Aichan\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Which of the following characters from ''Chota Bheem'' is not a good person and is sometimes troublesome?\', \'Bheem\', \'Kalia\', \'Raju\', \'Dholu\', \'Kalia\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Who is the daughter of Tuntun mausi?\', \'Indumati\', \'Chutki\', \'Rani\', \'Shivani\', \'Chutki\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'What was bheem''s favourite dish?\', \'Halwa\', \'Kheer\', \'Laddoo\', \'Jalebi\', \'Laddoo\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Who was the princess of Dholakpur?\', \'Indumati\', \'Chutki\', \'Rani\', \'Shivani\', \'Indumati\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Whose name is Jaggu?\', \'Donkey\', \'Bird\', \'Monkey\', \'Chimpamzee\', \'Monkey\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Where is Hattori from?\', \'Coga Valley\', \'Iga Valley\', \'Hiroshima\', \'Cagha Valley\', \'Iga Valley\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'What is Hattori's brother''s name?\', \'Shishimaru\', \'Kenechi\', \'Shinzo\', \'Aamara\', \'Shinzo\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Who is the female lead in the show?\', \'Umiko\', \'Sonam\', \'Suzuka\', \'Mitchiko\', \'Umiko\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Who is Kenechi''s teacher's love interest?\', \'Umiko'' Mom\', \'Kenechi''s Mom\', \'Haiko Madam\', \'Jaiko Madam\', \'Haiko Madam\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'What colours are Hattori''clothes\', \'Blue with a yellow belt ans red sleeves'\', \'Green with a red belt and yellow sleves\', \'Red with a yellow belt and white sleeves\', \'Blue with a red belt and yellow sleeves\', \'Blue with a red belt and yellow sleeves\')")













