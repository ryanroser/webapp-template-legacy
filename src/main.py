"""
This is a simple web server that does not use Google App Engine.
It is used for demonstration purposes.
"""

import os
from paste.urlparser import StaticURLParser
from paste.cascade import Cascade
import webapp2
from webapp2_extras import jinja2

# This StaticFileHandler is from https://github.com/robspychala/webapp2_static/blob/master/webapp2_static.py
import mimetypes
class StaticFileHandler(webapp2.RequestHandler):
    def get(self, path):
        abs_path = os.path.abspath(os.path.join(self.app.config.get('static_file_path', 'static'), path))
        if os.path.isdir(abs_path) or abs_path.find(os.getcwd()) != 0:
            self.response.set_status(403)
            return
        try:
            f = open(abs_path, 'r')
            self.response.headers.add_header('Content-Type', mimetypes.guess_type(abs_path)[0])
            self.response.out.write(f.read())
            f.close()
        except:
            self.response.set_status(404)

# Create a basic handler class to allow for Jinja2 templates.
class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

# Handler for the main page
class MainHandler(BaseHandler):
    def get(self):
		context = {}
		self.render_response('main.html', **context)


# This configuration for static files is from:
# http://stackoverflow.com/questions/8470733/how-can-i-handle-static-files-with-python-webapp2-in-heroku
# Create the main app
web_app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/static/(.+)', StaticFileHandler)
], 
config = {'static_file_path': './static'},
debug=True)


def main():
    from paste import httpserver
    httpserver.serve(web_app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
