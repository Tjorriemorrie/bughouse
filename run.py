import tornado.ioloop
from app import app

# run app
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
