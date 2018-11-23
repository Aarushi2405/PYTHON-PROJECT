from dbconnect import connection

c, conn = connection()
c.execute("CREATE TABLE users (uid INT(10) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), username VARCHAR(15) UNIQUE, email VARCHAR(50), security_question VARCHAR(100), age INTEGER(2), password VARCHAR(80), confirm_password VARCHAR(80))")
c.execute("CREATE TABLE quiz1 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(200), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz2 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(200), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz3 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(200), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("CREATE TABLE quiz4 (uid INT(10) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(200), option1 VARCHAR(50), option2 VARCHAR(50),  option3 VARCHAR(50), option4 VARCHAR(50), answer VARCHAR(50))")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Which of these, was the first Doreamon film?\', \'Nobita\'\'s Dorabian Nights\', \'Nobita\'\'s Little Space War\', \'Nobita\'\'s Dinosaur\', \'Nobita\'\'s Great Adventure in the South Seas\', \'Nobita\'\'s Dinosaur\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Suneo has a cat, what is it called and is it a male or a female cat?\', \'Midori, Female\',\'Mii Chan, Female\', \'Ria Chan, Female\', \'Chiruchiru, Male\', \'Chiruchiru, Male\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'Gian always picks on Nobita, who helps him with this?\', \'Doreamon', \'Suneo', \'Dekisugi', \'Sewashi', 'Suneo')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'What is Nobita\'\'s special skill?\', \'His handwriting skills\', \'His sleeping skills and comic book knowledge\', \'His fighting skills\', \'His ability to run fast\', \'His sleeping skills and comic book knowledge\')")
c.execute("INSERT INTO quiz1 (question, option1, option2, option3, option4, answer) VALUES (\'What is Nobita\'\'s mom\'\'s name?\', \'Tamao\', \'Nobi\', \'Tamaco\', \'Roboko\', \'Tamaco\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES (\'Which is the vegetable Shinchan hates eating?\', \'Beans\', \'Garlic\', \'Capsicum\', \'Carrot\', \'Capsicum\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES (\'Whom does Shinchan\'\'s teacher Yoshinaga marry?\', \'Suzuki\', \'Ishida Junichi\', \'Kazama\', \'Hiroshi\', \'Ishida Junichi\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Where does Shinchan live?\', \'Tokyo\', \'Kasukabe\', \'Osaka\', \'Hiroshima\', \'Kasukabe\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Who is Rose group\'\'s teacher?\', \'Yoshinaga\', \'Matsuzaka\', \'Midsi\', \'Nohara\', \'Matsuzaka\')")
c.execute("INSERT INTO quiz2 (question, option1, option2, option3, option4, answer) VALUES(\'Who has a crush on Shinchan?\', \'Nanako\', \'Nenechan\', \'Aichan\', \'Nohara\', \'Aichan\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Which of the following characters from \'\'Chhota Bheem\'\' is not a good person and is sometimes troublesome?\', \'Bheem\', \'Kalia\', \'Raju\', \'Dholu\', \'Kalia\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Who is Tuntun mausi\'\'s daughter?\', \'Indumati\', \'Chutki\', \'Rani\', \'Shivani\', \'Chutki\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'What was Bheem\'\'s favorite dish?\', \'Halwa\', \'Kheer\', \'Laddoo\', \'Jalebi\', \'Laddoo\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Who was the princess of Dholakpur?\', \'Indumati\', \'Chutki\', \'Rani\', \'Shivani\', \'Indumati\')")
c.execute("INSERT INTO quiz3 (question, option1, option2, option3, option4, answer) VALUES(\'Which species is Jaggu?\', \'Donkey\', \'Bird\', \'Monkey\', \'Chimpamzee\', \'Monkey\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Where is Hattori from?\', \'Coga Valley\', \'Iga Valley\', \'Hiroshima\', \'Cagha Valley\', \'Iga Valley\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'What is Hattori\'\'s brother\'\'s name?\', \'Shishimaru\', \'Kenechi\', \'Shinzo\', \'Aamara\', \'Shinzo\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Who is the female lead in the show?\', \'Yumiko\', \'Sonam\', \'Suzuka\', \'Mitchiko\', \'Yumiko\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'Who is Kenechi\'\'s teacher\'\'s love interest?\', \'Yumiko\'\' Mom\', \'Kenechi\'\'s Mom\', \'Haiko Madam\', \'Jaiko Madam\', \'Haiko Madam\')")
c.execute("INSERT INTO quiz4 (question, option1, option2, option3, option4, answer) VALUES(\'What colours are Hattori\'\'clothes?\', \'Blue with a yellow belt and red sleeves\', \'Green with a red belt and yellow sleeves\', \'Red with a yellow belt and white sleeves\', \'Blue with a red belt and yellow sleeves\', \'Blue with a red belt and yellow sleeves\')")
conn.commit()












