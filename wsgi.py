# -*- Encoding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options

from application import make_app

define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    options.parse_command_line()
    http_server = HTTPServer(WSGIContainer(make_app()))
    http_server.listen(options.port)
    IOLoop.instance().start()
