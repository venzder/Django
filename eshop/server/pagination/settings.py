from django.conf import settings

PAGINATION_PAGE_SIZE = getattr(settings, 'PAGINATION_PAGE_SIZE', None)
