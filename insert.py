import psycopg2

conexion = psycopg2.connect(
	user      = 'm0nT3cR1s70',
	password  = 'administrator',
	host      = 'localhost',
	port      =  5432,
	database  = 'Test')


try:
	with conexion:
		with conexion.cursor() as cursor:
			sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
			valores   = ('Luffy','Monkey D', 'onepiece@mail.com')
			cursor.execute(sentencia,valores)
			# conexion.commit()
			registros_insertados = cursor.rowcount
			print(registros_insertados)
except Exception as e:
	print(f'Error: {e}')
finally:
	conexion.close()
