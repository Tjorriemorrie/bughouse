from tornado.web import RequestHandler, asynchronous
from tornado.websocket import WebSocketHandler
from chess import uci, Board
import os
import json


class MainHandler(RequestHandler):
	@asynchronous
	def get(self):
		print 'index'
		# self.write("This is your response")
		self.render("index.html")

	# we don't need self.finish() because self.render() is fallowed by self.finish() inside tornado
	# self.finish()


# we gonna store clients in dictionary..
clients = dict()


class WSHandler(WebSocketHandler):
	def open(self, *args):
		print 'wohoo'
		self.id = self.get_argument("Id")
		self.stream.set_nodelay(True)
		clients[self.id] = {"id": self.id, "object": self}

		# is there bots as white?
		# make bot white move
		# with response do a write to client

	def on_message(self, message):
		"""
		when we receive some message we want some message handler..
		for this example i will just print message to console
		"""
		print "Client %s received a message : %s" % (self.id, message)
		# self.write_message('Server received: {}'.format(message))

		board = Board(fen=message)
		engine = uci.popen_engine("/Users/jaco/code/bughouse/stockfish-7-mac/Mac/stockfish-7-64")
		engine.uci()
		engine.setoption({'Ponder': False})
		engine.position(board)
		best_move = engine.go(wtime=60000, btime=60000)
		engine.quit()

		# print engine.options
		# options = OptionMap(
		# 	{
		# 		'Syzygy50MoveRule': Option(name='Syzygy50MoveRule', type='check', default=True, min=None, max=None,
		# 		                           var=[]),
		# 		'Ponder': Option(name='Ponder', type='check', default=False, min=None, max=None, var=[]),
		# 		'Hash': Option(name='Hash', type='spin', default=16, min=1, max=1048576, var=[]),
		# 		'Clear Hash': Option(name='Clear Hash', type='button', default='', min=None, max=None, var=[]),
		# 		'SyzygyProbeLimit': Option(name='SyzygyProbeLimit', type='spin', default=6, min=0, max=6,
		# 		                           var=[]),
		# 		'Write Debug Log': Option(name='Write Debug Log', type='check', default=False, min=None,
		# 		                          max=None, var=[]),
		# 		'SyzygyProbeDepth': Option(name='SyzygyProbeDepth', type='spin', default=1, min=1, max=100,
		# 		                           var=[]),
		# 		'Slow Mover': Option(name='Slow Mover', type='spin', default=84, min=10, max=1000, var=[]),
		# 		'SyzygyPath': Option(name='SyzygyPath', type='string', default='<empty>', min=None, max=None,
		# 		                     var=[]),
		# 		'UCI_Chess960': Option(name='UCI_Chess960', type='check', default=False, min=None, max=None,
		# 		                       var=[]),
		# 		'Threads': Option(name='Threads', type='spin', default=1, min=1, max=128, var=[]),
		# 		'Contempt': Option(name='Contempt', type='spin', default=0, min=-100, max=100, var=[]),
		# 		'Skill Level': Option(name='Skill Level', type='spin', default=20, min=0, max=20, var=[]),
		# 		'Move Overhead': Option(name='Move Overhead', type='spin', default=30, min=0, max=5000, var=[]),
		# 		'Minimum Thinking Time': Option(name='Minimum Thinking Time', type='spin', default=20, min=0,
		# 		                                max=5000, var=[]),
		# 		'nodestime': Option(name='nodestime', type='spin', default=0, min=0, max=10000, var=[]),
		# 		'MultiPV': Option(name='MultiPV', type='spin', default=1, min=1, max=500, var=[])
		# 	})

		msg = {
			'board': 'main',
			'from': str(best_move.bestmove)[:2],
			'to': str(best_move.bestmove)[-2:]
		}
		print 'replying {}'.format(msg)
		self.write_message(json.dumps(msg))

	def on_close(self):
		if self.id in clients:
			del clients[self.id]
