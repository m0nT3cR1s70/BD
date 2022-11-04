import psycopg2

conexion = psycopg2.connect(
	user     = 'm0nT3cR1s70',
	password = 'administrator',
	host     = 'localhost',
	port     = 5432,
	database = 'Test'
	)

try:
	with conexion:
		with conexion.cursor() as cursor:
			sentencia = 'SELECT id_persona,nombre,apellido FROM persona ORDER BY id_persona'
			cursor.execute(sentencia)
			registros = cursor.fetchall()
			print(registros)
except Exception as e:
	print(f'Error: {e}')
finally:
	conexion.close()