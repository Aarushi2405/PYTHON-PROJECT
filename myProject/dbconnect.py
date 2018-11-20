import MySQLdb

def connection() :
	conn = MySQLdb.connect(host = "localhost", user="root", passwd="A@rushi2405", db = "registration")
	c = conn.cursor()
	return c, conn

