from webob import Request, Response

class Wsgiclass:
    def __init__(self):
        self.rutas = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def ruta(self, path, methods=None):
        if methods is None:
            methods=['GET']
    
        def wrapper(controlador):
            self.rutas[path] = {'controller': controlador, 'methods': methods}
            return controlador

        return wrapper

    def handle_request(self, request):
        response = Response()
        for path, route_info in self.rutas.items():
            if path == request.path and request.method in route_info['methods']:
                return route_info['controller'](request, response)
        response = self.default_response()
        return response
    
    def default_response(self):
        response = Response()
        response.status_code = 404
        response.text = "Página no encontrada"
        return response