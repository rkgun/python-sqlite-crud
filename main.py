import sys 
import os
import sqlite3 as sql

class Database:
	sql_db = sql_cursor = None
	def __init__(self):
		global sql_db, sql_cursor
		sql_db = sql.connect('contactlist.sqlite')
		sql_cursor = sql_db.cursor()
		table_exist=sql_cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="list"')
		if table_exist=='':		
			cursor.execute('CREATE TABLE "list" ( "id" INTEGER,"name" TEXT, "surname" TEXT, "tel" TEXT,"fb" TEXT, "twitter" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )')
	def __del__(self):
		sql_db.commit()

class People():
	name='John'
	surname='Doe'
	tel='999-999-99-99'
	mail='example@gmail.com'
	facebook='facebook.com/people/name'
	twitter='https://twitter.com/name'
	def __init__(self,name,surname,tel,mail,facebook,twitter):
		self.name=name
		self.surname=surname
		self.tel=tel
		self.mail=mail
		self.facebook=facebook
		self.twitter=twitter
	def data(self):
		dt='("{}","{}","{}","{}","{}","{}")'.format(self.name,self.surname,self.tel,self.facebook,self.twitter,self.mail)
		return dt

	def data_(self):
		dt="name='{}', surname='{}', tel='{}', fb='{}', twitter='{}', mail='{}'".format(self.name,self.surname,self.tel,self.facebook,self.twitter,self.mail)
		return dt


class Contact(Database,People):
	def list(self,mode='DESC'):
		sql = "SELECT * FROM list ORDER BY id {}".format(mode)
		try:
			sql_cursor.execute(sql)
			result = sql_cursor.fetchall()
		except Exception as e:
			return e
		return result

	def insert(self,p):
		sql='INSERT INTO list (name,surname,tel,fb,twitter,mail) VALUES'+' '+p.data()
		try:
			sql_cursor.execute(sql)
		except Exception as e:
			return e

	def insert_many(self,p):
		for x in p:
			self.insert(x)

	def delete(self, id):
		sql="DELETE FROM list WHERE id = {}".format(id)
		try:
			sql_cursor.execute(sql)
		except Exception as e:
			return e

	def update(self, id, p):
		sql = "UPDATE list SET "+ p.data_() +" WHERE id = {}".format(id)
		try:
			sql_cursor.execute(sql)
		except Exception as e:
			return e

if __name__ == "__main__":
	db = Database()
	ct = Contact()
	pp = People('john2','doe','999','mail','fb','tw')
	pp2 = People('john3','doe','999','mail','fb','tw')
	
	"""
	ct.insert(pp)
	ct.insert_many([pp,pp2])
	ct.list()
    ct.delete(id) id=>int
    ct.update(id,pp) id=>int"""

