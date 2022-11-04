import psycopg2 


conexion = psycopg2.connect(
	user     = 'm0nT3cR1s70',
	password = 'administrator',
	host     = 'localhost',
	port     = 5432,
	database = 'Test'
	)

cursor    = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()