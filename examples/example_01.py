import falcon
from falcon_api_browse import HTMLResponseMiddleware
from wsgiref.simple_server import make_server


class Hello:
    """Hello is the most important Handler for this App.

    It is important to greet people!
    """
    def on_get(self, req, resp):
        """Handles GET on /hello.

        This is the basic docstring for the GET method handler.
        """
        resp.media = {'message': 'Hello, World!', 'cool': True}
        resp.content_type = falcon.MEDIA_JSON

    def on_post(self, req, resp):
        """Handles POST on /hello.

        This is the basic docstring for the POST handler.
        """


app = falcon.App(middleware=[HTMLResponseMiddleware()])
app.add_route('/hello', Hello())


if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        print('Open http://localhost:8000/hello in browser to view')
        # Serve one request and then exit.
        httpd.serve_forever()
