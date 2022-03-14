=================
Falcon API Browse
=================

This project provides a middleware for `Falcon Web Framework
<https://falcon.readthedocs.io/en/stable/index.html>`_ that will render the
response in an HTML form for documentation purpose. It uses the docstring from
the Resource object as documentation and all the supported response types for
simpler documentation.


This project is inspired by Django Rest Framework's `Browsable API
<https://www.django-rest-framework.org/topics/browsable-api/>`_ and is written
using jinja2 templating language.

Installing
----------

This project is currently in early stages of development. Once it is stable
enough to be used by other projects, it will be provided via PyPI.

::

   pip install git+https://github.com/maxking/falcon-api-browse

Using
-----

Since this is a middleware for falcon, you can use it by passing an initialized
instance during Falcon App creation.

::

   from falcon import App
   from falcon_api_browse import HTMLResponseMiddleware

   app = App(middleware=HTMLResponseMiddleware())


LICENSE
-------

This project and contents of this repo are licensed under Apache 2.0 License.
