from app import app
from tornado.ioloop import IOLoop
from tornado.options import options, parse_command_line

parse_command_line()
app.listen(options.port)
IOLoop.current().start()
