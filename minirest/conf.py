from django.conf import settings as base_settings

MINIREST = getattr(base_settings, "MINIREST", {})
