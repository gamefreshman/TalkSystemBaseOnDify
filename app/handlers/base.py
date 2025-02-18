import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,content-type")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    
    def options(self):
        self.set_status(204)
        self.finish() 