from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.db import connections


class DatabaseMiddleware(object):
    '''
    This middleware tracks all database queries made by the Django
    application in a single request-response cycle.
    '''
    def __init__(self):
        if not settings.DEBUG:
            raise MiddlewareNotUsed()
        # TODO merge this with the default settings
        self.config = settings.DJANGO_LENS

    def process_request(self, request):
        '''
        Parses the `Accept` header to determine the desired response format.
        '''


    def process_response(self, request, response):
        '''
        Overrides the response with query information.
        '''
        if (
            settings.DEBUG is True and
            self.config['headers']['profile'] in request.META
        ):
            for connection in connections:
