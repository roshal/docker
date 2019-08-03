
import time as p__time

from aiohttp import web as p__web

from . import functions as m__functions
from . import mongo as m__mongo
from . import postgres as m__postgres
from . import redis as m__redis


async def handle(request: p__web.Request) -> p__web.Response:
	value = 'hello'
	return p__web.Response(
		text = value,
	)

async def handle_time(request: p__web.Request) -> p__web.Response:
	value = p__time.time()
	value = str(value)
	return p__web.Response(
		text = value,
	)

async def handle_mongo(request: p__web.Request) -> p__web.Response:
	connection = m__mongo.connection
	database = connection['database']
	collection = database['collection']
	value = collection.insert_one({
		'value': 1,
	})
	value = collection.find()
	value = sum(value['value'] for value in value)
	value = str(value)
	value = m__functions.join('mongo', value)
	return p__web.Response(
		text = value,
	)

async def handle_postgres(request: p__web.Request) -> p__web.Response:
	with m__postgres.connection as connection:
		with connection.cursor() as cursor:
			cursor.execute('create table if not exists "table" ("key" serial primary key, "value" text)')
		with connection.cursor() as cursor:
			value = {
				'value': 'a',
			}
			cursor.execute('insert into "table" ("value") values (%(value)s)', value)
		with connection.cursor() as cursor:
			cursor.execute('select * from "table"')
			value = cursor.fetchall()
	value = [value[1] for value in value]
	value = m__functions.join('postgres', *value)
	return p__web.Response(
		text = value,
	)

async def handle_redis(request: p__web.Request) -> p__web.Response:
	connection = m__redis.connection
	connection.incr('key')
	value = connection.get('key').decode()
	value = m__functions.join('redis', value)
	return p__web.Response(
		text = value,
	)

async def handle_url(request: p__web.Request) -> p__web.Response:
	value = request.match_info.get('name')
	return p__web.Response(
		text = value,
	)

def function():
	routes = [
		p__web.route('get', '/', handle),
		p__web.route('get', '/mongo/', handle_mongo),
		p__web.route('get', '/postgres/', handle_postgres),
		p__web.route('get', '/redis/', handle_redis),
		p__web.route('get', '/time/', handle_time),
		p__web.route('get', '/url/{name}/', handle_url),
	]
	application = p__web.Application(
		debug = True,
	)
	application.add_routes(routes)
	p__web.run_app(application,
		port = 80,
	)
