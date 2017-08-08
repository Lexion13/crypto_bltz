import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.template

from tornado.options import define, options
define("port", default=8080, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/currency", CurrencyHandler),
            (r"/test", TestHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={
                "Header": HeaderModule,
                "Footer": FooterModule,
                "Sidebar": SidebarModule
            },
            debug=True,
        )
        tornado.web
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title', "top page")
        name = self.get_argument('name', 'World')
        self.render('index.html', name=name, title=title)
        
class CurrencyHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title', "fuck currency")
        name = self.get_argument('name', "name")
        self.render('index.html')

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title', 'test page')
        self.render('test.html', title=title)

class HeaderModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('modules/header.html')

class FooterModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('modules/footer.html')

class SidebarModule(tornado.web.UIModule):
    def render(self):
        return self.render_string('modules/sidebar.html')

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
