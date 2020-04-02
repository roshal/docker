
import psycopg2 as p__psycopg2

connection = p__psycopg2.connect(
	dbname = 'postgres',
	user = 'postgres',
	host = 'postgres',
	#	port = 5432,
)
