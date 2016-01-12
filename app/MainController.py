from app import app
from tornado.web import RequestHandler


class MainController(RequestHandler):
	def get(self):
		self.write("Hello, world")

app.add_handlers([
	(r"/", MainController),
])
