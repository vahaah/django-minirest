from django.conf import settings as base_settings

MINIREST_DEFAULT_PERMS = getattr(base_settings, "MINIREST_DEFAULT_PERMS", {
    'list': lambda request: True,
    'edit': lambda request: request.user.is_authenticated,
    'delete': lambda request: request.user.is_authenticated
})

MINIREST = getattr(base_settings, "MINIREST", {})
