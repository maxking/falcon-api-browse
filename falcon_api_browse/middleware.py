from falcon_api_browse.views import html_response


class HTMLResponseMiddleware:
    """Convert JSON response into an HTML page.

    This is a Middleware for Falcon web framework that convert a JSON response
    to an HTML page that lists requests, response and information about the
    resource handling the response.
    """

    def process_response(self, request, response, resource, params):
        """Convert JSON response into HTML if the client accepts HTML.

        :type request: :class:`falcon.Request`
        :type response: :class:`falcon.Response`
        :type resource: Falcon resource object.
        :type params: Response parameters.
        """
        accept_html = "text/html" in request.accept.split(",")
        if accept_html:
            html_response(request, response, resource, params)
