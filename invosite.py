# import flask web server
from flask import Flask


class Invosite:
    ''' Invomatic server node '''

    def __init__(self):
        '''Constructor for server node'''
        self.webapp = Flask(__name__)
        self.webapp.config['SECRET_KEY'] = 'secret' #TODO: change this
        from views import views
        from auth import auth
        self.webapp.register_blueprint(views, url_prefix='/')
        self.webapp.register_blueprint(auth, url_prefix='/')

    def start_webapp(self, debug=False):
        self.webapp.run(debug=debug)



if __name__ == '__main__':
    invosite = Invosite()
    invosite.start_webapp(debug=True)

