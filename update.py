import psycopg2

conexion = psycopg2.connect(
	user      = 'm0nT3cR1s70',
	password  = 'administrator',
	host      = 'localhost',
	port      = 5432,
    database  = 'Test'
	)

try:
	with conexion:
		with conexion.cursor() as cursor:
			sentencia = 'UPDATE persona SET nombre = %s WHERE id_persona=6'
			values    = ('Yiz',)
			cursor.execute(sentencia,values)
except Exception as e:
	print(f'Error: {e}')
finally:
	conexion.close()