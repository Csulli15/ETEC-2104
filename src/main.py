import cherrypy
import mako.template
import mako.lookup
import os.path
import random
import quotes
import datetime

names = ["Alice","Bob","Carol","Dave"]

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)]
)


class App:

    @cherrypy.expose
    def quote(self):
        q = random.choice(quotes.quotations)
        t = lookup.get_template("quotes.html")
        return t.render(quote=q)
    
    @cherrypy.expose
    def index(self):
        h = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        q = random.choice(quotes.quotations)
        n = random.choice(names)
        return h.render(quote=q, name=n)

    @cherrypy.expose
    def test(self):
        a = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return a.render()

    @cherrypy.expose
    def posts(self):
        p = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        time = []
        views = []
        l = 0
        while (l < 10):
            x = datetime.timedelta(minutes=random.randrange(8000))
            hoursago = int( x.seconds / 3600 )
            minutesago = round( (x.seconds - hoursago*3600)/60 )
            time.append(f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago")
            views.append(random.randint(1, 2500))
            l += 1
        return p.render(time=time, views=views)

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