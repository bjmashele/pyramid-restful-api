from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def list_cap_cities(request): 
  return Response('List of capital cities\n')

def get_city(request):
  return Response('A city named %(name)s\n' % request.matchdict)

__name__ == '__main__'
config = Configurator()

config.add_route('cap_cities', '/cap_cities')
config.add_route('city', '/cities/{name}')

config.add_view(list_cap_cities, route_name='cap_cities')
config.add_view(get_city, route_name='city')

app = config.make_wsgi_app()
server = make_server('0.0.0.0', 6543, app)
server.serve_forever()