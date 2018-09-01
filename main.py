import webapp2
import logging
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/home_page.html')
        self.response.write(template.render())

# BEGIN STUDY GROUP HANDLERS
class StudyGroupViewCollegesHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_view_colleges.html')
        self.response.write(template.render())

class StudyGroupViewClassesHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_view_classes.html')
        self.response.write(template.render())

class StudyGroupViewGroupsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_view_groups.html')
        self.response.write(template.render())

class StudyGroupViewGroupHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_view_group.html')
        self.response.write(template.render())

class StudyGroupAddCollegeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_add_college.html')
        self.response.write(template.render())

    def post(self):
        logging.info("DO SOMETHING HERE")

class StudyGroupAddClassHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_add_class.html')
        self.response.write(template.render())

    def post(self):
        logging.info("DO SOMETHING HERE")

class StudyGroupAddGroupHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template('static/studygroup_add_group.html')
        self.response.write(template.render())

    def post(self):
        logging.info("DO SOMETHING HERE")

# END STUDY GROUP HANDLERS


app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/view_colleges', StudyGroupViewCollegesHandler),
    ('/view_classes', StudyGroupViewClassesHandler),
    ('/view_groups', StudyGroupViewGroupsHandler),
    ('/view_group', StudyGroupViewGroupHandler),
    ('/add_college', StudyGroupAddCollegeHandler),
    ('/add_class', StudyGroupAddClassHandler),
    ('/add_group', StudyGroupAddGroupHandler)
], debug=True)
