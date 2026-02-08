import os
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_project.settings')

application = get_wsgi_application()

def test_app(environ, start_response):
    response_body = b"RENDER DJANGO WORKING"
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [response_body]
