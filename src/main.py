import os.path
import tornado.locale
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import pymongo

define("port", default=8888, help="run on the given port", type=int)

class Blog:
	def __init__(self, blogDict):
		self.title = blogDict['title']
		self.detail = blogDict['detail']
		self.content = blogDict['content']
		self.comment = blogDict['comment']

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", IndexHandler),
		]
		settings = dict(
			template_path = os.path.join(os.path.dirname(__file__), "templates"),
			static_path = os.path.join(os.path.dirname(__file__), "static"),
			# ui_modules = {"Book": BookModule},
			debug = True,
		)
		conn = pymongo.Connection("localhost", 27017)
		self.db = conn["paperDB"]
		tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		allData = self.application.db.infoDB.find()
		doc = allData[0]
		blog = Blog(doc)
		# blog = {'title':blog_title, 'detail':blog_detail, 'content':blog_content}

		self.render("blog.html", blog = blog)

if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()