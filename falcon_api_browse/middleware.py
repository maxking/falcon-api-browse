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

    async def process_response_async(self, request, response, resource, params):
        """Similar to :py:method:`process_response` but for ASGI.

        Since there isn't any expensive I/O in process_response, use the same
        method for ASGI too. The only I/O happening is reading the template
        from Disk to render the HTML.
        """
        return self.process_request(request, response, resource, params)
