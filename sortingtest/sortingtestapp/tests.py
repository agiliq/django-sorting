from django.test import TestCase
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpRequest
from django.test import Client
from django.core.handlers.wsgi import WSGIRequest
from django.test.client import Client


class RequestFactory(Client):

    """
    Class that lets you create mock Request objects for use in testing.

    Usage:

    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})

    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client

    Once you have a request object you can pass it to any view function,
    just as if that view had been hooked up using a URLconf.

    """

    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)
        return WSGIRequest(environ)


class TestTemplatetags(TestCase):

    def test_sort_links(self):
        "Test that using sort_link does not cause any error."
        template_str = """
        {% load sorting %}
        {% sort_link "link text" "field_name" "Visible name" %}
        """
        template = Template(template_str)
        rendered = template.render(Context({}))

    def test_sort_links_results(self):
        template_str = """
        {% load sorting %}
        {% sort_link "link text" "field_name" %}
        """
        template = Template(template_str)
        rendered = template.render(Context({}))
        print rendered

        template_str = """
        {% load sorting %}
        {% sort_link "link text" "field_name" "Visible name" %}
        """
        template = Template(template_str)
        rendered = template.render(Context({}))
        print rendered

    def test_auto_sort(self):
        from .sortingtestapp.models import SortableThingy
        sortable = SortableThingy.objects.all()
        template_str = """
        {% load sorting %}
        {% auto_sort sortable %}
        """
        template = Template(template_str)
        rendered = template.render(Context({"sortable": sortable}))

    def test_auto_sort_values(self):
        from .sortingtestapp.models import SortableThingy
        sortable = SortableThingy.objects.all()
        template_str = """
        {% load sorting %}
        {% auto_sort sortable %}
        """
        template = Template(template_str)
        rendered = template.render(Context({"sortable": sortable}))

    def test_auto_sort_urls(self):
        c = Client()
        c.get("/sorttest/")
        c.get("/sorttest/?sort_by=name")
        c.get("/sorttest/?sort_by=roll")
        c.get("/sorttest/xxx/?sort_by=name")
        c.get("/sorttest/xxx/?sort_by=parent")
