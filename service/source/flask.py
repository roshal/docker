
import flask as p__flask
import time as p__time


def handle():
	value = 'hello'
	return value

def function():
	flask = p__flask.Flask(__name__)
	flask.add_url_rule('/', None, handle)
	flask.run(
		host = '0.0.0.0',
		port = 80,
		debug = True,
	)
