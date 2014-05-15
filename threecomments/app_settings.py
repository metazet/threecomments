# coding: utf-8
from django.conf import settings

# allow profanities
THREECOMMENTS_ALLOW_PROFANITIES = getattr(settings, 'THREECOMMENTS_ALLOW_PROFANITIES', False)

# list of profanities
THREECOMMENTS_PROFANITIES_LIST = getattr(settings, 'THREECOMMENTS_PROFANITIES_LIST', [])
