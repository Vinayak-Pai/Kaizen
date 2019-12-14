# import cherrypy
#
# class demoExample:
#    def index(self):
#     return "Hello World!!!"
#    index.exposed = True
# cherrypy.quickstart(demoExample())

import json
import cherrypy

def error_page_404(status, message, traceback, version):
    return "404 Error!"

class HomeController():
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def GetStates(self, **kwargs):
        input_json = cherrypy.request.json
        filter_value = input_json["filter"].lower()

        with open('states.json', 'r') as chat_file:
            states_list = json.loads(chat_file.read())
            states_list = [s.lower() for s in states_list]
            return [s for s in states_list if filter_value in s]

def start_server():
    cherrypy.tree.mount(HomeController(), '/')
    cherrypy.config.update({'error_page.404': error_page_404})
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.engine.start()

if __name__ == '__main__':
    start_server()