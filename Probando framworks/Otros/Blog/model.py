import MySQLdb, datetime


DB_HOST = '127.0.0.1' 
DB_USER = 'adminMySpace' 
DB_PASS = 'asd123' 
DB_NAME = 'mydb'




def get_posts():
	datos = [DB_HOST,DB_USER, DB_PASS, DB_NAME] 
	conn = MySQLdb.connect(*datos)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM entries")
	
	wait = cursor.fetchall()
	
	cursor.close()                 # Cerrar el cursor 
	conn.close()  
	
	return wait


def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text)
