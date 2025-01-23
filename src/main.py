import cherrypy
import mako.template
import os.path

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        h = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return h.render()

    @cherrypy.expose
    def test(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return t.render()

    @cherrypy.expose
    def posts(self):
        p = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return p.render()

    @cherrypy.expose
    def signup(self):
        s = mako.template.Template(filename=f"{PYPATH}/../Html/signup.html")
        return s.render()


srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)