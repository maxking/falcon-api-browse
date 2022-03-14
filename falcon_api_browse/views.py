import json
import jinja2
import falcon
from importlib_resources import files


__all__ = [
    'get_template',
    'html_response',
    'ppjson',
]


def get_template(name):
    """Read templates for the response and return a Jinja2 template.

    :param name: The name of the template to load.
    :type name: str
    :returns: Jinja template.
    :rtype: :class:`jinja.Template`
    """
    jinja2.filters.FILTERS["ppjson"] = ppjson
    return jinja2.Template(
        files("falcon_api_browse.templates").joinpath(name).read_text()
    )


def html_response(request, response, resource, params):
    """Convert a JSON response into an HTML page.

    This converts a JSON request, resource and response into an HTML page and
    sets the correct return type, ``text/html``.

    :param request: The request object.
    :type request: :class:`falcon.Request`
    :param response: The response object.
    :type response: :class:`falcon.Response`
    :param resource: The Falcon resource object.
    :type resourse: Falcon resource object.
    :param params: The parameters passed to the resource.
    :type params: The response parameters.
    """
    template = get_template("base.html")
    response.text = template.render(
        response=response, request=request, resource=resource
    )
    response.content_type = "text/html"


def ppjson(value, indent=2):
    """Pretty print a json value.

    :param value: Json encoded string response.
    :type value: str
    :param indent: Number of spaces to indent each level.
    :type indent: int
    """
    if value:
        return json.dumps(json.loads(value), indent=indent)
    return ""
