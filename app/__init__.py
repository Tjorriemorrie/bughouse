import os
from tornado.web import Application, StaticFileHandler
from tornado.options import define
from app.MainHandler import MainHandler, WSHandler

STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

handlers = [
	(r'^/img/chesspieces/wikipedia/(.*)', StaticFileHandler, {'path': r'{}/chessboardjs-0.3.0/img/chesspieces/wikipedia/'.format(STATIC_PATH)}),
	(r'/ws', WSHandler),
	(r'/', MainHandler),
]

settings = {
	'debug': True,
	'static_path': STATIC_PATH,
	'cookie_secret': 'my geheime koekie',
	'xsrf_cookies': True,
	# 'login_url': '/login',
}

app = Application(
	handlers,
	**settings
)

define("port", default=8888, help="run on the given port", type=int)
