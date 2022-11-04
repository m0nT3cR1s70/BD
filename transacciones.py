import psycopg2 as bd

conexion = bd.connect(
	user       = 'm0nT3cR1s70',
	password   = 'administrator',
	host       = 'localhost',
	port       = 5432,
	database   = 'Test'
	)

try:
	conexion.autocommit = True
	cursor    = conexion.cursor()
	sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
	valores   = ('Mario','Nieto','mnieto@mail.com')
	cursor.execute(sentencia,valores)
	#conexion.commit()
except Exception as e:
	conexion.rollback()
	print(f'Error: {e}')
finally:
	conexion.close()